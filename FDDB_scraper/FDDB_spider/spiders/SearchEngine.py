import scrapy
from ..items import FddbItem


class SearchEngine(scrapy.Spider):
    name = "searchengine"
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    start_urls = [
        f"https://fddb.mobi/search/?lang=de&cat=mobile-de&search={letter}"
        for letter in alphabet
    ]

    def parse(self, response, **kwargs):
        items = response.css("table")

        # Tables are being used to present Food items
        for item in items:
            name = item.css("b::text").get()
            link = item.css("a::attr(href)").get()
            url_food_item = f"https://fddb.mobi{link}"
            # Pick up the details of the food
            yield scrapy.Request(url=url_food_item, callback=self.get_food_details)

        # This section produces the next page of items from the search
        next_button = response.xpath("body/div/div/div/div/div/a/@href").get()

        if next_button:
            next_page = f"http://{next_button[2:]}"
            yield scrapy.Request(url=next_page)

    def get_food_details(self, response):
        name_food = response.css("h3::text").get()
        tables = response.css("table")
        for table in tables:
            for row in table.css("tr"):
                if len(row.xpath("td")) == 2:
                    if row.xpath("td[2]/text()").get() is not None:
                        result = FddbItem()
                        result["name_food"] = name_food
                        result["name_param"] = row.xpath("td[1]/span/text()").get()
                        result["value_param"], result["unit_param"] = (
                            row.xpath("td[2]/text()").get().split(" ")
                        )
                        yield result
