def get_product_attrs(soup):
    attrs_raw = {
        a.text.strip(" :"): a.next_sibling.next_sibling.text.strip()
        for a in soup.find_all(class_="attribute-title")
    }

    price_soup = soup.find(class_="price-group")
    if price_soup.small:
        reg_price = price_soup.small.text
        sale_price = price_soup.strong.text
    else:
        reg_price = price_soup.strong.text
        sale_price = None
    
    attrs_raw['reg_price'] = reg_price
    attrs_raw['sale_price'] = sale_price

    return attrs_raw