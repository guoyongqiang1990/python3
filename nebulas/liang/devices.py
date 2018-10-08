# -*- coding: utf-8 -*-
import os

def devices():
    #读取adb devices命令返回的信息
    devicelist = os.popen("adb devices").readlines()
    n = len(devicelist)-2
    #print(devicelist)
    device = []
    #从信息中读取设备列表
    for i in range(n):
        point = devicelist[i+1].index("\t")
        device.append(devicelist[i+1][:point])
     #print(device)
    return device



if __name__=="__main__":
    for i in devices():
        print("设备%s的输出结果请查看D:\monkey_%s.txt" % (i,i))
        os.popen("adb -s %s shell monkey -v --throttle 300 --pct-touch 30 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 --ignore-crashes --ignore-timeouts --monitor-native-crashes -p io.nebulas.wallet.android.test 50 >D:\monkey_%s.txt" % (i,i))






