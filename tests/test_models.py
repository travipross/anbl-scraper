from anbl_scraper.models import Product

def test_create_product_from_dict(sample_product_list, sample_product):
    prod = Product.from_dict(sample_product_list[0]) 
    
    assert vars(prod) == vars(sample_product)
