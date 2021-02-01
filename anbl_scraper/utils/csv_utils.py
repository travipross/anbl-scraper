import csv
import os


def write_product_link_csv(outpath, products):
    with open(os.path.expanduser(outpath), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)