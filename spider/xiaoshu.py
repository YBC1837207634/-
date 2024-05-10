"""

    小舒代理
    url ：https://www.xsdaili.cn/

"""
import requests
from parsel import Selector
from spider.spiderbase import SpiderBase
from settings import XIAOSHU_URL


__all__ = ['XiaoShuCOM']


class XiaoShuCOM(SpiderBase):
    """
            该网站需要请求专栏来获取代理
    """

    def __init__(self):
        super().__init__()
        self.urls = self.div()


    def parser(self, response):
        """
            :
        """
        ips = []
        port = []
        selector = Selector(text=response.text)
        proxylist = selector.xpath('//div[@class="cont"]/text()[position()<101]').re('[0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?:[0-9]+')
        if proxylist:
            for proxy in proxylist:
                lit = proxy.split(':')
                ips.append(lit[0])
                port.append(lit[1])

        return [ips, port]


    def div(self):
        """ 获取专栏 url """    
        res = requests.get(
            XIAOSHU_URL, 
            headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                }

            )

        if res.status_code == 200:
            selector = Selector(text=res.text)
            div1_url = 'https://www.xsdaili.cn/' + selector.xpath('//div[@class="col-md-12"]/div[1]//a/@href').get() 
            div2_url = 'https://www.xsdaili.cn/' + selector.xpath('//div[@class="col-md-12"]/div[2]//a/@href').get()

        return [div1_url, div2_url]