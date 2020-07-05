# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
from scrapy.exceptions import NotConfigured
import pymysql


class Week0201Pipeline:

    def process_item(self, item, spider):
        movie = [(item['href'], item['title'], item['actors'], item['show_time'])]

        df = pd.DataFrame(data=movie)
        df.to_csv('week02_01.csv', mode='a', encoding='utf8', index=False, header=False)
        print('to_csv')
        return item


# 自定义pipeline类内的函数执行顺序
# 1. from_crawler 2.__init__ 3.open_spider 4.process_item(循环执行) 5. close_spider
# 1、2、3、5 只会执行一次
class MySQLPipeline:
    def __init__(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    # If present, this classmethod is called to create a pipeline instance from a Crawler.
    # It must return a new instance of the pipeline.
    # Crawler object provides access to all Scrapy core components like settings and signals;
    # it is a way for pipeline to access them and hook its functionality into Scrapy.
    # 从setting.py读取MySQL链接信息
    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('MYSQL_CONFIG'):
            raise NotConfigured

        db_config = crawler.settings.get('MYSQL_CONFIG')

        return cls(
            host=db_config.get('host'),
            port=db_config.get('port'),
            user=db_config.get('user'),
            password=db_config.get('password'),
            database=db_config.get('database'),
            charset=db_config.get('charset')
        )

    # This method is called when the spider is opened.
    def open_spider(self, spider):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        port=self.port,
                                        user=self.user,
                                        password=self.password,
                                        database=self.database,
                                        charset=self.charset
                                        )
        except Exception as e:
            print(f"ERROR 链接mysql失败；{e}")

    # This method is called when the spider is closed.
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        try:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO t_movie_info (href, title, actors, show_time) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (item['href'], item['title'], item['actors'], item['show_time']))
                # cursor.executemany(sql, items)
            self.conn.commit()
        except Exception as e:
            print(f"ERROR: {e}")
        return item
