# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from week01_02.items import Week0102Item

# 作业二：
#
# 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，
# 并以 UTF-8 字符集保存到 csv 格式的文件中。

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['m.maoyan.com']
    start_urls = ['http://m.maoyan.com/']

    def start_requests(self):
        url = 'https://m.maoyan.com/#movie/classic'
        # url = 'https://m.maoyan.com/ajax/moreClassicList?sortId=1&showType=3&limit=10&offset=0'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        movies = Selector(response=response).xpath('//div[@class="classic-movies-list"]/a')

        for m in movies[0:10]:
            href = m.xpath('./@href')
            title = m.xpath('./div/div/div[@class="title line-ellipsis"]/text()')
            actors = m.xpath('./div/div/div[@class="actors line-ellipsis"]/text()')
            show_time = m.xpath('./div/div/div[@class="show-info line-ellipsis"]/text()')

            item = Week0102Item()
            item['href'] = 'https://m.maoyan.com' + href.extract_first().strip()
            item['title'] = title.extract_first().strip()
            item['actors'] = actors.extract_first().strip()
            item['show_time'] = show_time.extract_first().strip()[0:10]

            yield item


