import scrapy
from pathlib import Path

from scrapy import signals
import time


class HousescrapSpider(scrapy.Spider):
    name = "housescrap"
    allowed_domains = ["www.rumah123.com"]
    #start_urls = ['https://www.rumah123.com/jual/depok/rumah/']

    def __init__(self, *args, **kwargs): 
      super(HousescrapSpider, self).__init__(*args, **kwargs) 

      self.start_urls = [kwargs.get('start_url')] 
    

    def parse(self, response):

        houses = response.css('div.card-featured__middle-section')


        for house in houses:
            relative_url = house.css('a ::attr(href)').get()
            house_url = 'https://www.rumah123.com' + relative_url
            yield response.follow(house_url, callback = self.parse_house_page)

        next_page_url = response.css('li.ui-molecule-paginate__item--next a::attr(href)').get()

        if next_page_url is not None or next_page_url != '':
            yield response.follow(next_page_url, callback=self.parse)
            
    
    def parse_house_page(self, response):


        harga = response.css('div.r123-listing-summary__price span::text').get()
        alamat = response.css('div.r123-listing-summary__header-container-address ::text').get()
        fasilitas = response.css('div.ui-facilities-portal__item ::text').getall()
        spesifikasi = [spec.css('span::text').getall() for spec in response.css('div.listing-specification-v2__item')]
        
        yield {
            'harga' : harga,
            'alamat' : alamat,
            'fasilitas' : fasilitas,
            'spesifikasi' : spesifikasi
        }