"""
    **************  **************  ************** 不可用 **************  **************  ************** 
    高可用 
    直接提供api接口来获取代理
    https://ip.jiangxianli.com/api/proxy_ips
    GitHub: https://github.com/jiangxianli/ProxyIpLib#%E5%85%8D%E8%B4%B9%E4%BB%A3%E7%90%86ip%E5%BA%93
"""
from spider.spiderbase import SpiderBase
from settings import GAOKEYONG_URL, GAOKEYONG_INDEX


__all__ = ["GaoKeYongCOM"]


class GaoKeYongCOM(SpiderBase):

    silent = True    # 是否不加载该模块
    
    def __init__(self):
        super().__init__()
        self.url = GAOKEYONG_URL
        self.max_index = GAOKEYONG_INDEX
    
    def parser(self):
        """ 
        可以直接请求该网站提供的接口，不需要提取数据 
        page	int	N	第几页	1
        country	string	N	所属地区	中国,美国
        isp	string	N	ISP	电信,阿里云
        order_by	string	N	排序字段	speed:响应速度,validated_at:最新校验时间 created_at:存活时间
        order_rule	string	N	排序方向	DESC:降序 ASC:升序
        """
        ips = [] 
        ports = []
        for i in range(self.max_index):
            response = self.spider(self.url, params={"page": i})
            if response:
                data = response.json()
                proxylist = data.get('data').get('data')
                for proxy in proxylist:
                    ips.append(proxy.get('ip'))
                    ports.append(proxy.get('port'))

        self.proxycollect.add(ips, ports=ports)
        # self.proxycollect.show()
        return self.proxycollect.produce
    


if __name__ == '__main__':
    g = GaoKeYongCOM()
    g.send()