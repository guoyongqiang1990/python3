#-*- coding:utf-8 -*-
'''
用例标题：
预置条件：
1,手机处于飞行模式
2,1，亮度调为300cd/m2
测试步骤：
1，设置亮屏超时30min
2，测试桌面亮屏时电流3分钟
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
        Common(DUT).unlockScreen()
        Common(DUT).clearRecentApp()
    def test_step(self):
        Common(DUT).setAirplaneMode("开启")
        Setting(DUT).setScreenTimeout("30min")
        Common(DUT).goBackHome()
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
    def tearDown(self):
        Common(DUT).goHome()
        Common(DUT).setAirplaneMode("关闭")

if __name__ == "__main__":
    unittest.main()
