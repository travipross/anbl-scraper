from setuptools import find_packages, setup

setup(
    name="anbl_scraper",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "anbl-crawl = anbl_scraper.crawl:main",
            "anbl-scrape = anbl_scraper.scrape:main",
        ]
    },
)
