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
            price = product.xpath(".//div[@class='p-price']/div[1]/span/text()").get()
            link_product = product.xpath(".//div[@class='product-img-outer']/a[1]/@href").get()
            link_img = product.xpath(".//div[@class='product-img-outer']/a[1]/img[1]/@data-src").get()

            yield {
                'link': link_product,
                'name': name,
                'price': price,
                'image': link_img
            }

        next_page = response.xpath("//ul[@class='pagination']/li[6]/a[@class='page-link']/")


