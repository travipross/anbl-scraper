import csv
import os
import datetime


def write_product_link_csv(outpath, products):
    outfile = os.path.expanduser(outpath)

    # if no extension, assume directory was provided
    _, ext = os.path.splitext(outfile)
    if not ext:
        outfile = os.path.join(
            outfile, datetime.datetime.now().strftime("crawl_%Y-%m-%d_%H-%M-%S.csv")
        )

    # Create directory if it doesn't exist
    outdir = os.path.dirname(outfile)
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Create file and write CSV
    print(f"Writing products to file: {outfile}")
    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)


def read_product_link_csv(inpath):
    with open(os.path.expanduser(inpath), newline="") as f:
        reader = csv.DictReader(f)
        return list(map(dict, reader))
