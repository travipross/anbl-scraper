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


def get_products_ajax(category, page, page_size):
    data = build_data_payload(category, page, page_size)
    resp = requests.post(INDEX_URL, data=data)
    if resp.status_code != 200:
        raise Exception(f"BAD RESPONSE: {resp.status_code}")
    else:
        return resp.text


def get_number_of_products(category):
    soup = bs4.BeautifulSoup(
        get_products_ajax(category, page=1, page_size=1), "html.parser"
    )
    n_products = int(soup.find(id="ProductsTotalCount").attrs["value"])

    return n_products


def get_number_of_pages(n_products, page_size):
    return n_products // page_size + (0 if n_products % page_size == 0 else 1)


def extract_product_info(product_list_element, product_type=None):
    info = product_list_element.a.attrs
    info["link"] = info.pop("href")
    info["name"] = info.pop("title").replace("\t", "")
    info["category"] = product_type
    return info


def fetch_func_factory(product_type, page_size):
    def fetcher(page):
        raw = get_products_ajax(product_type, page, page_size)
        soup = bs4.BeautifulSoup(raw, "html.parser")
        product_soup = soup.find_all(class_="product-title")
        products = [extract_product_info(p, product_type) for p in product_soup]

        return products

    return fetcher


def get_page_of_product_info(product_type, page, page_size):
    raw = get_products_ajax(product_type, page, page_size)
    soup = bs4.BeautifulSoup(raw, "html.parser")
    product_soup = soup.find_all(class_="product-title")
    products = [extract_product_info(p) for p in product_soup]

    return products
