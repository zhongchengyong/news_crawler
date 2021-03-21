import scrapy
import json
import os
import requests

from scrapy import Request
from scrapy.commands import fetch

PAGE_COUNT = 2321 # 23226 articals related: http://newssearch.chinadaily.com.cn/en/search?query=covid-19

# PAGE_COUNT = 23 # 23226 articals related: http://newssearch.chinadaily.com.cn/en/search?query=covid-19


class ChinadailySpider(scrapy.Spider):
    name = 'chinadaily'
    file_name = 'covid-19.html'
    allowed_domains = ['www.chinadaily.com.cn/']

    def start_requests(self):
        with open(self.file_name, 'w') as f:
            pass
        for i in range(PAGE_COUNT):
            list_url = 'http://newssearch.chinadaily.com.cn/rest/en/search?keywords=covid-19&sort=dp&page={}&curType=story&type=&channel=&source='.format(i)
            contents = requests.get(list_url).json()['content']

            # from ipdb import set_trace;set_trace()
            # content_str = news_list.decode('utf-8')
            # contents = json.loads(content_str)['content']
            for content in contents:
                yield self.make_requests_from_url(content['url'])

    def parse(self, response, **kwargs):
        title = response.xpath('/html/head/title/text()').extract()
        print(title)
        contents = response.xpath('//div[@id="Content"]/p/text()').extract()
        with open(self.file_name, 'a') as f:
            f.write('\n'.join(title) + '\n')
            f.write('\n'.join(contents) + '\n')
            # f.write(response.body.decode('utf-8') + '\n')

