import requests
import bs4
# session = requests.Session()

BASE_URL = "https://anbl.com"
BEER_URL = BASE_URL + "/beer"

INDEX_URL = BASE_URL + "/ecomwgtproductlisting/pagedindex"

# session.get(BEER_URL)

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.anbl.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.anbl.com/beer',
    'Accept-Language': 'en-US,en;q=0.9',

    # "Host": "www.anbl.com",
    # "Content-Length": "1076",
    
    # "Accept-Encoding": "gzip, deflate, br",
}

data= {
    "categoryId": "eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiYWUxZTk0ZjYtYzY4OC00ODQzLTlkMGUtZDM4YTVlZGJjNDQ2IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjI0LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==",
    "subCategoryId": "00000000-0000-0000-0000-000000000000",
    "widgetCode": "EcomWGTProductListing",
    "displayMode": "grid",
    "pageFrom": '1',
    "pageTo": '1',
    "userResultPerPage": '100',
    "sortBy": '4',
    "filterBy": "all",
    "uniqueListingString": "eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiYWUxZTk0ZjYtYzY4OC00ODQzLTlkMGUtZDM4YTVlZGJjNDQ2IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjI0LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==",
    "widgetUniqueCode": "SdWlppw1TpFAaFHqsHbZSrnkUDJdN0iIBCSwZrYRytezwBKq8yus4ZC+KiG/Jo/v",
}


resp = requests.post(INDEX_URL, headers=headers, data=data)
print(resp)
soup = bs4.BeautifulSoup(resp.text, "html.parser")
print(len(resp.text))
print(soup)