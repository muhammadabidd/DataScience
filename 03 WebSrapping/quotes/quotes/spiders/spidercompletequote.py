import scrapy


class SpidercompletequoteSpider(scrapy.Spider):
    name = "spidercompletequote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        quotes = response.css(".quote")
        
        for quote in quotes:
            # tags = quote.css(".tags")
            
            # yield {
            #     'quotes' : quote.css(".text::text").get(),
            #     'author' : quote.css(".author::text").get(),
            #     'tag' : tags.css(".tag::text").extract()
            # }

            relative_url = quote.xpath("span[2]/a/@href").get()

            quote_url = 'https://quotes.toscrape.com' +  relative_url

            yield response.follow(quote_url, callback = self.parse_page)

        
        nextpage = response.css(".pager .next a::attr(href)").get()

        nexpageurl = 'https://quotes.toscrape.com/' +  nextpage

        yield response.follow(nexpageurl, callback = self.parse)



    def parse_page(self, response):


        yield {
            "author_name" : response.css(".author-title::text").get(),
            "author_born_date" : response.css(".author-born-date::text").get(),
            "author_born_place" : response.css(".author-born-location::text").get(),
            "author_description" : response.css(".author-description::text").get().strip()
        }

        
