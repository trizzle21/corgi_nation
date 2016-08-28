import scrapy
import pillow

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = []
    start_urls = [

    ]

    def parse(self, response):
	
