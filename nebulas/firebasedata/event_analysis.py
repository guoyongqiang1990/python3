# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://console.firebase.google.com/project/fir-demo-project/analytics/app/android:com.labpixies.flood/events')
driver.maximize_window()
print(driver.title)
driver.find_element_by_id("identifierId").clear()
driver.find_element_by_id("identifierId").send_keys("yongqiang.guo@nebulas.io")
driver.find_element_by_css_selector("#identifierNext > content:nth-child(3) > span:nth-child(1)").click()

driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("guoyongqiang1990")
driver.find_element_by_css_selector("#passwordNext > content:nth-child(3) > span:nth-child(1)").click()
driver.implicitly_wait(10)

sleep(50)

driver.quit()
