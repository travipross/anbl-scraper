from anbl_scraper import CATEGORY_IDS
from anbl_scraper.utils.csv_utils import write_product_link_csv
from anbl_scraper.utils.ajax_utils import (
    get_number_of_pages,
    get_number_of_products,
    fetch_func_factory,
)
from concurrent.futures import ThreadPoolExecutor
import argparse
import os

#TODO: Fetch products as model.Product objects.
def fetch_products_threaded(category, page_size, max_workers=20, dry_run=False):
    n_prods = get_number_of_products(category)
    n_pages = get_number_of_pages(n_prods, page_size)
    fetch_func = fetch_func_factory(category, page_size)

    page_range = [1] if dry_run else range(1, n_pages + 1)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        res = executor.map(fetch_func, page_range)

    return [p for r in res for p in r]


def crawl(output_path="~/Downloads", page_size=20, categories=None, dry_run=False):
    if dry_run:
        categories = ["beer"]
    elif categories is None:
        categories = CATEGORY_IDS.keys()
    elif not set(categories).issubset(set(CATEGORY_IDS.keys())):
        raise KeyError(f"Unknown keys: {set(categories) - set(CATEGORY_IDS.keys())}")

    products = []
    print(f"Fetching {page_size} products at a time per thread...")
    for product_type in categories:
        product_list = fetch_products_threaded(
            product_type, page_size, max_workers=100, dry_run=dry_run
        )
        print(f"Number of {product_type} products: {len(product_list)}")
        products.extend(product_list)

    if len(products):
        if dry_run:
            print("Products:\n" + "-" * 9)
            for p in products:
                print(p)
        else:
            write_product_link_csv(output_path, products)
    else:
        print("Can't save to file as no products were returned")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--output-path",
        default="~/Downloads",
        help="Path to output file or directory.",
    )
    parser.add_argument(
        "-p",
        "--page-size",
        default=20,
        help="Number of product results to fetch per request.",
    )
    parser.add_argument(
        "-c",
        "--categories",
        nargs="+",
        default=None,
        help="Space-separated list of categories of product results to crawl.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scrape a single page of results and don't save to CSV.",
    )
    args = parser.parse_args()

    print(f"Running with args: {vars(args)}")
    crawl(
        output_path=args.output_path,
        page_size=args.page_size,
        categories=args.categories,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
