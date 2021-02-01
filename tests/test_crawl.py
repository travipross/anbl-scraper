from anbl_scraper.crawl import build_data_payload

def test_form_data():
    data = build_data_payload('cider', 1, 1)

    assert data == {
        'categoryId': 'eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiMmUzY2E3NDYtOWE5My00MTM1LWE2MDEtZWExN2QyOTFhNDIwIiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjQ4LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==',
        'pageFrom': '1',
        'pageTo': '1',
        'userResultPerPage': '1',
        'sortBy': '3',
        'displayMode': 'list',
        'widgetUniqueCode': 'SdWlppw1TpFAaFHqsHbZSrnkUDJdN0iIBCSwZrYRytezwBKq8yus4ZC+KiG/Jo/v',
    }