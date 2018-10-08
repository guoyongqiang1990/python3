# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : Data.py
# @Software: PyCharm
# @Version ：V1.0
import os, yaml

def data():
	path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	f = open( path + '\\Data\\button.yaml', 'rb')
	file = yaml.load(f)
	f.close()
	return file