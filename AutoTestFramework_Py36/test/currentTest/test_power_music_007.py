#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入音乐app
2.播放默认歌曲
3.锁屏
4.持续播放20分钟
5.点亮屏幕解锁
6.停止播放音乐，返回待机
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
        
    def test_step(self):
        Common(DUT).startActivity("com.android.music/.activity.MusicCenterActivity")
        Common(DUT).clickWhenExist(text="去听歌")
        Common(DUT).clickById("com.android.music:id/playbar_play")
        Common(DUT).clickWhenExist(text="知道了")
        Common(DUT).lockScreen()
 
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=180, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=1200, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
    def tearDown(self):
        Common(DUT).unlockScreen()
        Common(DUT).clickById("com.android.music:id/playbar_play")
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
