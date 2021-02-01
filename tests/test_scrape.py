import bs4


def test_get_soup(sample_page):
    soup = bs4.BeautifulSoup(sample_page, "html.parser")
    assert True
