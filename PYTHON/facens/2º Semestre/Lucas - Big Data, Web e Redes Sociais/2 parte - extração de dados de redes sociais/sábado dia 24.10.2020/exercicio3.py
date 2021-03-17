import scrapy
from ..items import HelloscrapyItem

class FirstSpider(scrapy.Spider):
    #não pode alterar o nome das 2 variáveis abaixo
    name = 'spiderone'
    start_urls = [
        'https://games.mercadolivre.com.br/games/'
    ]
    
    def parse(self, response):
        #criar instancia do HelloscrapyItem
        items = HelloscrapyItem()
        
        items['nomes'] = response.css("h2::text").extract()

        yield items
           
        