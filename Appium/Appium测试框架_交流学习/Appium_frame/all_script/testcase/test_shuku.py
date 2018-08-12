# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : data.py
# @Software: PyCharm
# @Version ：V1.0
import sys
sys.path.append("..")
import time, os, lujing
from appium import webdriver
from public import location_element, data

datas = data.data()
class CreatPage(location_element.Action):
	'''测试脚本'''

	shuku1 = datas['shuku']
	def shuku(self):
		'''点击书库'''
		self.findId(self.shuku1).click()
		time.sleep(3)