import requests
import bs4
import datetime
from anbl_scraper.utils.scrape_utils import get_product_attrs


class Product:
    REQUIRED_ATTRS = ["name", "link", "category"]
    META_ATTRS = [
        "abv_prct",
        "quantity_per_container",
        "container_size_ml",
        "country_of_origin",
        "price_reg",
        "price_sale",
    ]

    def __init__(self, *, name, link, category, **kwargs):
        self.name = name
        self.link = link
        self.category = category
        self.abv_prct = kwargs.get("abv_prct")
        self.quantity_per_container = kwargs.get("quantity_per_container")
        self.container_size_ml = kwargs.get("container_size_ml")
        self.country_of_origin = kwargs.get("country_of_origin")
        self.price_reg = kwargs.get("price_reg")
        self.price_sale = kwargs.get("price_sale")
        self.last_refreshed = None
        self.cached_page = None

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return {k: getattr(self, k) for k in (self.META_ATTRS + self.REQUIRED_ATTRS)}

    def fetch_product_page(self, cache=False):
        resp = requests.get(self.link)
        if resp.status_code == 200:
            if cache:
                self.cached_page = resp.text
            return resp.text

    def fetch_product_soup(self, cache=False):
        return bs4.BeautifulSoup(self.fetch_product_page(cache=cache), "html.parser")

    def refresh_metadata(self, cache=False):
        meta = get_product_attrs(self.fetch_product_soup(cache))
        for key in self.META_ATTRS:
            if meta.get(key):
                setattr(self, key, meta.get(key))
        self.last_refreshed = datetime.datetime.now()

    def __repr__(self):
        return f"<class 'Product(name={self.name}, category={self.category}'>"