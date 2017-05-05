#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests
import urllib
import json
import sys

class ConfigHttp:

    '''用于封装http请求方法,http头设置'''

    def __init__(self,host):
        self.host = host
        # self.port = port
        self.headers = {}

    # 设置 http 头
    def set_header(self,headers):
        self.headers = headers

    # 封装 HTTP GET 请求方法
    def get(self,url,params):
        params = urllib.urlencode(params) # 将参数转为 url 编码字符串
        url = "http://" + self.host + url + params
        try:
            response = requests.get(url,headers=self.headers)
            response = response.text.decode('uft-8')  # decode 函数对获取的字节数据进行解码
            json_response = json.loads(response)
            return json_response
        except Exception,e:
            print e.message
            return {}

    def post(self,url,data):
        data = json.dumps(data)
        data = data.encode('utf-8')


        # url = 'http://' + self.host + ':' + str(self.port) + url
        url = 'https://' + self.host + url

        try:
            response = requests.post(url, headers=self.headers, data=data)
            response = response.text.decode('utf-8')
            json_response = json.loads(response)
            return json_response
        except Exception,e:
            print e.message
            return {}




