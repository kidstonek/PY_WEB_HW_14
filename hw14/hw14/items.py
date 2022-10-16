# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hw14Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    keywords = scrapy.Field()

    author_name = scrapy.Field()
    author_born_date = scrapy.Field()
    author_description = scrapy.Field()

