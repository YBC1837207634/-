"""

    提供服务器接口 ，请求该接口可以获取代理

"""
from flask import Flask
from tool.redisclient import RedisClient
from settings import MAX_POINT, REDIS_KEY


__all__ = ['app']

app = Flask(__name__)
R = RedisClient()


@app.route('/')
def hello():
    return "<h1> Hello </h1>"


@app.route('/random')
def have_random():
    """ 随机返回一个代理 """
    return R.random(REDIS_KEY, MAX_POINT, MAX_POINT)


@app.route('/list')
def proxyList():
    """ 返回所有可用代理 """
    proxies = R.haveList(REDIS_KEY, MAX_POINT, MAX_POINT)
    s = ''    
    for p in proxies:
        s += p + '  |  '
    
    return s


# if __name__ == '__main__':
#     app.run()
    
    