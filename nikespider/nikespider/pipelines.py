# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NikespiderPipeline:

    def __init__(self):
        self.items = []


    def open_spider(self, spider):
        # 初始化空列表
        self.items = []


    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        with open('nike.json', 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)
