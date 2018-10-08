#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
测试步骤：
1.普通模式，测试录音宝后台录音时电流
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
        Common(DUT).clearUserData("com.android.soundrecorder")
    def test_step(self):
        Common(DUT).startActivity("com.android.soundrecorder/.SoundRecorder")
        Common(DUT).click_relative(0.5, 0.9)
        Common(DUT).goHome()
        Common(DUT).lockScreen()
        Common(DUT).wait(5)
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
        Common(DUT).unlockScreen()
        Common(DUT).startActivity("com.android.soundrecorder/.SoundRecorder")
        Common(DUT).click_relative(0.5, 0.9)
        
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
