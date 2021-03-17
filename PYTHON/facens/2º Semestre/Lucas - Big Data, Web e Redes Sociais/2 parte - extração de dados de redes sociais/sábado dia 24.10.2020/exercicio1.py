import scrapy

class FirstSpider(scrapy.Spider):
    name = 'spiderone' #nome do agente
    start_urls = ['https://lista.mercadolivre.com.br/jogos/'] #url 

    def parse (self, response): 
         yield {'pagina':response.text}