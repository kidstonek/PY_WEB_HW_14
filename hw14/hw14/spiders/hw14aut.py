import scrapy
from ..items import Hw14Item

items = Hw14Item()
class Hw14autSpider(scrapy.Spider):
    name = 'hw14aut'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for quote in response.xpath("/html//div[@class='quote']"):
            title = quote.xpath("span[@class='text']/text()").extract()
            author = quote.xpath("span/small/text()").extract()
            keywords = quote.xpath("div[@class='tags']/a/text()").extract()

            items['title'] = title
            items['author'] = author
            items['keywords'] = keywords

            yield items
            author_url = quote.xpath("span/a/@href").get()
            yield response.follow(author_url, callback=self.parse_additional)

            next_link = response.xpath("//li[@class='next']/a/@href").get()
            if next_link:
                yield scrapy.Request(url=self.start_urls[0] + next_link)
    def parse_additional(self, response):
        author_name = response.xpath("/html//div/h3[@class='author-title']/text()").extract()
        author_born_date = response.xpath("/html//span[@class='author-born-date']/text()").get()
        author_description = response.xpath("/html//div[@class='author-description']/text()").get()

        items['author_name'] = author_name
        items['author_born_date'] = author_born_date
        items['author_description'] = author_description
        yield items
