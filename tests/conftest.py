import pytest
import os
import bs4

def load_page(page_name):
    current_path = os.path.realpath(__file__)
    test_resources_dir = os.path.join(os.path.dirname(current_path), "resources")
    with open(os.path.join(test_resources_dir, page_name)) as f:
        return f.read()


@pytest.fixture
def sample_page():
    return load_page("sample-page.html")

@pytest.fixture
def sample_soup(sample_page):
    return bs4.BeautifulSoup(sample_page, 'html.parser')

@pytest.fixture
def sample_page_sale():
    return load_page("sample-page-sale.html")

@pytest.fixture
def sample_soup_sale(sample_page_sale):
    return bs4.BeautifulSoup(sample_page_sale, 'html.parser')