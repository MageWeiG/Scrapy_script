# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SoftwarePipeline:
    def process_item(self, item, spider):
        num_int = 0
        download_num = item['software_down']
        if 'M' in download_num:
            num_int = int(download_num[:-1])
            item['software_down'] = num_int * 100
        elif 'K' in download_num:
            num_int = int(download_num[:-1])
            item['software_down'] = num_int/10
        else:
            num_int = int(download_num)
            item['software_down'] = num_int/10000
        if (item['software_down'] >= 5):
            return item
        else:
            return
        
