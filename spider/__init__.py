"""
      代理获取，继承Spiderbase，重写parser方法来获取所需网站的代理。
      导入该包时自动载入当前包中所有的代理模块
      所写代理类继承Spiderbase，然后实现成员urls(类型为列表), 然后将所需获取的网页放到该列表中\n
      实现parser方法，接受一个response，然后解析该服务器响应类，最后返回[ip, port]即可。
      如果该代理不需要继续使用只需要在该类中定义一个silent然后值为True即可。

"""
import pkgutil
import inspect
from spider.spiderbase import SpiderBase


classes = []
for finder, name, ispkg in pkgutil.walk_packages(__path__):
    module = finder.find_spec(name).loader.load_module(name)
    items = inspect.getmembers(module, inspect.isclass)
    for name, value in items:
        if value and value is not SpiderBase and issubclass(value, SpiderBase) and not \
              getattr(value, 'silent', False):
            classes.append(value)

__all__ = classes

