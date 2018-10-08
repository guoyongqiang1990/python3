#-*- coding:utf-8 -*-
'''
用例标题：
预置条件：
1，飞行模式开启
2，关闭闪光灯
3，关闭HDR
测试步骤：
1，打开相机，选择前置摄像头
2，测试录制视频5分钟
预期结果：

'''
from aw import *
from aw.power import USB,PM 
######################################             
TAG=__file__.split("\\")[-1]
TAG = TAG.split('.')[0]                  
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).clearRecentApp()
        Common(DUT).clearUserData("com.android.camera")
        Common(DUT).startActivity("com.android.camera/.CameraLauncher")
        Common(DUT).clickById("com.android.camera:id/flashlight_picker")
        Common(DUT).clickByText("关闭")
        Common(DUT).clickById("com.android.camera:id/hdr_picker")
        Common(DUT).clickByText("关闭")
    def test_step(self):
        Common(DUT).clickByText("名片扫描")
        Common(DUT).clickByText("摄像")
        Common(DUT).clickById("com.android.camera:id/camera_picker")
        Common(DUT).clickById("com.android.camera:id/shutter_button_icon")
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
        Common(DUT).clickById("com.android.camera:id/shutter_button_icon")
        Common(DUT).clickById("com.android.camera:id/camera_picker")
        Common(DUT).clickById("com.android.camera:id/settings_btn")
        Common(DUT).clickByText("还原设置")
        Common(DUT).clickByText("确定")
        Common(DUT).goBackHome()
        Common(DUT).lockScreen()
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName="test_power_CameraToIdle_005", tPath=CONST.POWER.tPath)
        USB.connectUsb()    
    def tearDown(self):
        Common(DUT).unlockScreen()
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()