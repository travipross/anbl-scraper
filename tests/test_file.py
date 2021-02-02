import os
import csv
from anbl_scraper.utils.csv_utils import read_product_link_csv

def test_reader(sample_product_list, test_resources_path):
    product_list = read_product_link_csv(os.path.join(test_resources_path, "sample_products.csv"))

    assert product_list == sample_product_list