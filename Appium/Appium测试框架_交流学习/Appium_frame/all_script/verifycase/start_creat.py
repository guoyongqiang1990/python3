# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : data.py
# @Software: PyCharm
# @Version ：V1.0
import sys
sys.path.append("..")
from appium import webdriver
import unittest, time, os, lujing
from testcase.test_shuku import CreatPage
from public import data, img_file
from data import test_phone
img_file = img_file.img_file()  #定义图片文件保存的位置
apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径

class take_screen_shot():  #这个类将在下面作为装饰器使用
	def __init__(self, func):
		self.func = func
		self.name = apk_path + '\\report\\img_result\\'+ img_file + '\\' + func.__name__ + '.png'  #拼接截图文件名

	def __call__(self, *args):   #对每次调用的函数都做截图操作
		try:
			self.func(self, *args)
		finally:
			driver.get_screenshot_as_file(self.name)

class Test(unittest.TestCase):
	"""验证脚本"""
	@classmethod
	def setUpClass(self):
		shouji = test_phone.testphone()
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',shouji)
		driver = self.driver
		global driver
		time.sleep(5)

	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	@take_screen_shot
	def test_01(self):
		"""测试用例1"""
		sp = CreatPage(driver)
		sp.shuku()
		assert '小王'=='小王',"验证失败！"

	@take_screen_shot
	def test_02(self):
		"""测试用例2"""
		sp = CreatPage(driver)
		sp.shuku()
		assert '小王'=='小王',"验证失败！"

if __name__ == '__main__':
	unittest.main()