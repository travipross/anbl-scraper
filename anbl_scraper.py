import json
import re
from requests_html import HTMLSession


def update_product_with_metadata(html_session, product):
    r = html_session.get(product.get("url"))
    # get abv
    try:
        abv_text = r.html.find(".information-attribute", containing="Alcohol content").pop().text
        abv = float(re.search("Alcohol content : (.+)%", abv_text).group(1))
    except IndexError:
        # couldn't find abv on page
        abv = None

    # get vol
    try:
        vol_text = r.html.find(".information-attribute", containing="Container Size").pop().text
        vol = int(re.search("Container Size : (.+) mL", vol_text).group(1))
    except IndexError:
        vol = None

    # get qty
    try:
        qty_text = r.html.find(".information-attribute", containing="Quantity per container").pop().text
        qty = int(re.search("Quantity per container : (.+)", qty_text).group(1))
    except IndexError:
        qty = 1

    # get current price
    try:
        price_current_text = r.html.find(".price-current").pop().text
        price_current = float(re.search("\$(.+) /UNIT", price_current_text).group(1))
    except IndexError:
        price_current = None

    # get regular price
    try:
        price_regular_text = r.html.find(".price-before-discount").pop().text
        price_regular = float(re.search("\$(.+)", price_regular_text).group(1))
    except IndexError:
        price_regular = price_current

    # get mL alcohol per dollar
    try:
        ml_alcohol_per_dollar = float(qty) * float(vol) * (abv/100.0) / price_regular
    except TypeError:
        ml_alcohol_per_dollar = None

    # get mL alcohol per dollar (sale)
    try:
        ml_alcohol_per_dollar_sale = float(qty) * float(vol) * (abv/100.0) / price_current
    except TypeError:
        ml_alcohol_per_dollar_sale = None

    # update product dict
    d = {"abv": abv,
         "vol_ml": vol,
         "qty": qty,
         "price_current": price_current,
         "price_regular": price_regular,
         "ml_alc_per_dollar": ml_alcohol_per_dollar,
         "ml_alc_per_dollar_sale": ml_alcohol_per_dollar_sale}

    product.update(d)


# load json file with results
results_json = "run_results.json"
with open(results_json) as f:
    data = json.load(f)

# run single example
session = HTMLSession()
sample_product = data["product_categories"][0]["product"][0]
update_product_with_metadata(session,sample_product)
