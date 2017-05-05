#!/usr/bin/env python
#-*- coding:utf-8 -*-

import configparser

# BaseHttp 类
class BaseHttp:
    '''配置要测试接口服务器的 ip、端口、域名等信息'''

    def __init__(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file)
        self.host = config['DEFAULT']['host']
        self.port = config['DEFAULT']['port']

    def set_host(self,host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port