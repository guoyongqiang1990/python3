# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : data.py
# @Software: PyCharm
# @Version ：V1.0
from uiautomator import Device
import time
import os
import cv2
import numpy as np

class Test:
	def __init__(self, deviceid):
		self.device = Device(deviceid)
		self.deviceid = deviceid

	def click(self, x, y):
		self.device.click(x, y)

	def startActivity(self, activity):
		os.system('adb -s %s shell am start %s' % (self.deviceid, activity))

	# 平均hash算法计算
	def classify_aHash(self, image1, image2):
		image1 = cv2.resize(image1, (8, 8))
		image2 = cv2.resize(image2, (8, 8))
		gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
		gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
		hash1 = self.getHash(gray1)
		hash2 = self.getHash(gray2)
		return self.Hamming_distance(hash1, hash2)

	# 输入灰度值，返回hash
	def getHash(self, image):
		avreage = np.mean(image)
		hash = []
		for i in range(image.shape[0]):
			for j in range(image.shape[1]):
				if image[i, j] > avreage:
					hash.append(1)
				else:
					hash.append(0)
		return hash

	# 计算汉明距离
	def Hamming_distance(self, hash1, hash2):
		num = 0
		for index in range(len(hash1)):
			if hash1[index] != hash2[index]:
				num += 1
		return num

	# 使用adb命令截取手机页面图片
	def screenshot(self):
		time.sleep(8)
	# os.system("adb shell /system/bin/screencap -p /sdcard/p2.png")     #（保存到SDCard）
	# os.system("adb pull /sdcard/p2.png E:\Study\uiautomator\picture")    #（保存到电脑）
		self.device.screenshot("E:\\Study\\uiautomator\\picture\\p2.png")

if __name__ == "__main__":
	w = Test('1ec8a07b')  # 记录手机串号，查看方式adb devices
	w.startActivity('com.android.mms/.ui.ConversationList')
	w.screenshot()
	img1 = cv2.imread("E:\\Study\\uiautomator\\picture\\p1.png")  # 读取保存的图片，原始图片
	img2 = cv2.imread("E:\\Study\\uiautomator\\picture\\p2.png")  # 读取与原始图相同使用screenshot方法截取的页面图片
	cv2.imshow("img1", img1)  # 展示图片1
	cv2.imshow("img2", img2)  # 展示图片2
	degree = w.classify_aHash(img1, img2)  # 调用方法，对比两张图片是否相同，返回值0为相同，返回1为不同，值越小，返回值越小，相似度越高
	print (degree)
	cv2.waitKey(0)