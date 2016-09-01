import scrapy
import pillow

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.google.com"]
    start_urls = [
    	"https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1284&bih=625&q=corgi+puppies&oq=corgi&gs_l=img.1.1.0l10.2660.3340.0.4569.5.4.0.1.1.0.58.210.4.4.0....0...1ac.1.64.img..0.5.211.ye4ueTSq_iY#tbm=isch&q=corgi"
    ]

    def parse(self, response):
	
