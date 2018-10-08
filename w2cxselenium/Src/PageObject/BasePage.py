# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ，FindElement等
    """
    #初始化driver，url等
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.driver = selenium_driver

    #通过title断言进入的页面是否正确
    #使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    #打开页面，校验页面链接是否加载正确
    #以单下划线开头的方法，在使用import*时，该方法不会被导入，保证该方法为类私有
    def _open(self, url, pagetitle):
        #使用get打开链接访问网址
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle), u"打开页面失败 %s" % url

    #定义open方法，调用_open()打开链接
    def open(self):
        self._open(self, url, pagetitle)

    #重写元素定位方法
    def find_element(self, *loc):
    # return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)

        except:
            print (u"%s 页面中未能找到 %s 元素" %(self, loc))

    #重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    #定义script方法，执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)

    #重写定义send_keys的方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s"% loc )
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" %(self, loc))








#封装页面通用的获取元素及元素操作的方法

    #在页面封装页面跳转方法

    #在页面封装获取单个element方法


    #在页面封装获取元素列表方法


    #在页面封装点击方法



    #在页面封装双击方法



    #在页面封装输入方法

    #页面刷新方法



    #在页面封装判断某元素是否存在方法


    #获取“内容审核”菜单


    #获取“运营管理”菜单