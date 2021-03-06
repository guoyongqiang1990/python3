#-*- coding:utf-8 -*-
import os
from aw.common import Common 
from uiautomator import Device
from logger import Logger

class Setting(Common):
    
    def launchSetting(self):
        self.startActivity("com.android.settings/.GnSettingsTabActivity")
        
    def launchSubSetings(self, items):
        '''
        item is list type
        '''
        self.launchSetting()
        for next in items:
            self.clickByText(next, screeScroll=True, timeout=20, waitTime=2)
            
    def switchWifi(self, status):
        _Dict={
            "开启":"false",
            "关闭":"true"
            }
        self.goBackHome()
        self.launchSubSetings(["WLAN"])
        self.switchWidget(_Dict[status], "com.gionee.setting.adapter.wifi:id/switch_widget")
        
    def switchBT(self, status):
        _Dict={
            "开启":"false",
            "关闭":"true"
            }
        
        self.goBackHome()
        self.launchSubSetings(["蓝牙"])
        self.switchWidget(_Dict[status], "com.gionee.setting.adapter.wifi:id/switch_widget")
        self.switchWidget(_Dict[status], "com.gionee.bluetooth:id/switch_widget") #适配G1602A
        
    def switchGPS(self, status):
        _Dict={
            "开启":"false",
            "关闭":"true"
            }
        self.goBackHome()
        self.launchSubSetings(["更多设置","位置信息"])
        self.switchWidget(_Dict[status], "com.gionee.setting.adapter.wifi:id/switch_widget")
        self.switchWidget(_Dict[status], "com.android.settings:id/switch_widget")#适配G1602A
        
    def switchData(self, status):
#         _Dict={
#             "开启":False,
#             "关闭":True
#             }
        self.switchAirplane("关闭")
        self.goBackHome()
        self.launchSubSetings(["移动网络"])
        self.switchWighetByIndex(status, 0, "amigo:id/amigo_switchWidget")
#         self.switchWidget(_Dict[status], "amigo:id/amigo_switchWidget")
        
    def switchAirplane(self, status):
        _Dict={
            "开启":"false",
            "关闭":"true"
            }
        self.goBackHome()
        self.launchSubSetings(["更多连接"])
        self.switchWidget(_Dict[status], "amigo:id/amigo_switchWidget")
        self.clickWhenExist(text="知道了")
        
    def connectWifi(self, SSID, password):
        self.switchWifi("开启")
        self.clickByText(SSID, screeScroll=True)
        if not self.exists(text="连接"):
            self.goBack()
        else:
            self.clickWhenExist(text="允许")
            self.setText("com.gionee.setting.adapter.wifi:id/password",password)
            self.wait(0.5)
            self.goBack()
            self.clickByText("连接")
        Logger.info("WIFI已连接")
        
    def clearWifi(self):
        self.launchSubSetings(["WLAN"])
        while self.exists(text="已知接入点"):
            self.clickById("com.gionee.setting.adapter.wifi:id/iv_ad_setting", 0)
            self.clickWhenExist(text="清除网络")
            self.clickWhenExist(text="清除")
        Logger.info("WIFI已清除")
        
    def switchHotpoint(self, status):
        _Dict={
            "开启":"false",
            "关闭":"true"
            }
        self.goBackHome()
        self.launchSubSetings(["个人热点", "WLAN 热点"])
        self.switchWidget(_Dict[status], "com.gionee.setting.adapter.wifi:id/switch_widget")
        self.wait(5)
        
        
if __name__=="__main__":
    Setting().clearWifi()
