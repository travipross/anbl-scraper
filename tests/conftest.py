import pytest
import os
import bs4


def load_page(test_resources_dir, page_name):
    with open(os.path.join(test_resources_dir, page_name)) as f:
        return f.read()


@pytest.fixture
def test_resources_path():
    current_path = os.path.realpath(__file__)
    return os.path.join(os.path.dirname(current_path), "resources")


@pytest.fixture
def sample_page(test_resources_path):
    return load_page(test_resources_path, "sample-page.html")


@pytest.fixture
def sample_soup(sample_page):
    return bs4.BeautifulSoup(sample_page, "html.parser")


@pytest.fixture
def sample_page_sale(test_resources_path):
    return load_page(test_resources_path, "sample-page-sale.html")


@pytest.fixture
def sample_soup_sale(sample_page_sale):
    return bs4.BeautifulSoup(sample_page_sale, "html.parser")


@pytest.fixture
def sample_product_list():
    return [
        {
            "link": "https://www.anbl.com/beer/13-barrels-brewing-miss-clara-s-kolsch-473ml-34918",
            "name": "13 Barrels Brewing Miss Clara's Kolsch 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/13-barrels-brewing-pabineau-pale-ale-473ml-33811",
            "name": "13 Barrels Brewing Pabineau Pale Ale 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/13-barrels-brewing-rendez-vous-rouge-473ml-33920",
            "name": "13 Barrels Brewing Rendez-Vous Rouge 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/13-barrels-brewing-tall-tales-ipa-473ml-33810",
            "name": "13 Barrels Brewing Tall Tales IPA 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/13-barrels-brewing-tipsy-barrel-radler-473ml-36634",
            "name": "13 Barrels Brewing Tipsy Barrel Radler 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/13-barrels-brewing-wild-goose-stout-473ml-34890",
            "name": "13 Barrels Brewing Wild Goose Stout 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/2-crows-brewing-i-love-you-brett-saison-473ml-37115",
            "name": "2 Crows Brewing I Love You Brett Saison 473ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/3-fonteinen-oude-geuze-cuvee-armand-gaston-375ml-34841",
            "name": "3 Fonteinen Oude Geuze Cuvee Armand & Gaston 375ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/3flip-brewing-americana-track-4-355ml-36931",
            "name": "3Flip Brewing Americana Track 4 355ml",
            "category": "beer",
        },
        {
            "link": "https://www.anbl.com/beer/3flip-brewing-anonymous-amber-ale-355ml-36932",
            "name": "3Flip Brewing Anonymous Amber Ale 355ml",
            "category": "beer",
        },
    ]
