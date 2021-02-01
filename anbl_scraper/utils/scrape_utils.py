def get_product_attrs(soup):
    attrs_raw = {
        a.text.strip(" :"): a.next_sibling.next_sibling.text.strip()
        for a in soup.find_all(class_="attribute-title")
    }
    return attrs_raw