# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 14:06
# @Author  : shenwei
# @微信公众号    :老干部集中营
# @File    : Data.py
# @Software: PyCharm
# @Version ：V1.0
import time

#返回
def img_file():
	img_file_name = '%s'%time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
	return img_file_name