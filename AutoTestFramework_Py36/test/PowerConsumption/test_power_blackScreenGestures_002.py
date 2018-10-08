#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
开启飞行模式
测试步骤：
1，开启黑屏手势，定义画↓↓解锁屏幕
2，锁屏,3分钟后测试待机电流
预期结果：

'''
from aw import * 
from aw.power import USB,PM 
# from aw.power import Power,USB 
######################################             
TAG=__file__.split("\\")[-1]      
fPath=rootPath+"\\"+TAG         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Setting(DUT).switchAirplane("开启")
#         Setting(DUT).switchWifi("关闭")
#         Setting(DUT).switchBT("关闭")
#         Setting(DUT).switchGPS("关闭")
#         Setting(DUT).switchData("关闭")
        Common(DUT).goBackHome()
        Common(DUT).clearRecentApp()
#         Common(DUT).clearUserData("com.gionee.softmanager")
    def test_step(self):
        Setting(DUT).launchSubSetings(["更多设置","动作手势"])
        Common(DUT).switchWidget("开启", "amigo:id/amigo_switchWidget")
        Common(DUT).switchWighetByIndex("关闭", 0, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 1, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 2, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("开启", 3, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 4, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 5, "com.android.settings:id/gesture_checkbox")
        Common(DUT).clickByText("黑屏手势")
        Common(DUT).clickByText("双指下滑", screeScroll=True)
        Common(DUT).clickByText("屏幕解锁")
        Common(DUT).clickWhenExist(text="确定")
        Common(DUT).clickByText("完成")
        Common(DUT).goBackHome()
        Common(DUT).lockScreen()
        
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=CONST.POWER.sample, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Setting(DUT).launchSubSetings(["更多设置","动作手势"])
        Common(DUT).switchWidget("关闭", "amigo:id/amigo_switchWidget")
        Setting(DUT).switchAirplane("关闭")
        Common(DUT).goHome()
if __name__ == "__main__":
    unittest.main()
