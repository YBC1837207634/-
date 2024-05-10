"""
        代理测试类\n
        从数据库中取出代理然后进行检测，可用代理保留，分数为0的代理删除\n
        因为需要检测的代理很多，所以采用异步请求来检测代理是否可用
"""
import time
import logging
import asyncio
import aiohttp
from tool.redisclient import RedisClient
from settings import HEADERS, TIMEOUT, REDIS_KEY, TESTER_URL, SUBSCORE, MAX_POINT, SEMAPHORE, TESTER_SILENT, TESTER_DEALY


__all__ = ['Tester']


class Tester:

    def __init__(self):
        self.db = RedisClient()
        self.timeout = aiohttp.ClientTimeout(total=TIMEOUT)
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(asctime)s %(message)s")
        self.semaphore = asyncio.Semaphore(SEMAPHORE)
                  
    async def __test(self, sesstion:aiohttp.ClientSession, url, proxy):
        """  异步测试代理 """
        async with self.semaphore:
            # logging.info(f'{proxy}>>>>{url}开始测试~~~')
            try:
                async with sesstion.get(url=url, headers=HEADERS, proxy='http://'+proxy) as response:
                    if response.status == 200:
                        logging.info(f'{proxy}访问  {url}成功！')
                        self.db.setPoint(REDIS_KEY, proxy, MAX_POINT)  # 设置分数
                        return 
                    else:
                        pass
            except:
                pass

            logging.info(f'{proxy}访问  {url}失败 代理无效！')    
            
            # 判定是否代理是否分数过低，如果过低就删除该代理
            if self.db.subPoint(REDIS_KEY, proxy, SUBSCORE):
                logging.warning(f'{proxy} 多次失败，代理无效，删除该代理')

        
    async def __run(self):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            while not TESTER_SILENT:
                proxylist = self.db.getall(REDIS_KEY)
                if proxylist:
                    tasks = [ asyncio.create_task(self.__test(session, TESTER_URL, proxy)) \
                            for proxy in proxylist ]
                    await asyncio.gather(*tasks)
                time.sleep(TESTER_DEALY)
                

    def run(self):
        try:
            asyncio.run(self.__run())
        except:
            logging.error('tester模块已经停止运行')
            self.db.close()


    

