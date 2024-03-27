# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bookscrapper3Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

# def sell(value):
#     return value * 10000



# class Bookitem(scrapy.item):
#     url = scrapy.Field()
#     name = scrapy.Field()
#     price = scrapy.Field()
#     stock = scrapy.Field()        # Running sell function 
#     product_description = scrapy.Field()
