import scrapy

class FirstSpider(scrapy.Spider):
    #não pode alterar o nome das 2 variáveis abaixo
    name = 'spiderone'
    start_urls = [
        'https://games.mercadolivre.com.br/games/'
    ]
    
    def parse(self, response):
        all_div_quotes = response.css("h2::text").extract()

        for item in all_div_quotes:
            
            title = item

            yield{'nome':title}            
            