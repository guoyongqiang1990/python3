# coding=utf-8
from appium import webdriver
from time import sleep
import os
import unittest

# Returns abs path relative to this file and not cwd  如何定义路径，待研究
'''
PATH = lambda p: os.path.abspath(

    os.path.join(os.path.dirname(__file__), p)

)
'''


class AppMainPage(unittest.TestCase):
    def test_location(self):
        desired_caps = {}
        # 设置测试平台
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'A10ABMQE8WGU'
        # 设置启动参数
        desired_caps['appPackage'] = 'com.w2cx.businessversion'
        desired_caps['appActivity'] = 'com.w2cx.clientversion.module.splash.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.w2cx.clientversion.module.splash.SplashActivity'
        desired_caps['sessionOverride'] = 'true'  # 每次启动时覆盖session，否则第二次后运行会报错不能新建session
        desired_caps['unicodeKeyboard'] = 'true'  # 设置键盘
        desired_caps['resetKeyboard'] = 'true'  # 设置默认键盘为appium的键盘
        # desired_caps['udid'] = 'A10ABMQE8WGU'       #Unique device identifier of the connected physical device

        # 设置代理服务器
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # sleep(3)
        driver.implicitly_wait(10)
        # 获取上下文


        # 点击顶部定位栏
        driver.find_element_by_name("北京市").click()
        # sleep(2)
        driver.implicitly_wait(10)

        # 点击顶部搜索框
        search_text = driver.find_element_by_id("com.w2cx.businessversion:id/search_edit")
        # 清空搜索框
        search_text.clear()
        # 输入搜索词
        search_text.send_keys("武汉")
        # sleep(2)
        driver.implicitly_wait(10)
        driver.press_keycode(84)  # 为何不管用？？？

        # sleep(2)
        driver.implicitly_wait(10)

        # 切换到上海
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'上海市')]").click()
        driver.implicitly_wait(10)

        '''#点击热门词
        driver.find_element_by_id("com.w2cx.businessversion:id/search_edit").click()
        sleep(2)

        #点击“取消”按钮
        driver.findElementByName("取消").click()
        sleep(2)'''

        sleep(5)
        driver.close_app()
        driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)