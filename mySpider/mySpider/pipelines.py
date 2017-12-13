# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def __init__(self):
        self.file = open("teacher.json","wb")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(content.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.file.close()