# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium import webdriver
from BasePage import BasePage

#继承BasePage类
class LoginPage(BasePage):

    #定位器，通过元素属性定位元素对象
    username_loc = (By.ID, "loginName")
    password_loc = (By.ID, "pwd")
    verifycode_loc = (By.ID, "code")
    submit_loc = (By.CLASS_NAME, "ant-btn")

    #Action
    def open(self):
        #调用page中的_open()打开链接
        self._open(self.base_url, self.pagetitle)
    #调用sendkeys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)
    #调用sendkeys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
    #调用sendkeys对象，输入验证码
    def input_verifycode(self, verifycode):
        self.find_element(*self.verifycode_loc).send_keys(verifycode)
    #调用sendkeys方法登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
