import scrapy


class JijiScrapedSpider(scrapy.Spider):
    name = "jiji_scraped"
    allowed_domains = ["jiji.co.ke"]
    start_urls = ["https://jiji.co.ke/"]

    def parse(self, response):
        all_cars=response.css("div.b-trending-card>a::attr('href')")
        for i in all_cars:

            print(i.get())
