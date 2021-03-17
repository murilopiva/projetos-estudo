import scrapy
from ..items import HelloscrapyItem

class FirstSpider(scrapy.Spider):
    #não pode alterar o nome das 2 variáveis abaixo
    name = 'spiderone'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        #criar instancia do HelloscrapyItem
        items = HelloscrapyItem()
        
        all_div_quotes = response.css("div.quote")
        
        for item in all_div_quotes:
            
            title = item.css('span.text::text').extract()
            author = item.css('.author::text').extract()
            tag = item.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items     
        