import scrapy


class SpidercompletequoteSpider(scrapy.Spider):
    name = "spidercompletequote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        quotes = response.css(".quote")
        
        for quote in quotes:
            tags = quote.css(".tags")
            
            yield {
                'quotes' : quote.css(".text::text").get(),
                'author' : quote.css(".author::text").get(),
                'tag' : tags.css(".tag::text").extract()
            }
        
        nextpage = response.css(".pager .next a::attr(href)").get()

        nexpageurl = 'https://quotes.toscrape.com/' +  nextpage

        yield response.follow(nexpageurl, callback = self.parse)
