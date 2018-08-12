# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.maximize_window()
print(driver.title)

sleep(5)

driver.quit()