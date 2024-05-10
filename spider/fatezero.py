"""

    url http://proxylist.fatezero.org/
    api http://proxylist.fatezero.org/proxy.list
    筛选匿名度  	high_anonymous

"""
import re
from spider.spiderbase import SpiderBase
from settings import FATEZERO_URL


__all__ = ['FateZeroCOM']


class FateZeroCOM(SpiderBase):

    def __init__(self):
        super().__init__()
        self.urls = [FATEZERO_URL]


    def parser(self, response):
        ips = []
        port = []
        proxylist = re.findall('{"anonymity": "high_anonymous", "from": "proxylist", "host": "(.+?)", "port": (.+?), .*?}', response.text, re.S)
        if proxylist:
            for item in proxylist:
                 ips.append(item[0])
                 port.append(item[1])
            
        return [ips, port]