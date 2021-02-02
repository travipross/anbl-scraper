import requests
import bs4
from anbl_scraper.utils.scrape_utils import get_product_attrs


class Product:
    META_KEYS = [
        "abv_prct",
        "quantity_per_container",
        "container_size_ml",
        "country_of_origin",
        "price_reg",
        "price_sale",
    ]

    def __init__(self, name, link, category, **kwargs):
        self.name = name
        self.link = link
        self.category = category
        self.abv_prct = kwargs.get("abv_prct")
        self.quantity_per_container = kwargs.get("quantity_per_container")
        self.container_size_ml = kwargs.get("container_size_ml")
        self.country_of_origin = kwargs.get("country_of_origin")
        self.price_reg = kwargs.get("price_reg")
        self.price_sale = kwargs.get("price_sale")
        self.cached_page = None

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return vars(self)

    def fetch_product_page(self, force_refresh=False):
        if force_refresh or not self.cached_page:
            resp = requests.get(self.link)
            if resp.status_code == 200:
                self.cached_page = resp.text
        return self.cached_page

    def fetch_product_soup(self, force_refresh=False):
        return bs4.BeautifulSoup(
            self.fetch_product_page(force_refresh=force_refresh), "html.parser"
        )

    def refresh_metadata(self):
        meta = get_product_attrs(self.fetch_product_soup(force_refresh=True))
        for key in self.META_KEYS:
            if meta.get(key):
                setattr(self, key, meta.get(key))
