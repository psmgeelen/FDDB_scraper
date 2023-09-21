# FDDB Scraper
This is an FDDB scraper to scrape nutritional data from the FDDB website: https://fddb.mobi/ 
The scraper works as follows:
- It searches on a single letter of the alphabet
- It gets all items of the page
- It goes into every item to get the details of each item
- It leverages pagination to get all items of a single letter in the alphabet
- It moves on to the next letter of the alphabet

This approach means that it very thorough, but also produces a large amount of duplicates. Deplucitating the data with e.g. pandas is essential.
