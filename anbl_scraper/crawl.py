from anbl_scraper import INDEX_URL, SORT_MODES, CATEGORY_IDS
import requests
import bs4


def build_data_payload(category, page, page_size, sort_mode=SORT_MODES["name"]):
    data = {
        "categoryId": CATEGORY_IDS[category],
        "pageFrom": str(page),
        "pageTo": str(page),
        "userResultPerPage": str(page_size),
        "sortBy": str(sort_mode),
        "displayMode": "list",
        "widgetUniqueCode": "SdWlppw1TpFAaFHqsHbZSrnkUDJdN0iIBCSwZrYRytezwBKq8yus4ZC+KiG/Jo/v",
    }
    return data


def get_products_html(category, page, page_size):
    data = build_data_payload(category, page, page_size)
    resp = requests.post(INDEX_URL, data=data)
    if resp.status_code != 200:
        raise Exception(f"BAD RESPONSE: {resp.status_code}")
    else:
        return resp.text


def get_number_of_products(category):
    soup = bs4.BeautifulSoup(
        get_products_html(category, page=1, page_size=1), "html.parser"
    )
    n_products = int(soup.find(id="ProductsTotalCount").attrs["value"])

    return n_products


def get_number_of_pages(n_products, page_size):
    return n_products // page_size + (0 if n_products % page_size == 0 else 1)


if __name__ == "__main__":
    page_size = 100
    product_type = "cider"
    n_prods = get_number_of_products(product_type)
    n_pages = get_number_of_pages(n_prods, page_size)

    products = []
    for page in range(1, n_pages + 1):
        raw = get_products_html(product_type, page, page_size)
        soup = bs4.BeautifulSoup(raw, "html.parser")
        product_soup = soup.find_all(class_="product-title")

        print([p.a.attrs["href"] for p in products])
        print(f"Number of products: {len(product_soup)}")
