import scrapy


class BookstoscrapeSpider(scrapy.Spider):
    name = "bookstoscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        products= response.xpath('//article[@class="product_pod"]')
        for product in products:
            img_url=img_url=response.urljoin(product.xpath('.//div[@class="image_container"]/a/img/@src').get())
            book_name=product.xpath('.//h3/a/text()').get()
            book_price=product.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').get()
            book_stoke=product.xpath('.//div[@class="product_price"]/p[@class="instock availability"]/text()[2]').get().strip()
          
        yield{
            'img_ur':img_url,
            'book_name':book_name,
            'book_price':book_price,
            'book_stoke':book_stoke,

        }
        next_page =response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
