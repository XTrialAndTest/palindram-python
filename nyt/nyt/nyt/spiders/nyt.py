import scrapy

list=[]
class NytSpider(scrapy.Spider):
    name = "nyt"
    allowed_domains = ["nytimes.com"]
    start_urls = ["https://www.nytimes.com/international/"]

    def parse(self, response):
        allheading=response.css('section.story-wrapper>a::attr("href")')
        for i in allheading:
           
            yield scrapy.Request(url=i.get(),callback=self.singleHeading)

    def singleHeading(self, response):
        
        main_heading=response.css('div.ehdk2mb0>h1.css-1l8buln::text').get()
        sumarry=response.css('p#article-summary::text').get()
        author=response.css('a.e1jsehar0::text').get()
        if sumarry is not None:
            theData={
            'Heading':f"{main_heading}",
            'summary':f"{sumarry}",
            'author':f"{author}",
            

        }
            yield theData

