# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : Data.py
# @Software: PyCharm
# @Version ：V1.0
import sys
sys.path.append("..")
from public import apk
from appium import webdriver

#VIVO手机
def VIVO():
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '24'
	desired_caps['noReset'] = True  # 不需要每次都安装apk
	desired_caps['app'] = newlist  # 测试apk包
	desired_caps['deviceName'] = '1ec8a07b'  # vivo Y51A
	desired_caps['unxcodeKeyboard'] = 'True'
	desired_caps['resetKeyboard'] = 'True'
	#如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
	# desired_caps['appPackage'] = 'com.quduquxie'
	# desired_caps['appActivity'] = 'com.quduquxie.base.module.splash.view.SplashActivity'
	return desired_caps

#NOTE2手机
def NOTE2():
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '4.4.4'
	desired_caps['noReset'] = True  # 不需要每次都安装apk
	desired_caps['app'] = newlist # 测试apk包
	desired_caps['deviceName'] = '6O5711A41695'  # 红米NOTE2
	desired_caps['unxcodeKeyboard'] = 'True'
	desired_caps['resetKeyboard'] = 'True'
	#如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
	# desired_caps['appPackage'] = 'com.quduquxie'
	# desired_caps['appActivity'] = 'com.quduquxie.base.module.splash.view.SplashActivity'
	return desired_caps
	
newlist = apk.apk() #获取APK路径