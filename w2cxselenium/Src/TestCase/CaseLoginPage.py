#-*- coding: utf-8 -*-

import sys
sys.path.append("..")
import importlib
importlib.reload(sys)
import unittest
from PageObject import LoginPage
from selenium import webdriver

class Caselogin52cx(unittest.TestCase):
    """
    登录后台管理系统的case
     """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)

        cls.url ="http://172.16.10.68:5050"
        cls.username ="15630893829"
        cls.password ="893829"
        cls.verifycode = "0000"

    #用例执行体
    def test_login_52cx(self):
        #声明LoginPage类对象
        login_page =LoginPage.LoginPage(self.driver, self.url, u"我爱出行管理平台")

        #调用打开页面组件
        login_page.open()
        #调用用户名输入组件
        login_page.input_username(self.username)
        #调用密码输入组件
        login_page.input_password(self.password)
        #调用点击登录按钮组件
        login_page.click_submit()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main()