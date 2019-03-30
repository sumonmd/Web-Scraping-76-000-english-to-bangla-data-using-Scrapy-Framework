import scrapy


class DictionarySpider(scrapy.Spider):
    name = "dictionary"
    s_urls=['http://www.english-bangla.com/browse/index/a']
    def parse(self,response):
        urls=response.css("div#cat_page>ul>li>a::attr(href)").getall()
        for url in urls:
                yield{
                    'link':url
                }
