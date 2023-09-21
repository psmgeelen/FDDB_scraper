# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class FddbItem(Item):
    name_food = Field()
    name_param = Field()
    value_param = Field()
    unit_param = Field()
