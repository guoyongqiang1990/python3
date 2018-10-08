#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
测试步骤：
1.开启关闭手电筒，3分钟后测试待机电流
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
        Setting(DUT).switchAirplane("开启")
        Common(DUT).goBackHome()
    def test_step(self):
        Common(DUT).openQuicksetting()
        Common(DUT).clickByText("手电筒")
        Common(DUT).goHome()
        Common(DUT).lockScreen()
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()     
        Common(DUT).unlockScreen()
        Common(DUT).goBack()
        Common(DUT).openQuicksetting()
        Common(DUT).clickByText("手电筒")

    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
