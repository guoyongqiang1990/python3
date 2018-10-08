#-*- coding:utf-8 -*-
'''
用例标题：
预置条件：
1，开启飞行模式
测试步骤：
1，设置菜单默认状态下，home键退出设置
2,等待手机灭屏3分钟后，测试待机电流3分钟
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
        Setting(DUT).switchAirplane("开启")
    def test_step(self):
        Common(DUT).launchSettings()
        Common(DUT).goHome()
        Common(DUT).lockScreen()
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
        Common(DUT).unlockScreen()
    def tearDown(self):
        Common(DUT).goHome()
#         Common(DUT).setAirplaneMode("关闭")

if __name__ == "__main__":
    unittest.main()
