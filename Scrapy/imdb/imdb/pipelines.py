# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

class IMDBPipeline(object):
    
    # @classmethod
    # def from_crawler(cls,crawler):
    #     logging.warning(crawler.settings.get('MYSQL_URL'))

    # def open_spider(self,spider):
    #     logging.warning("Spider opened from pipeline")

    # def close_spider(self,spider):
    #     logging.warning("Spider closed from pipeline")

    def process_item(self, item, spider):
        return item
