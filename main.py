import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://muhammadabidd.github.io/portfolio/']

    def parse(self, response):
        # Extract data using CSS selectors
        title = response.css('title::text').get()
        paragraphs = response.css('p::text').getall()

        # Extract data using XPath selectors
        links = response.xpath('//a/@href').getall()

        # Yield the extracted data
        yield {
            'title': title,
            'paragraphs': paragraphs,
            'links': links
        }

