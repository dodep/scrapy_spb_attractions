import json
import scrapy

class AttractionsSpyder(scrapy.Spider):
    name = 'att'
    
    URI_1 = 'https://tonkosti.ru/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80'
    URI_2 = 'https://www.spb-guide.ru/'
    URI_3 = 'http://opeterburge.ru/sight/botanicheskij-sad-2.html'

    start_urls = [URI_1, URI_2, URI_3]
    
    data = []
    
    def parse(self, response):
        if response.url == self.URI_1:
            self.parse_01(response)
        if response.url == self.URI_2:
            self.parse_02(response)    
        if response.url == self.URI_3:
            self.parse_03(response)
        
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

        yield None
        
    def parse_01(self, response):
        title = response.css('h1::text').extract_first()
        text = response.css('p::text').extract_first()
        img = response.css('.scrolling-gallery__photo img::attr(src)').extract_first()
        data = {
                "title": title,
                "text": text,
                "img": img
            }
        self.data.append(data)
        
    def parse_02(self, response):
        title = response.css('.index23:nth-child(1) h2::text').extract_first()
        text = response.css('.index23:nth-child(1) .dim1::text').extract_first()
        img = response.css('.index23:nth-child(1) .indeximg25::attr(src)').extract_first()
        data = {
                "title": title,
                "text": text,
                "img": self.URI_2 + img
            }
        self.data.append(data)
    
    def parse_03(self, response):
        title = response.css('.title::text').extract_first()
        text = response.css('p:nth-child(2)::text').extract_first()
        img = response.css('p:nth-child(3) img::attr(src)').extract_first()
        data = {
                "title": title,
                "text": text,
                "img": 'http://opeterburge.ru' + img
            }
        self.data.append(data)