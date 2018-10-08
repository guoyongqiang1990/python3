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
        Common(DUT).clearRecentApp()
        Common(DUT).setAirplaneMode("开启")
    def test_step(self):
        Common(DUT).startActivity("com.android.music/.activity.MusicCenterActivity")
        Common(DUT).clickWhenExist(text="去听歌")
        Common(DUT).clickById("com.android.music:id/playbar_play")
        Common(DUT).clickWhenExist(text="知道了")
        for i in range(20):
            Common(DUT).volumeUp()
            Common(DUT).clickWhenExist(text="确定")
        Common(DUT).lockScreen()
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=600, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
    def tearDown(self):
        Common(DUT).unlockScreen()
        Common(DUT).clickById("com.android.music:id/playbar_play")
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()