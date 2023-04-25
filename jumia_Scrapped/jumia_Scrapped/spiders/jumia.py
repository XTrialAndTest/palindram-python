import scrapy
n=0
listN=[]

class JumiaSpider(scrapy.Spider):
    name = "jumia"
    # allowed_domains = ["https://www.jumia.co.ke/home-office-appliances/"]
    start_urls = ["https://www.jumia.co.ke/home-cooking-appliance-accessories/"]

    def parse(self, response):
       
        links=response.css("#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div.-paxs.row._no-g._4cl-3cm-shs> article.prd._fb.col.c-prd>a::attr('href') ").getall()
        for link in links:
            # print(link)
            # response.follow(link,callback=self.parseInnerPage(response))
            yield scrapy.Request(url=response.urljoin(link),callback=self.parseInnerPage)
        # nextPage=response.css("#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div.pg-w.-ptm.-pbxl > a").getall()
        nextpage=response.css('#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div.pg-w.-ptm.-pbxl > a:nth-child(6)::attr("href")').get()
        
        if nextpage is not None:
            # response.follow(nextpage.get(),callback=self.parse)
            yield scrapy.Request(url=response.urljoin(nextpage),callback=self.parse)
            # print(nextpage,'nextpage to scrape ==============================================>')
       
        
        
    def parseInnerPage(self,response):
        product_name=response.css("#jm > main > div:nth-child(1) > section > div > div.col10 > div.-df.-j-bet > div > h1::text").get()
        price=response.css('#jm > main > div:nth-child(1) > section > div > div.col10 > div.-phs > div.-hr.-mtxs.-pvs > div > span::text').get()
        brand=response.css("#jm > main > div:nth-child(1) > section > div > div.col10 > div.-phs > div:nth-child(1) > a:nth-child(1)::text").get()
        if response.css("#jm > main > div:nth-child(1) > section > div > div.col10 > div.-phs > div.-hr.-mtxs.-pvs > div > div > span.bdg._dsct._dyn.-mls::text").get() is  None:
            discount=f"0%"
        else:   
            discount=response.css("#jm > main > div:nth-child(1) > section > div > div.col10 > div.-phs > div.-hr.-mtxs.-pvs > div > div > span.bdg._dsct._dyn.-mls::text").get()
        
        no_of_ratings =response.css("#jm > main > div:nth-child(1) > section > div > div.col10 > div.-phs > div.-df.-i-ctr.-pvxs > a::text").get()
        desc=''
        descList=[response.css('#jm > main > div:nth-child(2) > div.col12 > div.card.aim.-mtm > div.markup.-mhm.-pvl.-oxa.-sc::text').getall(),response.css('#jm > main > div:nth-child(2) > div.col12 > div.card.aim.-mtm > div.markup.-mhm.-pvl.-oxa.-sc>ul>li::text').getall(),response.css('#jm > main > div:nth-child(2) > div.col12 > div.card.aim.-mtm > div.markup.-mhm.-pvl.-oxa.-sc>p::text').getall()]
        for i in descList:
            if len(i)>0:
                desc=i
        key_features=''
        keyfeaturesList=[response.css('#jm > main > div:nth-child(2) > div.col12 > section.card.aim.-mtm.-fs16 > div.row.-pas > article:nth-child(1) > div > div>ul>li::text').getall(),response.css('#jm > main > div:nth-child(2) > div.col12 > section.card.aim.-mtm.-fs16 > div.row.-pas > article:nth-child(1) > div > div>ul>li>b::text').getall()]
        for i in keyfeaturesList:
            if len(i)>0:
                key_features=i
        in_box=''
        in_box_list=[response.css('#jm > main > div:nth-child(2) > div.col12 > section.card.aim.-mtm.-fs16 > div.row.-pas > article:nth-child(2) > div > div::text').getall(),response.css('#jm > main > div:nth-child(2) > div.col12 > section.card.aim.-mtm.-fs16 > div.row.-pas > article:nth-child(2) > div > div>ul>li::text').getall()]

        for i in in_box_list:
            if len(i)>0:
                in_box=i
        specification_key=response.css('#jm > main > div:nth-child(2) > div.col12 > section.card.aim.-mtm.-fs16 > div.row.-pas > article:nth-child(3) > div > ul > li>span::text').getall()
        specification_value=response.css('#jm > main > div:nth-child(2) > div.col12 > section.card.aim.-mtm.-fs16 > div.row.-pas > article:nth-child(3) > div > ul > li::text').getall()
        specification_value_trim=[]
        for i in specification_value:
            specification_value_trim.append(i.replace(':',''))
        
        specifications=dict(zip(specification_key,specification_value_trim))
        imageList=[]
        all_imges=response.css('label.itm-sel>img::attr("data-src")').getall()
        for i in all_imges:
            imageList.append(i)
        singleImage=response.css('#jm > main > div:nth-child(1) > section > div > div.col6.-phs.-pvxs > div>div>a::attr("href")').get()
        # unique id 
      
        
        def num():  
            global n
            n= n+1
           
            return n
        
        
        yield {
                "id":num(),
                "product_name":product_name,
                "discount":discount,
                "price": price,
                "brand":brand,
                "singleImage": singleImage,
                "imageList":imageList,
                "specification":specifications,
                "in_box":in_box,
                "key_features":key_features,
                "description":desc,
                 "no_of_ratings":no_of_ratings,

            }
        
          