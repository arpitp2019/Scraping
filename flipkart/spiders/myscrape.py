# -*- coding: utf-8 -*-
#this is 
import scrapy
from scrapy import Spider
from scrapy.http import Request


class MyscrapeSpider(scrapy.Spider):
    name = 'myscrape'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=muscleblaze+whey+protein']
    
    
    def parse(self, response):
        productlink= response.xpath('//*[@class="_2rpwqI"]/@href').extract()
        for i in productlink:
            absolute_url=response.urljoin(i)
            yield Request(absolute_url,callback=self.parse_book)
            
        next_page_url=response.xpath('//*[@class="_1LKTO3"]/@href').extract_first() 
        absolute_next_page=response.urljoin(next_page_url)
        yield Request(absolute_next_page)
           
            
    def parse_book(self,response):
        name=response.xpath('//*[@class="B_NuCI"]/text()').extract_first()
        price=response.xpath('//*[@class="_30jeq3 _16Jk6d"]/text()').extract_first()
        picture_url=response.xpath('//*[@class="CXW8mj _3nMexc"]/img/@src').extract_first()
        yield{
            "Name":name,
            "Price":price,
            "Picture url":picture_url,
            "product url":response.url
        }
        