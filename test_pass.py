import requests
import bs4

BASE_URL = "https://anbl.com"
BEER_URL = BASE_URL + "/beer"
INDEX_URL = BASE_URL + "/ecomwgtproductlisting/pagedindex"

SORT_MODES = {
    'name': '3',
    'price_low_high': '4',
    'price_high_low': '5'
}

CATEGORY_IDS = {
    'beer': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiYWUxZTk0ZjYtYzY4OC00ODQzLTlkMGUtZDM4YTVlZGJjNDQ2IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjcyLCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
    'spirits': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiNmJiYjA3ZTQtOWFlZC00MWE2LThiZjAtNTIxYzg0M2ZkNDk2IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjcyLCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
    'other_cider_coolers': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiMzM1Y2NiYWUtM2Y5MS00MWY5LWE3NjEtZWJmNzY4M2VkN2Q4IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjI0LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
    'cider': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiMmUzY2E3NDYtOWE5My00MTM1LWE2MDEtZWExN2QyOTFhNDIwIiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjQ4LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
    'coolers': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiYTE3N2QzNTctZTAyZi00YWIzLWFjNmMtMzYwYjg3Njg1ZGIzIiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjI0LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
    'wine': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiOTlhNmJmMjEtY2FhMy00ZWJjLTlkNGEtZDJhNjNmODMzNmE3IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjQ4LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
    'whiskey': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiODAxYzI4ZGQtN2UzYi00NzdhLTg0MzEtNWE0Mjc1MGU1OTZhIiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjQ4LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
}


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
        'categoryId': CATEGORY_IDS['wine'],
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

