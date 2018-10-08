#-*- coding:utf-8 -*-
import os
import time
import json
import threading
from aw.common import Common
 
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
record = time.strftime("%Y-%m-%d_%H-%M-%S")
jsonFile="project.json"

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
    print deviceList
    return deviceList 

def getOtaPackage(sn):
    with open(rootPath+"\\"+jsonFile,"r") as f:
        DATA = json.load(f) 
#     if DATA["auto_upgrade"]["OTA"]=="yes":
    path="\\10.8.0.22\software_release\git_release\2017-04\02_ANDROID\G1602A\G1602A-T0131-170417AA_sign_user\BJ_G1602A_sign_T0131_OTA\ota"
    git_release="\\\\10.8.0.22\software_release\git_release"
    _DATE=time.strftime("%Y-%m")
    product=DATA["auto_upgrade"]["product"]
    tag=DATA["auto_upgrade"]["tag"]
    nowGnVersion=Common(sn).getGnVersion().split("_")[-1]
    print nowGnVersion
    #BJ_G1602A_sign_update_amigo3.5.0_T0121.zip
    rootdir=git_release+"\\"+_DATE+"\\02_ANDROID\\"+product
    print rootdir
    for parent,dirnames,filenames in os.walk(rootdir): 
        for filename in  filenames:  
            if "ota" in parent and tag in parent and ".zip" in filename:
#                 print filename
#                 print parent
                otapkg=filename.split("_")[-1] 
                otapkg=otapkg.split(".")[0]
                if otapkg > nowGnVersion:
                    otapkgPath= parent+"\\"+filename
                else:
                    print("已是最新版本")
                    time.sleep(3600)
        print otapkgPath
        return otapkgPath

def autoOta(sn):   
    with open(rootPath+"\\"+jsonFile,"r") as f:
        DATA = json.load(f) 
    if DATA["auto_upgrade"]["OTA"]=="yes":
        otaPackage=getOtaPackage(sn)
        zipFile=otaPackage.split("\\")[-1]
        Common(sn).copyFile(getOtaPackage(sn), "/storage/sdcard0/")
        Common(sn).launchSettings()
        Common(sn).swipeToBottom()
        Common(sn).clickByText("系统升级")
        Common(sn).clickById("gn.com.android.update:id/menu_setting")
        Common(sn).clickByText("本地升级")
        Common(sn).clickByText("手动选择更新包")
        Common(sn).swipeToBottom()
        Common(sn).swipeToBottom()
        Common(sn).clickByText(zipFile)
        Common(sn).clickByText("立即重启")
        return True
    else:
        return False
        
def myThreads():
    threadsList=[]
    for DUT in deviceList():
        print "DUT:"+DUT
        t = threading.Thread(target=autoOta,args=(DUT,) )
        threadsList.append(t)
    print threadsList
    for t in threadsList:
        t.setDaemon(True)
        t.start()
        time.sleep(5)
    for t in threadsList:
        t.join() 

if __name__=="__main__":
    myThreads()
        