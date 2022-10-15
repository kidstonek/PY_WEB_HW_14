import scrapy


class Hw14autSpider(scrapy.Spider):
    name = 'hw14aut'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print(response.xpath("/html//span/a/@href").get())
        for quote in response.xpath("/html//div[@class='quote']"):
            # q = quote.xpath("div[@class='author']/a/text()").extract()
            # q = quote.xpath("/html//span/a/@href").get()
            # print(q)
            yield {
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get(),
                "link": quote.xpath("span/a/@href").get()
            }
