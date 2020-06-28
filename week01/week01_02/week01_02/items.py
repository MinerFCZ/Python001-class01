# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Week0102Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    href = scrapy.Field()
    title = scrapy.Field()
    actors = scrapy.Field()
    show_time = scrapy.Field()
