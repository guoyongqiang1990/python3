#-*- coding:utf-8 -*-
'''
用例标题：
前提条件：
测试步骤：
1.测试亮屏使用指南针时电流
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
    def test_step(self):
        Common(DUT).startActivity("jlzn.com.android.compass/.JLZN_CompassActivity")
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=CONST.POWER.delay[180], caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()   
        
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()