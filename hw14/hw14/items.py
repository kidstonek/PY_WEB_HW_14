# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from datetime import datetime

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_quotes(text):
    text = text.strip(u'\u201c'u'\u201d')
    return text


def remove_quotes(text):
    # strip the unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text


def convert_date(text):
    return datetime.strptime(text, '%B %d, %Y')


def parse_location(text):
    return text[3:]


class Hw14Item(scrapy.Item):
    # define the fields for your item here like:
    quote_content = scrapy.Field(
        input_processor=MapCompose(remove_quotes),
        # TakeFirst return the first value not the whole list
        output_processor=TakeFirst()
    )
    author_name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    author_birthday = scrapy.Field(
        input_processor=MapCompose(convert_date),
        output_processor=TakeFirst()
    )
    author_bornlocation = scrapy.Field(input_processor=MapCompose(parse_location), output_processor=TakeFirst()
                                       )
    author_bio = scrapy.Field(input_processor=MapCompose(str.strip),
                              output_processor=TakeFirst()
                              )
    tags = scrapy.Field()
    quote_content = scrapy.Field(input_processor=MapCompose(remove_quotes))
    text = scrapy.Field()
    author = scrapy.Field()
