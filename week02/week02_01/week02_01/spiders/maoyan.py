# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from week02_01.items import Week0201Item

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['m.maoyan.com']
    start_urls = ['http://m.maoyan.com/']

    def start_requests(self):
        url = 'https://m.maoyan.com/#movie/classic'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="classic-movies-list"]/a')

        for m in movies[0:10]:
            href = m.xpath('./@href')
            title = m.xpath('./div/div/div[@class="title line-ellipsis"]/text()')
            actors = m.xpath('./div/div/div[@class="actors line-ellipsis"]/text()')
            show_time = m.xpath('./div/div/div[@class="show-info line-ellipsis"]/text()')

            item = Week0201Item()
            item['href'] = 'https://m.maoyan.com' + href.extract_first().strip()
            item['title'] = title.extract_first().strip()
            item['actors'] = actors.extract_first().strip()
            item['show_time'] = show_time.extract_first().strip()[0:10]

            yield item
