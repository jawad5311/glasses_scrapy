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
        products = response.xpath("//div[@id='product-lists']/div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        for product in products:
            name = product.xpath(".//div[@class='p-title']/a[1]/text()").get().strip()

            yield {
                'name': name
            }


