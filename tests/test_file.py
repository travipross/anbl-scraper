import os
from anbl_scraper.utils.csv_utils import read_product_link_csv, write_product_link_csv


def test_reader(sample_product_list, test_resources_path):
    product_list = read_product_link_csv(
        os.path.join(test_resources_path, "sample_products.csv")
    )

    assert product_list == sample_product_list


def test_writer(tmp_path, sample_product_list):
    filename = os.path.join(tmp_path, "test_file.csv")
    write_product_link_csv(filename, sample_product_list)
    prods = read_product_link_csv(filename)

    assert prods == sample_product_list
