# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class HelloscrapyPipeline:
    def __init__(self): # metodo que é chamado quando a classe é instanciada
        self.mongoclient = MongoClient('localhost', 27017)
    
    def process_item(self, item, spider):
        self.store_nosqldb(item)
        return item

    def store_nosqldb(self, item):
        documento1 = {
                      "title": item['title'][0],
                      "author":item['author'][0],
                      "tag":item['tag'][0]
                     }

        db.nomes.insert(documento1)
