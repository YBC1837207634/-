存储模块：负责存储爬取下来的代理。首先要保证代理不重复，标识代理的可用情况，其次要动态实时地处理每个代理， 一种比较高效和方便的存储方式就是 Redis的 Sorted Set，即有序集合。

获取模块：负责定时在各大代理网站爬取代理。代理既可以是免费公开的，也可以是付费的形式都是IP加端口。此模块尽量从不同来源爬取，并且尽量爬取高置代理，爬取放功后格可用代理存储到存储模块中。

检测模快：负责定时检测存储模块中的代理是否可用，设置一个检测链接、可以设置为需要爬取的那个网站，这样更具有针对性。对于一个通用型的代理、可以设置为百度链接。标识每一个代理的状态，设置分数标识，100分代表可用，分数越少代表越不可用。将分数标识立即设置为满分100，也可以在原分数基酬上加1；如果代理不可用，就将分数标识减1，当分数减到一定阔值后，直接从存储模块中删除此代理。这样就可以标识代理的可用情况，在选用的时候也会更有针对性。

接口模块：用API提供对外服务的接口。提供一个Web API 接口，访问这个接口即可拿到可用代理。


![image](https://github.com/YBC1837207634/proxy-pool/assets/134582298/1f47ea89-860b-4b14-8bd0-216174b8f7fb)
