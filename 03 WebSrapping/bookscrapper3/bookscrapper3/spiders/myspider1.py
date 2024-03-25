import scrapy
from bookscrapper3.items import Bookitem

class Myspider1Spider(scrapy.Spider):
    name = "myspider1"
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

        book_item = Bookitem()


        book_item['url'] = response.url ,
        book_item['name'] =  response.css(".product_main h1::text").get() ,
        book_item['price'] = response.css(".product_main .price_color::text").get() ,
        book_item['stock'] = response.css(".product_main .instock ::text").extract()[1].split()[2].replace("(", "") ,
        book_item['product_description'] = response.xpath("//div[@id='product_description']//following-sibling::p//text()").get()


        yield Bookitem
