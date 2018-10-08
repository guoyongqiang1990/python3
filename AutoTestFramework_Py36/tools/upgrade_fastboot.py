#-*- coding:utf-8 -*-
import time
import os
import threading
from aw.common import Common
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
def fastboot(sn,cmd):
    os.system("fastboot -s "+sn+" "+cmd)
    
def upgrade_fastboot(sn):

    os.system("adb -s "+sn+" reboot bootloader")
    print("----- reflash partition ... -----")
    fastboot(sn,"flash partition "+bp_path+"\\gpt_both0.bin")
    print("----- bp download ... -----")
    fastboot(sn,"flash sbl1 "+bp_path+"\\sbl1.mbn")
    fastboot(sn,"flash tz "+bp_path+"\\tz.mbn")
    fastboot(sn,"flash rpm "+bp_path+"\\rpm.mbn")
    fastboot(sn,"flash devcfg "+bp_path+"\\devcfg.mbn")
    fastboot(sn,"flash cmnlib "+bp_path+"\\cmnlib.mbn")
    fastboot(sn,"flash cmnlib64 "+bp_path+"\\cmnlib64.mbn")
    fastboot(sn,"flash keymaster "+bp_path+"\\keymaster.mbn")
    fastboot(sn,"flash cmnlib "+bp_path+"\\cmnlib.mbn")
    fastboot(sn,"flash modem "+bp_path+"\\NON-HLOS.bin")
    print("----- ap download ... -----")
    fastboot(sn,"flash persist "+ap_path+"\\persist.img")
    fastboot(sn,"flash aboot "+ap_path+"\\emmc_appsboot.img")
    fastboot(sn,"flash cache "+ap_path+"\\cache.img")
    fastboot(sn,"flash mdtp "+ap_path+"\\mdtp.img")
    fastboot(sn,"flash -S 300M system "+ap_path+"\\system.img")
    fastboot(sn,"flash recovery "+ap_path+"\\recovery.img")
    fastboot(sn,"flash boot "+ap_path+"\\boot.img")
    fastboot(sn,"flash splash "+bp_path+"\\splash.img")
    print("----- userdata download ... -----")
    fastboot(sn,"flash userdata "+ap_path+"\\userdata.img")
    print("----- update efs ... -----")
    fastboot(sn,"flash modemst1 "+bp_path+"\\dummy_bin.img")
    fastboot(sn,"flash modemst2 "+bp_path+"\\dummy_bin.img")
    fastboot(sn,"flash fsg "+bp_path+"\\fs_image.tar.gz.mbn.img")
    fastboot(sn,"reboot")
    
def upgrade_OTA(sn):
    OTA_PKG=r"Z:\git_release\2017-04\02_ANDROID\G1602A\G1602A-T0140-170421AA_sign_user\BJ_G1602A_sign_T0140_OTA\ota\BJ_G1602A_sign_update_amigo3.5.0_T0140.zip"
    os.system("adb -s %s push "%sn+OTA_PKG+" /storage/sdcard0/")
    Common(sn).launchSettings()
    Common(sn).swipeToBottom()
    Common(sn).clickByText("系统升级")
    Common(sn).clickById("gn.com.android.update:id/menu_setting")
    Common(sn).clickByText("本地升级")
    Common(sn).clickByText("自动扫描更新包")
    Common(sn).clickById("gn.com.android.update:id/gn_su_id_local_fileIcon")
    Common(sn).clickByText("立即重启")
    
def myThreads():
    threadsList=[]
    for DUT in deviceList():
        print "DUT:"+DUT
        t = threading.Thread(target=upgrade_OTA,args=(DUT,) )
        threadsList.append(t)
    print threadsList
    for t in threadsList:
        t.setDaemon(True)
        t.start()
        time.sleep(5)
    for t in threadsList:
        t.join()  
           
ap_path=r"D:\upgrade\G1602A_T0049\G1602A_T0049"
bp_path=ap_path+"\\bpimage"    
myThreads()