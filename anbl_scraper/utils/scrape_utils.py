def parse_price(raw_price):
    return float(raw_price.lstrip("$").strip()) if raw_price is not None else None


def parse_abv(raw_abv):
    return float(raw_abv.rstrip("%").strip()) if raw_abv is not None else None


def parse_int(raw_int):
    return int(raw_int) if raw_int is not None else None


def parse_vol(raw_ml):
    return int(raw_ml.rstrip("mL")) if raw_ml is not None else None


def get_product_attrs(soup):
    # Parse from attribute box
    attrs_raw = {
        a.text.strip(" :"): a.next_sibling.next_sibling.text.strip()
        for a in soup.find_all(class_="attribute-title")
    }
    attrs_raw["abv_prct"] = parse_abv(attrs_raw.pop("Alcohol content"))
    attrs_raw["quantity_per_container"] = parse_int(
        attrs_raw.pop("Quantity per container")
    )
    attrs_raw["container_size_ml"] = parse_vol(attrs_raw.pop("Container Size"))
    attrs_raw["country_of_origin"] = attrs_raw.pop("Country of origin")

    # Parse from price box
    price_soup = soup.find(class_="price-group")
    if price_soup.small:
        price_reg = price_soup.small.text
        price_sale = price_soup.strong.text
    else:
        price_reg = price_soup.strong.text
        price_sale = None

    attrs_raw["price_reg"] = parse_price(price_reg)
    attrs_raw["price_sale"] = parse_price(price_sale)

    return attrs_raw