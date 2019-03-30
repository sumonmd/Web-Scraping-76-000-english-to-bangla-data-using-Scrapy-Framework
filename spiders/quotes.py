# -*- coding: utf-8 -*-
import scrapy
from ..items import DictionaryWord

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://www.english-bangla.com/browse/index/a']
    #def nextCharword(self,response):
    #allchar = response.css('div.a-z>a::attr(href)').extract()
    def parse(self, response):
        allchar = response.css('div.a-z>a::attr(href)').extract()
        for letter in allchar:
            yield scrapy.Request(url=letter, callback=self.Next_parse)


    def Next_parse(self,response):
      urls = response.css("div#cat_page>ul>li>a::attr(href)").getall()
      for url in urls:
            url=response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.parse_details)
         #follow pagination link
      next_page_url = response.css('div.pagination>a[rel=next]::attr(href)').extract_first()
      if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.Next_parse)

    def parse_details(self,response):
        dictionary = DictionaryWord()
        word = response.css('span#speak.word::text').get().strip()
        mean =response.css('span.format1::text').get().replace(u'\ax0',u' ').strip()
        dictionary['word'] = word
        dictionary['mean'] = mean
        yield dictionary

