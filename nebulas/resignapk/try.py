# -*- coding: utf-8 -*-
import shutil
import os
import sys

a = "C:\\Users\\郭永强\\Desktop\\Nasnano2.2\\wallet.apk"
print(a.split(os.sep))

path = a.split(os.sep)
lenth = len(path)
apk_name = path[-1]

print(path)
print(lenth)
print(path[-1])

root = os.getcwd()
tmp_path = root + os.sep + "tmp"
print(tmp_path)

#copy文件至tmp
if not os.path.exists(tmp_path):
	os.system("mkdir tmp")
shutil.copyfile(a,tmp_path+os.sep+apk_name)
#os.system("zip -d "+tmp_path+os.sep+apk_name+" META-INF/*")