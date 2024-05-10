"""
    链接redis数据库
    
"""
import logging
from redis import StrictRedis
from tool.proxycollect import ProxyCollect
from random import choice
from settings import HOST, PORT, DBINDEX, DEFAULT_POINT


__all__ = ['RedisClient']


class RedisClient:

    def __init__(self):
        self.db = StrictRedis(host=HOST, port=PORT, db=DBINDEX)
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(asctime)s %(message)s")

    def put(self, key, proxycollect:ProxyCollect):
        """  将代理存放到数据库中 """
        if proxycollect.empty():
            logging.warning('代理列表为空，无法存入数据库!')
            return 
        for proxy in proxycollect.produce():
            if not self.exists(key, proxy):  # 判断是否一个键内是否有相同的元素
                if self.db.zadd(key, {proxy: DEFAULT_POINT}):
                    logging.info(f' {key} : {proxy} 存放成功！')
                else:
                    logging.warning(f' {key} : {proxy} 存放失败！')

    def getall(self, key:str) -> list[str]:
        """ 获取数据库中所有的代理 """
        return self.decode(self.db.zrevrange(key, 0, -1))

    def exists(self, key, element) -> bool:
        """ 判断一个键中是否包含某个元素 """
        return bool(self.db.zscore(key, element))
    
    def delete(self, key, value):
        """ 指定键删除对应的值 """
        self.db.zrem(key, value)
    
    def subPoint(self, key, value, score) -> int | None:
        """ 减分，如果分数过低就删除该代理 """
        self.db.zincrby(key, score, value)   # 降低得分
        s = self.db.zscore(key, value)  # 获取当前代理的得分
        if s <= 0:
            return self.db.zrem(key, value)   # 分数过低，删除代理
        return None

    def setPoint(self, key, value, score):
        """ 设置分数 """
        self.db.zadd(key, {value: score})
        
    def decode(self, byte) -> list[str] | str:
        """  将字节序列转换为 字符串 """
        # if isinstance(byte, list):
        strlist = [ b.decode(encoding='utf-8') for b in byte ]
        return strlist
        # return byte.decode(encoding='utf-8')

    def random(self, key, s_score, e_score) -> str:
        """ 从指定的键中随机去除一个元素 """
        proxies = self.db.zrangebyscore(key, s_score, e_score)
        if proxies:
            proxies = self.decode(proxies)
            return choice(proxies)    # 从列表中随机取出一个元素
            
        return ''
                
    def haveList(self, key, s_score, e_score) -> list[str]:
        """ 获取所有可用代理组成的列表 """
        proxies = self.decode(self.db.zrangebyscore(key, s_score, e_score))
        return proxies

    def close(self):
        self.db.close()



def openRedis():
    """ 启动数据库进程 """
    # return subprocess.Popen(CMD, shell=True)
