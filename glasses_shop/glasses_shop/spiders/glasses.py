import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']

    def start_requests(self):
        yield scrapy.Request(
            url='http://www.glassesshop.com/bestsellers',
            callback=self.parse,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            })

    def parse(self, response):
        pass
