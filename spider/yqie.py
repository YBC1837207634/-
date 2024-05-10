"""
    免费代理
    url http://ip.yqie.com/ipproxy.htm
"""
from parsel import Selector
from spider.spiderbase import SpiderBase
from settings import YQIE_URL


__all__ = ['YQIE_URL']


class YQieCOM(SpiderBase):

    def __init__(self):
        super().__init__()
        self.urls = [YQIE_URL]

    
    def parser(self, response):
        selector = Selector(text=response.text)
        ips = selector.xpath('//table//tr[position()>1 and position()<19]/td[1]/text()').getall()   # ip
        port = selector.xpath('//table//tr[position()>1 and position()<19]/td[2]/text()').getall()
        return [ips, port]