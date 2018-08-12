# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : data.py
# @Software: PyCharm
# @Version ：V1.0
import time, os, sys, unittest
import HTMLTestRunner
from module import creat_img_file
from module import sendreport

#========================将测试用例添加到测试套件========================
def creatsuite():
	testunit = unittest.TestSuite()

	#定义测试文件查找目录
	test_dir = (os.getcwd()+ '/all_script/')

	#定义discover方法的参数
	discover = unittest.defaultTestLoader.discover(
		test_dir,
		pattern = 'start_*.py',
		top_level_dir = None)

	#discover方法筛选出来的用例，循环添加到测试套件中
	for test_case in discover:
		testunit.addTests(test_case)
	return testunit

#创建HTML文件
file_name = sendreport.file_name

#创建图片放置文件夹
img_file = sendreport.img_file

fp = open(file_name, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = 'APP测试用例报告',
	description = u'APP用例执行情况')

if __name__ == '__main__':
	creat_img_file.creat_img_file(img_file)
	alltestnames = creatsuite()
	runner.run(alltestnames)
	fp.close()
	# sendreport.sendreport()