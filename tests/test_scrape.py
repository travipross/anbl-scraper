from anbl_scraper.utils.scrape_utils import get_product_attrs


def test_attrs_extract(sample_soup):
    raw_attrs = get_product_attrs(sample_soup)

    assert raw_attrs["Alcohol content"] == "5.0%"
    assert raw_attrs["Quantity per container"] == "12"
    assert raw_attrs["Container Size"] == "341 mL"
    assert raw_attrs["Country of origin"] == "Canada"
    assert raw_attrs["reg_price"] == "$25.49"