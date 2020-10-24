# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SoftwareItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    software_category = scrapy.Field()
    software_name = scrapy.Field()
    software_down = scrapy.Field()

