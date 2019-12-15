# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import redis
#
# conn=redis.Redis(host='192.168.0.108',port=6379,password="123456")
# ret=conn.sadd("urls","12334")
# # ret1=conn.sadd("urls","123")
# # print(ret)
# print(ret)
# print(conn.smembers("urls"))
# conn.close()
from SpriderBase.spiders.chouti import ChoutiSpider
import warnings

def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        print(11111)
        warnings.warn('logfile argument deprecated', UserWarning,stacklevel=3)

s1=ChoutiSpider()


print(type(s1))
