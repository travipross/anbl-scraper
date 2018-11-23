import json
import re
import queue
import time
from threading import Thread
from requests_html import HTMLSession


def update_product_with_metadata(html_session, product, max_attempts=5):
    # try up to 5 times to load the product page
    attempt = 0
    while True:
        if attempt > max_attempts:
            print("ERROR LOADING PAGE: %s" % product["name"])
            return False  # could not get web page / read any data
        attempt = attempt + 1
        try:
            r = html_session.get(product.get("url"))
            break
        except ConnectionResetError:
            continue

    # preset return flag
    success = True

    # get abv
    try:
        abv_text = r.html.find(".information-attribute", containing="Alcohol content").pop().text
        abv = float(re.search("Alcohol content : (.+)%", abv_text).group(1))
    except IndexError:
        # couldn't find abv on page
        abv = None
        success = False

    # get vol
    try:
        vol_text = r.html.find(".information-attribute", containing="Container Size").pop().text
        vol = int(re.search("Container Size : (.+) mL", vol_text).group(1))
    except IndexError:
        vol = None
        success = False

    # get qty
    try:
        qty_text = r.html.find(".information-attribute", containing="Quantity per container").pop().text
        qty = int(re.search("Quantity per container : (.+)", qty_text).group(1))
    except IndexError:
        qty = 1

    # get current price
    try:
        price_current_text = r.html.find(".price-current").pop().text
        price_current = float(re.search("\$(.+) /UNIT", price_current_text).group(1).replace(",", ""))
    except IndexError:
        price_current = None
        success = False

    # get regular price
    try:
        price_regular_text = r.html.find(".price-before-discount").pop().text
        price_regular = float(re.search("\$(.+)", price_regular_text).group(1).replace(",", ""))
    except IndexError:
        price_regular = price_current

    # get mL alcohol per dollar
    try:
        ml_alcohol_per_dollar = float(qty) * float(vol) * (abv/100.0) / price_regular
    except TypeError:
        ml_alcohol_per_dollar = None
        success = False

    # get mL alcohol per dollar (sale)
    try:
        ml_alcohol_per_dollar_sale = float(qty) * float(vol) * (abv/100.0) / price_current
    except TypeError:
        ml_alcohol_per_dollar_sale = None
        success = False

    # update product dict
    d = {"abv": abv,
         "vol_ml": vol,
         "qty": qty,
         "price_current": price_current,
         "price_regular": price_regular,
         "ml_alc_per_dollar": ml_alcohol_per_dollar,
         "ml_alc_per_dollar_sale": ml_alcohol_per_dollar_sale}
    product.update(d)

    return success


# load json file with results
results_json = "run_results.json"
with open(results_json) as f:
    data = json.load(f)

# Initialize a queue object
q = queue.Queue()

# loop over all products and output to disk
n = 0
for category in data["product_categories"]:
    print("Queueing all products in [%s] category..." % category["name"])
    for item in category["product"]:
        q.put([item, n])
        n = n + 1
print("%d products queued" % n)


def url_scraper_worker(q):
    session = HTMLSession()
    while not q.empty():
        [product, n] = q.get()
        success = update_product_with_metadata(session, product)
        print("%d: %s... " % (n, product["name"]), end="")
        print("Success") if success else print("Some data missing")


max_workers = 20
workers_list = []
for i in range(max_workers):
    workers_list.append(Thread(target=url_scraper_worker, args=(q,)))
    workers_list[i].start()
    print("Started worker %d" % (i+1))

# save new results to disk every 5 seconds
output_name = "parsed_data.json"
while not q.empty():
    with open(output_name, 'w') as f:
        json.dump(data, f, indent=4)
    time.sleep(5)
