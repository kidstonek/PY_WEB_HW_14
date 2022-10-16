import scrapy
from scrapy.loader import ItemLoader

from ..items import Hw14Item


class Hw14autSpider(scrapy.Spider):
    items = Hw14Item()
    name = 'hw14aut'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for quote in response.xpath("/html//div[@class='quote']"):
            loader = ItemLoader(item=Hw14Item(), selector=quote)
            text = quote.xpath("span[@class='text']/text()").extract()
            author = quote.xpath("span/small/text()").extract()
            tags = quote.xpath("div[@class='tags']/a/text()").extract()
            loader.add_css('quote_content', '.text::text')

            self.items['text'] = text
            self.items['author'] = author
            self.items['tags'] = tags
            # self.items['quote_content'] = quote_content

            yield self.items
            author_url = quote.xpath("span/a/@href").get()
            yield response.follow(author_url, callback=self.parse_additional)

            next_link = response.xpath("//li[@class='next']/a/@href").get()
            if next_link:
                yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_additional(self, response):
        author_name = response.xpath("/html//div/h3[@class='author-title']/text()").extract()
        author_birthday = response.xpath("/html//span[@class='author-born-date']/text()").get()
        author_bornlocation = response.css('.author-born-location::text').get(),
        author_bio = response.xpath("/html//div[@class='author-description']/text()").get()

        self.items['author_name'] = author_name
        self.items['author_birthday'] = author_birthday
        self.items['author_bornlocation'] = author_bornlocation
        self.items['author_bio'] = author_bio
        yield self.items
