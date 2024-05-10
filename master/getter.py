"""
    调度spider包中的所有代理，然后存放到数据库中
"""
import logging
import time
import spider
from tool.redisclient import RedisClient
from settings import GETTER_DELAY, GETTER_SILENT, REDIS_KEY


__all__ = ['Getter']


class Getter:

    def __init__(self):
        self.client = RedisClient()
        self.spiderTasks = [ task() for task in spider.__all__]
        
    def run(self):
        try:
            while not GETTER_SILENT:
                
                for spider in self.spiderTasks:
                    self.client.put(REDIS_KEY, spider.yiku())
                time.sleep(GETTER_DELAY)
        except:
            logging.error('getter模块已经停止运行')
            pass
        finally:
            self.client.close()
            


