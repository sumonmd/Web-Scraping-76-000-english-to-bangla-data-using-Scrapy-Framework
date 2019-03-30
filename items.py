# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DictionaryWord(scrapy.Item):
    # define the fields for your item here like:
    word = scrapy.Field()
    mean = scrapy.Field()

    pass
