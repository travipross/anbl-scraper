from anbl_scraper import CATEGORY_IDS
from anbl_scraper.utils.csv_utils import write_product_link_csv
from anbl_scraper.utils.ajax_utils import (
    get_number_of_pages,
    get_number_of_products,
    page_fetcher_factory,
)

from concurrent.futures import ThreadPoolExecutor


def fetch_products_threaded(category, page_size, max_workers=20):
    n_prods = get_number_of_products(category)
    n_pages = get_number_of_pages(n_prods, page_size)
    fetcher = page_fetcher_factory(category, page_size)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        res = executor.map(fetcher, range(1, n_pages + 1))

    return [p for r in res for p in r]


def main():
    output_path = "~/Desktop/test.csv"
    page_size = 20
    products = []
    print(f"Fetching {page_size} products at a time per thread...")
    for product_type in CATEGORY_IDS.keys():
        product_list = fetch_products_threaded(product_type, page_size, max_workers=100)
        print(f"Number of {product_type} products: {len(product_list)}")
        products.extend(product_list)

    if len(products):
        write_product_link_csv(output_path, products)
    else:
        print("Can't save to file as no products were returned")


if __name__ == "__main__":
    main()
