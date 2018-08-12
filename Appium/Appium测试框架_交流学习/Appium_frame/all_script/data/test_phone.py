# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : data.py
# @Software: PyCharm
# @Version ：V1.0
import sys
sys.path.append("..")
import os, yaml
from data import information

#通过test_phone.yaml文件获取返回手机信息
def testphone():
	path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	f = open( path + '\\data\\test_phone.yaml', 'rb')
	files = yaml.load(f)
	f.close()
	file = files['Phone']
	if file == 'VIVO':
		shouji = information.VIVO()
	elif file == 'NOTE2':
		shouji = information.NOTE2()
	else:
		print('您在test_phone.yaml输入的测试机没有相关信息')
		shouji = '空'
	print('获取到手机信息为：%s' %shouji)
	return shouji