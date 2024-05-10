HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }


TIMEOUT = 3
CMD = 'db\\redis-server.exe'

# tester
TESTER_SILENT = False   # 是否关闭
TESTER_DEALY = 8        # 检测间隔时间
DEFAULT_POINT = 10      # 默认分数
SUBSCORE = -2           # 每次减去2分
SEMAPHORE = 10          # 最多10个并发
MAX_POINT = 100
TESTER_URL = 'https://www.baidu.com/'


# getter
GETTER_SILENT = False   # 是否关闭
GETTER_DELAY = 180       # 获取代理的间隔时间 


# redis数据库配置
HOST = 'localhost'
PORT = '6379'
DBINDEX = 0        # 第几个数据库
REDIS_KEY = 'HTTP'

# 快代理
KUAIDAILI_URL = 'https://www.kuaidaili.com/free/inha/{}/'   
KUAIDAILI_INDEX = 3


# 66ip   高匿 国内外  通过API获取代理   修改 gtenum的字段
IP66_URL = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip'
IP66_INDEX = 3


# IP3366
IP3366_URL = 'http://www.ip3366.net/?stype=1&page={}'
IP3366_INDEX = 5


#IP3366 奇云daili
IP3366Q_URL = 'https://proxy.ip3366.net/free/?action=china&page={}'
IP3366Q_INDEX = 2


# 高可用
GAOKEYONG_URL = 'https://ip.jiangxianli.com/api/proxy_ips'   # api
GAOKEYONG_INDEX = 4


# fatezero
FATEZERO_URL = 'http://proxylist.fatezero.org/proxy.list'
#{"anonymity": "high_anonymous", "from": "proxylist", "host": "(+?)", "port": (+?), .*?}


# 小舒代理    该代理网站与其余代理不同，需要获取最新专栏来从里面提取出代理
XIAOSHU_URL = 'https://www.xsdaili.cn/'
XIAOSHU_INDEX = 2      # 只选择前三个专栏


# 免费代理 yqie.com
YQIE_URL = 'http://ip.yqie.com/ipproxy.htm'
