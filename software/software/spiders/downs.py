import scrapy
import os
from ..items import SoftwareItem

class DownsSpider(scrapy.Spider):
    name = 'downs'
    allowed_domains = ['https://en.softonic.com/']    
    #start_urls = ['https://en.softonic.com/windows/security-privacy:weekly-downloads/2']

    def start_requests(self):
        #category 13
        all_category = ['browsers','security-privacy','games','business-productivity','internet-network','multimedia','development','education-reference','lifestyle','personalization','social-communication','travel-navigation','utilities-tools']

        conjunctions = ':weekly-downloads'

        start_urls = ['https://en.softonic.com/windows']

        for category in all_category:
            for i in range(1,11,1):
                path = os.path.join(start_urls[0],(category+conjunctions),str(i))
                print(path)
                yield scrapy.Request(
                    url = path,
                    callback = self.parse,
                    meta = {'category':category}
                )

                
    def parse(self, response):

        soft_name = response.xpath('/html/body/div[@class="wrapper"]')[1].xpath('./div/div[@class="content content--colored"]/ul/li/a/article/div[@class="app-list-item__media"]/div[@class="media media--top media-app"]/div[@class="media__body"]/h2/text()').extract()
        downloads = response.xpath('/html/body/div[@class="wrapper"]')[1].xpath('./div/div[@class="content content--colored"]/ul/li/a/article/div[@class="app-list-item__rating"]/div[3]/text()').re('(.+) downloads')

        
        for i in range(20):
            software_info = SoftwareItem()            
            software_info['software_category'] = response.meta['category']
            software_info['software_name'] = soft_name[i]
            software_info['software_down'] = downloads[i]
            yield software_info
        
        out_data = dict(zip(soft_name,downloads))
        print(response.meta['category'])
        print(out_data)
        #yield out_data
