#-*- coding:utf-8 -*-
import os
# import time

def shell(cmd):
    os.system("adb shell "+cmd)
    

shell("am start -n com.gionee.note/.HomeActivity")
shell("input tap 290 1838")#点击“新建”根据手机适配坐标点
for i in range(10):
    shell("input text abcdefghigklmnopqrstuvwxyzabcdefghigklmnopqrstuvwxyz")
    shell("input keyevent 66")
    shell("input keyevent 66")


