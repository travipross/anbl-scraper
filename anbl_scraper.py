import json
import re
from requests_html import HTMLSession

results_json = "run_results.json"
with open(results_json) as f:
    data = json.load(f)

# for category in data.get("product_categories"):
#     print(category.get("name"))
#     products = category.get("product")
#     for product in products:
#         continue
#         # print("%s - %s" %  (product.get("name"), product.get("url")))

# def scrape_for_metadata(prod):
#     page = requests.get(prod.get("url"))
#
#


sample_product = data["product_categories"][0]["product"][0]
session = HTMLSession()
r = session.get(sample_product.get("url"))


# search for all products
try:
    abv_text = r.html.find(".information-attribute", containing="Alcohol content").pop().text
    abv = float(re.search("Alcohol content : (.+)%", abv_text).group(1))
except IndexError:
    # couldn't find abv on page
    abv = None

try:
    vol_text = r.html.find(".information-attribute", containing="Container Size").pop().text
    vol = int(re.search("Container Size : (.+) mL", vol_text).group(1))
except IndexError:
    vol = None

try:
    qty_text = r.html.find(".information-attribute", containing="Quantity per container").pop().text
    qty = int(re.search("Quantity per container : (.+)", qty_text).group(1))
except IndexError:
    qty = 1

try:
    price_current_text = r.html.find(".price-current").pop().text
    price_current = float(re.search("\$(.+) /UNIT", price_current_text).group(1))
except IndexError:
    price_current = None

try:
    price_regular_text = r.html.find(".price-before-discount").pop().text
    price_regular = float(re.search("\$(.+)", price_regular_text).group(1))
except IndexError:
    price_regular = price_current

d = {"abv": abv,
     "vol_ml": vol,
     "qty": qty,
     "price_current": price_current,
     "price_regular": price_regular}

sample_product.update(d)