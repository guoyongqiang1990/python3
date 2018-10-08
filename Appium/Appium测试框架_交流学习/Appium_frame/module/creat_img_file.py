# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : Data.py
# @Software: PyCharm
# @Version ：V1.0
import os

#创建图片文件夹
def creat_img_file(path):
		# 去除首位空格
		path = path.strip()
		# 去除尾部 \ 符号
		path = path.rstrip("\\")
		# 判断路径是否存在，存在为True，不存在为False
		isExists = os.path.exists(path)
		# 判断结果
		if not isExists:
			# 如果不存在则创建目录，创建目录操作函数
			os.makedirs(path)
			print(path + ' 创建成功')
			return True
		else:
			# 如果目录存在则不创建，并提示目录已存在
			print(path + ' 目录已存在')
			return False