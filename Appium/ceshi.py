#coding=utf-8
from appium import webdriver
from time import sleep

try:

        desired_caps = {}
        #设置测试平台
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'C4Y7N16506009767'
        #设置启动参数
        desired_caps['appPackage'] = 'io.nebulas.wallet.android.test'
        desired_caps['appActivity'] = 'io.nebulas.wallet.android.module.launch.LaunchActivity'
        desired_caps['appWaitActivity'] = 'io.nebulas.wallet.android.module.launch.LaunchActivity'
        desired_caps['sessionOverride'] = 'true' #每次启动时覆盖session，否则第二次后运行会报错不能新建session
        desired_caps['unicodeKeyboard'] = 'true' #设置键盘
        desired_caps['resetKeyboard'] = 'true'   #设置默认键盘为appium的键盘
        #desired_caps['udid'] = 'A10ABMQE8WGU'       #Unique device identifier of the connected physical device

        #设置代理服务器
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #sleep(3)
        driver.implicitly_wait(10)


        # 点击不升级
        driver.find_element_by_id("io.nebulas.wallet.android.test:id/rootView").click()
        #sleep(2)
        driver.implicitly_wait(10)

        #点击同意协议
        driver.find_element_by_id("io.nebulas.wallet.android.test:id/agreeCB").click()
        # sleep(2)
        driver.implicitly_wait(10)

        driver.find_element_by_id("io.nebulas.wallet.android.test:id/positiveTV").click()
        # sleep(2)
        driver.implicitly_wait(10)

        """
        search_text.clear()
        #输入搜索词
        search_text.send_keys("武汉")
        #sleep(2)
        driver.implicitly_wait(10)
        driver.press_keycode(84)       #为何不管用？？？

        #sleep(2)
        driver.implicitly_wait(10)

        #切换到上海
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'上海市')]").click()
        driver.implicitly_wait(10)

        w = driver.get_window_size()['width']
        h = driver.get_window_size()['height']
        #driver.swipe(int(w * 0.25), int(h * 0.5), int(w * 0.75), int(h * 0.5), 1000)

        sleep(2) #此处使用implicitly_wait会报错，不知道为啥

        driver.swipe(int(w * 0.5), int(h * 0.75), int(w * 0.5), int(h * 0.25), 1000)
        driver.find_elements_by_id('com.w2cx.businessversion:id/home_infor_title')[0].click()#点击第一条资讯
        driver.implicitly_wait(30)
        driver.tap([(694,1814)],1000)

        '''#点击热门词
        driver.find_element_by_id("com.w2cx.businessversion:id/search_edit").click()
        sleep(2)
        
        #点击“取消”按钮
        driver.findElementByName("取消").click()
        sleep(2)'''
        """

        sleep(5)
        driver.close_app()

finally:
        driver.quit()
