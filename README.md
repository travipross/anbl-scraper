# ANBL-SCRAPER #
-----------------
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/travipross/anbl-scraper/Python%20Workflow) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/travipross/anbl-scraper) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![GitHub issues](https://img.shields.io/github/issues/travipross/anbl-scraper) 

Tools to crawl ANBL website to build a registry of individual product URLs, and to scrape metadata from each URL, extracting up-to-date information including pricing, volume, and quantity-per-container. 

## Installation
0. (Optional) Create a new virtual environment.
1. Clone this repository.
2. Navigate to top level directory.
3. Run `pip install .` (Optionally with the `-e` flag for development mode)

## Included Tools - CLI Entrypoints
* `anbl-crawl`
    * Uses AJAX POST requests to return pages of product results within certain categories (by default, crawls all products).
    * Saves output to CSV containing columns for `name`, `link`, and `category`.
    * Supported top-level category filters include the following:
        * `beer`
        * `spirits`
        * `wine`
        * `cider_coolers_other`
  
* `anbl-scrape`
    * Reads product links from CSV generated by `anbl-crawl`, and then visits each link to scrape relevant product metadata where possible.
    * Results are output to another CSV in order to preserve the input for later re-use.
    * **NOTE: This tool may make thousands of HTTP requests in short succession. Use sparingly if you don't want to risk getting the attention of ANBL sysadmins.** 

## TODO
* Create combined tool to crawl + scrape with a single CLI entrypoint.
* Use `pandas` library to perform some basic calculations on the scraped metadata (price per unit vol, etc.)
* Implement custom `Product` class throughout library, where relevant, for better consistency.
* Create basic Sphinx documentation
* PyPI?