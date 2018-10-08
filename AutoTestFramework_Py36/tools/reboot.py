#-*- coding:utf-8 -*-
import os,sys
import threading
def deviceList():
    devices=os.popen("adb devices").read()
    devices=devices.split("\n")
    deviceList=[]
#     print devices
    for line in devices:
        line=line.split("\t")
        if line[-1]=="device":
            deviceList.append(line[0])
        if line[-1]=="offline":
            print("%s is offline"%line[0])
    print(deviceList)
    return deviceList  
    
 
def reboot(sn):
    if len(deviceList())!=0:
        os.system("adb -s %s reboot"%sn)
        print ("restart pbone")
def powerOff(sn):
    if len(deviceList())!=0:
        os.system("adb -s %s shell reboot -p"%sn )
        print("power off ")
def recovery(sn):
    if len(deviceList())!=0:
        os.system("adb -s %s reboot factory reset"%sn )
        
def myThreads():
    threadsList=[]
    for DUT in deviceList():
        print("DUT:"+DUT)
        t = threading.Thread(target=powerOff,args=(DUT,) )
        threadsList.append(t)
    print(threadsList)
    for t in threadsList:
        t.setDaemon(True)
        t.start()
    for t in threadsList:
        t.join()    
        
myThreads()