# -*- coding: utf-8 -*-
import os

def devices():
    devicelist = os.popen("adb devices").readlines()
    n = len(devicelist)-2
    print(devicelist)
    device = []
    for i in range(n):
        point = devicelist[i+1].index("\t")
        device.append(devicelist[i+1][:point])
     #print(device)
    return device



def deviceList():
    devices = os.popen("adb devices").read()
    print(devices)
    devices = devices.split("\n")
    print(devices)
    deviceList=[]
    #print devices
    for line in devices:
        line=line.split("\t")
        if (line[-1])=="device":
            deviceList.append(line[0])
        if line[-1]=="offline":
            print("%s is offline" % line[0])
    print(deviceList)
    return deviceList


if __name__=="__main__":
    for i in devices():
        print("设备%s的输出结果请查看D:\monkey_%s.txt" % (i,i))
        os.popen("adb -s %s shell monkey -v --throttle 300 --pct-touch 30 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 --ignore-crashes --ignore-timeouts --monitor-native-crashes -p io.nebulas.wallet.android.test 50 >D:\monkey_%s.txt" % (i,i))






