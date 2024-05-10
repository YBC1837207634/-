import time
from parsel import Selector
from spider.spiderbase import SpiderBase
from settings import KUAIDAILI_URL, KUAIDAILI_INDEX


__all__ = ['KuaiDaiLiCOM']


class KuaiDaiLiCOM(SpiderBase):

    def __init__(self):
        super().__init__()
        self.urls = [KUAIDAILI_URL.format(i+1) for i in range(KUAIDAILI_INDEX)]

    def parser(self, response):
        """ 提取该网站中的代理 """
        selector = Selector(text=response.text)
        table = selector.xpath('//table[contains(@class,"table")]')
        ip = table.xpath('//td[@data-title="IP"]/text()').getall()
        port = table.xpath('//td[@data-title="PORT"]/text()').getall()
        time.sleep(1)
        return [ip, port]
    




