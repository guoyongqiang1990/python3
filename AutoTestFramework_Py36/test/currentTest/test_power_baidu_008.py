#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入百度首页，点击新闻
2.判断刷新按钮，上限5次
3.每10s向上滑动并刷新一次
4.重复2、3步66次
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
        Common(DUT).startActivity("com.baidu.searchbox/.MainActivity")
        Common(DUT).clickByText("新闻")
        Common(DUT).wait(2)

        Common(DUT).nohupTest("PowerTestCases.jar", "testBaidu")
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=180, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=660, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
 
    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
