import pytest
from anbl_scraper.utils.ajax_utils import build_data_payload, get_number_of_pages


def test_form_data():
    data = build_data_payload("cider_coolers_other", 1, 1)

    assert data == {
        "categoryId": "eyJRdWlja1NlYXJjaFN0cmluZyI6bnVsbCwiS2V5d29yZCI6bnVsbCwiQnJhbmQiOm51bGwsIkNhdGVnb3J5IjoiMzM1Y2NiYWUtM2Y5MS00MWY5LWE3NjEtZWJmNzY4M2VkN2Q4IiwiU3VwcGxpZXIiOm51bGwsIlNlYXJjaEluIjpudWxsLCJDcml0ZXJpYSI6bnVsbCwiUGFnZU51bWJlckZyb20iOjEsIlBhZ2VOdW1iZXJUbyI6MSwiVXNlclJlc3VsdFBlclBhZ2UiOjI0LCJJZFByb21vdGlvbkZyb20iOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJQb3dlclNlYXJjaEZpbHRlcnMiOiIifQ==",
        "pageFrom": "1",
        "pageTo": "1",
        "userResultPerPage": "1",
        "sortBy": "3",
        "displayMode": "list",
        "widgetUniqueCode": "SdWlppw1TpFAaFHqsHbZSrnkUDJdN0iIBCSwZrYRytezwBKq8yus4ZC+KiG/Jo/v",
    }


@pytest.mark.parametrize(
    "page_size, n_prods, n_pages", [(24, 100, 5), (25, 100, 4), (26, 100, 4)]
)
def test_num_pages(page_size, n_prods, n_pages):
    assert n_pages == get_number_of_pages(n_prods, page_size)
