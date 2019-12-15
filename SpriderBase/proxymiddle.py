#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64
import random
from six.moves.urllib.parse import unquote

try:
    from urllib2 import _parse_proxy
except ImportError:
    from urllib.request import _parse_proxy
from six.moves.urllib.parse import urlunparse
from scrapy.utils.python import to_bytes


class ProxyMiddleware(object):

        # 作用是把密码等信息进行base64加密
    def _basic_auth_header(self, username, password):
        user_pass = to_bytes(
            '%s:%s' % (unquote(username), unquote(password)),
            encoding='latin-1')
        return base64.b64encode(user_pass).strip()

        #  在下载页面之前执行
    def process_request(self, request, spider):
        PROXIES = [
            "https://194.226.34.132:5555",
            "https://112.84.178.21:8888",
        ]
        # PROXIES = [
        #     # "http://118.31.56.152:3128",
        #     "http://36.25.41.166:9999",
        #     "http://116.113.27.170:50035",
        # ]
        url = random.choice(PROXIES)
        print(url,"proxy")
        orig_type = ""
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))

        if user:
            creds = self._basic_auth_header(user, password)
        else:
            creds = None
        request.meta['proxy'] = proxy_url
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic ' + creds


"""
免费代理地址
    http://www.kxdaili.com/dailiip.html
"""