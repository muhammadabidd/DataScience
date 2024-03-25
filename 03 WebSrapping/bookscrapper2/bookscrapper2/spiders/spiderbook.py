import scrapy


class SpiderbookSpider(scrapy.Spider):
    name = "spiderbook"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:

            relative_url = book.css("h3 a::attr(href)").get()

            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' +  relative_url
            else : 
                book_url = 'https://books.toscrape.com/catalogue/' +  relative_url
            yield response.follow(book_url, callback = self.parse_bookpage)

        
        nextpage = response.css('li.next a ::attr(href)').get()
        if nextpage is not None :
            if 'catalogue/' in nextpage:
                nexpageurl = 'https://books.toscrape.com/' +  nextpage
            else : 
                nexpageurl = 'https://books.toscrape.com/catalogue/' +  nextpage
            yield response.follow(nexpageurl, callback = self.parse)


    def parse_bookpage(self, response):

        yield {
            'url' : response.url ,
            'name' :  response.css(".product_main h1::text").get() ,
            'price' : response.css(".product_main .price_color::text").get() ,
            'stock' : response.css(".product_main .instock ::text").extract()[1].split()[2].replace("(", "") ,
            'product_description' : response.xpath("//div[@id='product_description']//following-sibling::p//text()").get()
        }
        

