#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.病毒查杀，back键退出，3分钟后测试待机电流
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
        Common(DUT).clearUserData("com.gionee.softmanager")
    def test_step(self):
        Common(DUT).startActivity("com.gionee.softmanager/.MainActivity")
        Common(DUT).clickByText("病毒查杀")
        Common(DUT).clickByText("快速扫描")
        Common(DUT).wait(5)
        Common(DUT).clickByText("完成")
        Common(DUT).goBack(2)
        result = Checkpoint(DUT).checkIfExist("检测点1",text="联系人") 
        self.assertEqual(result, True)
        Common(DUT).lockScreen()
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=300, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=180, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[180], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
        Common(DUT).unlockScreen()
        
    def tearDown(self):
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
