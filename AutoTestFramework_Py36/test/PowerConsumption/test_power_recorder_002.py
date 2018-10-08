#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
测试步骤：
1.录音保存后，back键退出，3分钟后测试待机电流
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
        Common(DUT).wait(5)
        Common(DUT).click_relative(0.5, 0.9)
        Common(DUT).clickById("com.android.soundrecorder:id/stop")
        Common(DUT).clickByText("保存")
        Common(DUT).goBack()
        Common(DUT).lockScreen()
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
