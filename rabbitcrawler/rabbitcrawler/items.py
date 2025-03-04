# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RabbitcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Reddit(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    depth = scrapy.Field()

class Youtube(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    depth = scrapy.Field()

class Wiki(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    depth = scrapy.Field()