import scrapy


class SpiderbookSpider(scrapy.Spider):
    name = "spiderbook"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
