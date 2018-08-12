# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : data.py
# @Software: PyCharm
# @Version ：V1.0
import os

#获取APK文件，输入路径
def apk():
	apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	#  获取APP文件夹下的.apk文件
	newlist = []
	items = os.listdir(apk_path + '\\app\\')
	for names in items:
		if names.endswith(".apk"):
			newlist.append(names)
			file = apk_path + '\\app\\' + newlist[0]
	return file  #输出APK路径