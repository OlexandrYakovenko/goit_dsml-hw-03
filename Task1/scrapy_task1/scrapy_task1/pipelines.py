# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyTask1Pipeline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if 'fullname' in adapter.keys():
            self.authors.append(dict(adapter))
        elif 'quote' in adapter.keys():
            self.quotes.append(dict(adapter))
        else:
            raise Exception('Something went wrong.')

    def close_spider(self, spider):
        with open('quotes.json', 'w', encoding='utf-8') as f:
            json.dump(self.quotes, f, ensure_ascii=False, indent=4)
        with open('authors.json', 'w', encoding='utf-8') as f:
            json.dump(self.authors, f, ensure_ascii=False, indent=4)
