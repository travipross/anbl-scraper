import json
import csv

in_file = "parsed_data.json"
with open(in_file) as f:
    data = json.load(f)


out_file = "parsed_data.csv"
with open(out_file, 'w') as ff:
    writer = csv.writer(ff, delimiter=",", quotechar="|", )
    writer.writerow(["Category",
                     "Product",
                     "Volume (mL)",
                     "ABV (%)",
                     "qty",
                     "Current Price ($)",
                     "Regular Price ($)",
                     "mL / $",
                     "mL / $ (sale)"])

    for cat in data["product_categories"]:
        for prod in cat["product"]:
            row = [
                cat.get("name"),
                prod.get("name"),
                prod.get("vol_ml"),
                prod.get("abv"),
                prod.get("qty"),
                prod.get("price_current"),
                prod.get("price_regular"),
                prod.get("ml_alc_per_dollar"),
                prod.get("ml_alc_per_dollar_sale"),
                ]
            writer.writerow(row)

print("Done")