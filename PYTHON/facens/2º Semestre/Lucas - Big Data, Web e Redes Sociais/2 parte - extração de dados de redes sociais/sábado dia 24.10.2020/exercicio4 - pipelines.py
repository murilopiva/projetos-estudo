# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import json

class HelloscrapyPipeline:
    def __init__(self): # metodo que é chamado quando a classe é instanciada
        self.mongoclient = MongoClient('localhost', 27017)
             
    
    def process_item(self, item, spider):
        self.store_nosqldb(item)
        return item

    def store_nosqldb(self, item):
        nomes = item['nomes']
        
        for i in nomes:
            documento1 = (
                            { 
                                "nomes":i
                          }
                         )

            db = self.mongoclient.dbmongo  
            db.nomes.insert_one(documento1).inserted_id
