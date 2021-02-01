from anbl_scraper import INDEX_URL, SORT_MODES, CATEGORY_IDS
import requests
import bs4


# headers = {
#     'Connection': 'keep-alive',
#     'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
#     'Accept': '*/*',
#     'X-Requested-With': 'XMLHttpRequest',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://www.anbl.com',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Referer': 'https://www.anbl.com/beer',
#     'Accept-Language': 'en-US,en;q=0.9',
# }



def build_data_payload(category, page, page_size, sort_mode=SORT_MODES['name']):
    data = {
        'categoryId': CATEGORY_IDS[category],
        'pageFrom': str(page),
        'pageTo': str(page),
        'userResultPerPage': str(page_size),
        'sortBy': str(sort_mode),
        'displayMode': 'list',
        'widgetUniqueCode': 'SdWlppw1TpFAaFHqsHbZSrnkUDJdN0iIBCSwZrYRytezwBKq8yus4ZC+KiG/Jo/v',
        # 'filterBy': 'all',
        # 'uniqueListingString': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiYWUxZTk0ZjYtYzY4OC00ODQzLTlkMGUtZDM4YTVlZGJjNDQ2IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjcyLCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
        # 'subCategoryId': '00000000-0000-0000-0000-000000000000',
        # 'widgetCode': 'EcomWGTProductListing',
    }
    return data

def get_number_of_products(category):
    data = build_data_payload(category, page=1, page_size=1)
    soup = bs4.BeautifulSoup(
        requests.post(INDEX_URL, data=data).text, 
        'html.parser'
        )
    print(soup)
    n_products = int(soup.find(id="ProductsTotalCount").attrs['value'])
    
    return n_products

def get_number_of_pages(n_products, page_size):
    return n_products // page_size + ( 0 if n_products%page_size == 0 else 1 )



if __name__ == "__main__":
    page_size = 100
    product_type = 'cider'
    n_prods = get_number_of_products(product_type)
    n_pages = get_number_of_pages(n_prods, page_size)

    products = []
    for page in range(n_pages):
        data = build_data_payload(product_type, page, page_size)
        response = requests.post(INDEX_URL, data=data)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        product_soup = soup.find_all(class_='product-title')

        print([ p.a.attrs['href'] for p in products ])
        print(f'Number of products: {len(product_soup)}')