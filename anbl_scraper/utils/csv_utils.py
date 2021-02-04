from argparse import ArgumentError
import csv
import os
import datetime
from anbl_scraper import CSV_HEADER_CRAWL, CSV_HEADER_SCRAPE


def write_product_link_csv(outpath, products, listing_type="crawl"):
    if listing_type not in ["crawl", "scrape"]:
        raise ArgumentError(f"Invalid CSV type: {listing_type}")

    outfile = os.path.expanduser(outpath)

    # if no extension, assume directory was provided
    _, ext = os.path.splitext(outfile)
    if not ext:
        outfile = os.path.join(
            outfile,
            datetime.datetime.now().strftime(f"{listing_type}_%Y-%m-%d_%H-%M-%S.csv"),
        )

    # Create directory if it doesn't exist
    outdir = os.path.dirname(outfile)
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Create file and write CSV
    print(f"Writing {len(products)} products to file: {outfile}")
    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=(
                CSV_HEADER_SCRAPE if listing_type == "scrape" else CSV_HEADER_CRAWL
            ),
            extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(products)


def read_product_link_csv(inpath):
    with open(os.path.expanduser(inpath), newline="") as f:
        reader = csv.DictReader(f)
        return list(map(dict, reader))
