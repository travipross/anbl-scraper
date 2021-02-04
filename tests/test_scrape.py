from anbl_scraper.utils.scrape_utils import (
    get_product_attrs,
    parse_abv,
    parse_int,
    parse_price,
    parse_vol,
)
import pytest


def test_attrs_extract(sample_soup):
    attrs = get_product_attrs(sample_soup)

    assert attrs["abv_prct"] == 5.0
    assert attrs["quantity_per_container"] == 12
    assert attrs["container_size_ml"] == 341
    assert attrs["country_of_origin"] == "Canada"
    assert attrs["price_reg"] == 25.49


@pytest.mark.parametrize(
    "in_val,out_val", [("1.23", 1.23), ("5 %", 5.0), ("  6.9 %", 6.9), (None, None)]
)
def test_parse_abv(in_val, out_val):
    assert out_val == parse_abv(in_val)


@pytest.mark.parametrize("in_val,out_val", [("1", 1), ("2", 2), (None, None)])
def test_parse_int(in_val, out_val):
    assert out_val == parse_int(in_val)


@pytest.mark.parametrize(
    "in_val,out_val",
    [("$1234", 1234.0), ("$ 49.99", 49.99), ("$ 29,999", 29999.0), (None, None)],
)
def test_parse_price(in_val, out_val):
    assert out_val == parse_price(in_val)


@pytest.mark.parametrize(
    "in_val,out_val",
    [("355 mL", 355), ("1140", 1140), (None, None)],
)
def test_parse_vol(in_val, out_val):
    assert out_val == parse_vol(in_val)