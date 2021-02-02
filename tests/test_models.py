from anbl_scraper.models import Product


def test_product_from_dict(sample_product_list, sample_product):
    prod = Product.from_dict(sample_product_list[0])

    assert vars(prod) == vars(sample_product)


def test_product_to_dict(sample_product):
    d = sample_product.to_dict()
    p = Product.from_dict(d)
    assert vars(p) == vars(sample_product)
