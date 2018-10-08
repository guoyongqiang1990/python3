#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
关闭wifi，关闭GPS、蓝牙，音量最大，亮度为300cd/m2，清除后台应用
测试步骤：
1.打开视频应用，播放本地视频
2.全屏播放，3分钟后测试电流10分钟
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
        Common(DUT).setScreenTimeout("30min")
        Common(DUT).unlockScreen()
        Common(DUT).pushFile("video\\powerConsumption720P_11.25.mp4", "/storage/sdcard0/")
        Common(DUT).adbCmd("install -r -d "+ resourcePath+"apk\\Amigo_Video_6.0-local.apk")
        Common(DUT).launchSettings()
        Common(DUT).clickByText("显示")
        Common(DUT).switchWidget("true", "amigo:id/amigo_switchWidget")
        Common(DUT).switchWighetByIndex("关闭", 0, "android:id/checkbox")
        Common(DUT).goBack()
        Setting(DUT).switchWifi("关闭")
        Setting(DUT).switchBT("关闭")
        Setting(DUT).switchGPS("关闭")
        Common(DUT).clearRecentApp()

    def test_step(self):
        Common(DUT).goHome()
        Common(DUT).startActivity("com.gionee.video/.VideoMainActivity")
        Common(DUT).clickWhenExist(text="继续")
        Common(DUT).clickByText("设置")
        Common(DUT).switchWighetByIndex("开启", 0, "com.gionee.video:id/amigo_switchWidget")
        Common(DUT).goBack()
        Common(DUT).clickByText("扫描")
        Common(DUT).clickByText("内部存储器")
        Common(DUT).clickById("com.gionee.video:id/name")
        Common(DUT).clickWhenExist(text="我知道了")
        Common(DUT).wait(7)
        Common(DUT).clickScreenCenter()
        Common(DUT).clickById("com.gionee.video:id/screen_mode_switcher")
        for i in range(20):
            Common(DUT).volumeUp()
            Common(DUT).clickWhenExist(text="确定")
        
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=CONST.POWER.sample, mTime=600, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()  
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
