import scrapy


class Myspider1Spider(scrapy.Spider):
    name = "myspider1"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
