"""
        代理爬虫基类
"""
import logging
import requests
from retrying import retry, RetryError
from requests.packages import urllib3
from requests.exceptions import ConnectionError
from tool.proxycollect import ProxyCollect
from settings import TIMEOUT, HEADERS


__all__ = ["SpiderBase"]


class SpiderBase: 
    """ 请求基类，所有代理的请求都可以继承该类，只需要实现parser方法即可 """

    def __init__(self, timeout=TIMEOUT):
        self.tiemout = timeout
        self.proxycollect = ProxyCollect()
        self.urls = []
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(asctime)s %(message)s")
        urllib3.disable_warnings()  # 去除SSL验证警告
        

    @retry(retry_on_result=lambda res: res is None, wait_fixed=1000, stop_max_attempt_number=3)
    def spider(self, url, **kwargs) -> requests.Response:
        """ get请求 """
        kwargs.setdefault('headers', HEADERS)
        kwargs.setdefault('proxies', None)
        kwargs.setdefault('timeout', self.tiemout)
        kwargs.setdefault('verify', False)
        try:
            response = requests.get(url, **kwargs)
        except ConnectionError:
            """ 链接失败 """ 
            logging.warning("  [%s 链接超时!]", url)
        except:
            logging.warning("  [%s 请求失败!]", url)
        else:
            if response and response.status_code == 200:
                logging.info("  [%s 请求成功，正在获取信息]", url)
                return response
            else:
                logging.warning("  [%s 响应为空!]", url)

        return None

    
    def yiku(self) -> ProxyCollect:
        """ 需要先实现parser方法之后才可以调用 """
        try:
            for url in self.urls:
                response = self.spider(url)
                self.proxycollect.add(*self.parser(response))
        except RetryError:
            logging.warning(f'多次请求无效，url >>> {url}')
            
        return self.proxycollect