#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
开启飞行模式，
开启双击点亮屏幕
测试步骤：
1，手机锁屏，等待手机灭屏后，双击唤醒
2，唤醒后，等待灭屏三分钟后测试待机电流
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
        Setting(DUT).launchSubSetings(["更多设置","动作手势"])
        Common(DUT).switchWidget("开启", "amigo:id/amigo_switchWidget")
        Common(DUT).switchWighetByIndex("关闭", 0, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 1, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 2, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 3, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 4, "com.android.settings:id/gesture_checkbox")
        Common(DUT).switchWighetByIndex("关闭", 5, "com.android.settings:id/gesture_checkbox")
    def test_step(self):
        Common(DUT).goBackHome()
        Common(DUT).lockScreen()
        Common(DUT).wait(7)
        Common(DUT).doubleClick(500, 500)
        Common(DUT).wait(2)
        USB.disconnectUsb()
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
