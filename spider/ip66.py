"""

    url http://www.66ip.cn/
    api http://www.66ip.cn/nmtq.php?getnum=50&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip

"""
from spider.spiderbase import SpiderBase
from settings import IP66_URL
from parsel import Selector


__all__ = ['IP66COM']


class IP66COM(SpiderBase):

    def __init__(self):
        super().__init__()
        self.urls = [IP66_URL]

    def parser(self, response):
        selector = Selector(text=response.text) 
        ips = []
        port = []
        # 111.0.65.4:9091   
        proxylist = selector.xpath('//body').re('[0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?:[0-9]+')
        for proxy in proxylist:
            split = proxy.split(':')
            if len(split) == 2:
                ips.append(split[0])   # ip
                port.append(split[1])

        return [ips, port]
    