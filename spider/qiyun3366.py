"""
    齐云3366s
    url https://proxy.ip3366.net/free/?action=china&page=1

"""
from parsel import Selector
from spider.spiderbase import SpiderBase
from settings import IP3366Q_URL, IP3366Q_INDEX


__all__ = ['QiYun3366COM']


class QiYun3366COM(SpiderBase):

    def __init__(self):
        super().__init__()
        self.urls = [ IP3366Q_URL.format(i+1) for i in range(IP3366Q_INDEX) ]

    
    def parser(self, response):
        selector = Selector(text=response.text)
        ip = selector.xpath('//tbody/tr/td[1]/text()').getall()
        port = selector.xpath('//tbody/tr/td[2]/text()').getall()

        return [ip, port]

