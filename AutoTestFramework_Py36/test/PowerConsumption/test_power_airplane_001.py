#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.开启飞行模式，3分钟后测试待机电流
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
        Common(DUT).lockScreen()
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
        Common(DUT).unlockScreen()
    def tearDown(self):
        Common(DUT).goHome()
#         Common(DUT).setAirplaneMode("关闭")

if __name__ == "__main__":
    unittest.main()
