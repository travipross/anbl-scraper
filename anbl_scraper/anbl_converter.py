import json
import csv


def main():
    in_file = "parsed_data.json"
    out_file = "parsed_data.csv"
    with open(in_file) as f:
        data = json.load(f)
    anbl_csv_writer(data, out_file)
    print("Done")


def anbl_csv_writer(data, filename):
    with open(filename, 'w') as ff:
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


if __name__ == "__main__":
    main()
