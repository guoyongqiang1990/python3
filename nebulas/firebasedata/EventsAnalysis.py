# -*- coding: utf-8 -*-
__author__ = 'MrGuo'

###############################
#
#验证firebase埋点数据
#
#
###############################

import os
import csv
import sys
import requests
import json


def Get_web_info(url):
    '''
    :param url: website
    '''
    # 请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    #request = urllib.request.Request(url=url, headers=headers)
    # 爬取结果
    response = requests.get(url,headers = headers)
    # 设置解码方式
    response.encoding = "utf-8"
    # # 打印结果
    data = response.text
    print('----------------------------------------------')
    print(data)
    return data

if __name__ == '__main__':
    Get_web_info("https://www.google.com")