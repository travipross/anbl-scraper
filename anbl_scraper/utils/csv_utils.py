import csv
import os


def write_product_link_csv(outpath, products):
    with open(os.path.expanduser(outpath), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)


def read_product_link_csv(inpath):
    with open(os.path.expanduser(inpath), newline="") as f:
        reader = csv.DictReader(f)
        return list(map(dict, reader))
