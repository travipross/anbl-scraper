# ANBL-SCRAPER #
Crawls ANBL website to build a registry of individual product links,  and then visits each link to extract up-to-date information including pricing, volume, and quantity-per-container. 

## DEPRECIATED - OLD README ##
Using JSON formatted product list with URLs, visits each page and collects data about products in order to determine highest ABV per dollar

anbl_scraper.py - visits urls specified in a JSON file, then repopulates JSON object with product attributes and writes to disk. Runs in parallel with a default of 20 web scraper workers.

anbl_converter.py - Converts JSON file from output of anbl_scraper.py to CSV format for easier manipulation with Excel (or equivalent spreadsheet software)

