# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd


class Week0102Pipeline:
    def process_item(self, item, spider):
        # movie = {'href': item['href'], 'title': item['title'], 'actors': item['actors'], 'show_time': item['show_time']}
        movie = [(item['href'], item['title'], item['actors'], item['show_time'])]

        df = pd.DataFrame(data=movie)
        df.to_csv('./week01_02.csv', mode='a', encoding='utf8', index=False, header=False)
        return item
