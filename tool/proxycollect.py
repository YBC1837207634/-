"""
    存放代理，提供添加和产出代理的接口

"""


class ProxyCollect:
    """ 存放从代网站中提前的代理 """

    def __init__(self, level:str=None):
        self.__collect = {
            'ip': [],
            'port': []
        }
        self.secret_level = level
        
    def add(self, ips:list, ports:list):
        self.__collect['ip'] = self.__collect.get('ip') + ips if ips else None
        self.__collect['port'] = self.__collect.get('port') + ports if ports else None
    
    @property
    def returndict(self) -> dict:
        """  以字典的形式返回代理  """
        return self.__collect
    
    def produce(self) -> str:
        """  可迭代  """
        ip = self.__collect['ip']
        port = self.__collect['port']
        if self.empty():
            return []
        try:
            for i, p in zip(ip, port):
                yield i + ':' + p
        except StopIteration:
            pass
    
    def __repr__ (self) -> str:
        return f"ProxyCollect< {self.__collect} >"
    
    @property
    def s(self) -> str:
        s = ''
        ips = self.__collect.get('ip')
        ports = self.__collect.get('port')
        for ip, port in zip(ips, ports):
            # print(ip, ':', port)
            s += f'{ip} : {port} \n'
        return s

        
    def empty(self):
        """ 是否为空 """
        return self.__collect['ip'] is [] or self.__collect is []