"""
    IP3366

"""
from parsel import Selector
from settings import IP3366_URL, IP3366_INDEX
from spider.spiderbase import SpiderBase


__all__ = ['IP3366COM']


class IP3366COM(SpiderBase):

    def __init__(self):
        super().__init__()
        self.urls = [ IP3366_URL.format(i+1) for i in range(IP3366_INDEX)]

    def parser(self, response):
        selector = Selector(text=response.text)
        table = selector.xpath('//table[contains(@class,"table-bordered")]/tbody')
        ip = table.xpath('./tr/td[1]/text()').getall()     # ip 
        port = table.xpath('./tr/td[2]/text()').getall()  # 端口
        return [ip, port]
