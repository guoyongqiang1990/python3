#-*- coding:utf-8 -*-
'''
用例标题：
预置条件：
1, Wifi开启
2,故事锁屏界面提示更新
3,不更新
测试步骤：
1，解锁屏幕后，测试待机3分钟
2,更新后，测试亮屏电流3分钟
预期结果：

'''
from aw import *
from aw.power import USB,PM 
######################################             
TAG=__file__.split("\\")[-1]
fPath=rootPath+"\\"+TAG          
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).clearRecentApp()
        Common(DUT).clearUserData("com.amigo.keyguard")
    def test_step(self):
        Common(DUT).startActivity("com.amigo.keyguard/com.amigo.navi.keyguard.category.CategoryBaseActivity")
        Common(DUT).clickById("com.amigo.keyguard:id/category_setting")
        Common(DUT).switchWidget("关闭", "com.amigo.keyguard:id/settings_switch_wallpaper_update")
        Setting(DUT).connectWifi(CONST.WIFI.SSID, CONST.WIFI.password)
        Common(DUT).goBackHome()
        Common(DUT).lockScreen()
        Common(DUT).wakeUp()
        if Common(DUT).exists(text="更新"):
            Common(DUT).unlockScreen()
            USB.disconnectUsb()
            PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
            USB.connectUsb()  
            Common(DUT).lockScreen()
            Common(DUT).wakeUp()
            Common(DUT).clickByText("更新")
            Common(DUT).clickWhenExist(text="同意")
            Common(DUT).wait(180)
            Common(DUT).unlockScreen()
            USB.disconnectUsb()
            PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName="test_power_keyguardStory_004", tPath=CONST.POWER.tPath)
            USB.connectUsb()  
        Common(DUT).unlockScreen()
    def tearDown(self):
        Setting(DUT).clearWifi()
        Setting(DUT).switchWifi("关闭")
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
