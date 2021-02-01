from setuptools import find_packages, setup

setup(
    name="anbl_scraper",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
)
