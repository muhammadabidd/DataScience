import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            yield {
                'name' : book.css('h3 a::text').get(),
                'price' : book.css('.product_price .price_color::text').get(),
                'url' : book.css('h3 a').attrib['href']
            }

        nextpage = response.css("li.next a::attr(href)").get()

        if nextpage is not None :
            if 'catalogue/' in nextpage:
                nexpageurl = 'https://books.toscrape.com/' +  nextpage
            else : 
                nexpageurl = 'https://books.toscrape.com/catalogue/' +  nextpage
            yield response.follow(nexpageurl, callback = self.parse)
