from anbl_scraper.utils.scrape_utils import get_product_attrs


def test_attrs_extract(sample_soup):
    attrs = get_product_attrs(sample_soup)

    assert attrs["abv_prct"] == 5.0
    assert attrs["quantity_per_container"] == 12
    assert attrs["container_size_ml"] == 341
    assert attrs["country_of_origin"] == "Canada"
    assert attrs["price_reg"] == 25.49