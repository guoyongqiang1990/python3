#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入阅读app
2.打开书架中第一本书
3.每隔30秒翻一页
4.重复步骤3，执行100次（分5次检查黑屏）
5.返回待机
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
        Common(DUT).clickByText("阅读", screeScroll=True, direction="left_right")
#         Common(DUT).startActivity("com.chaozh.iReaderGionee/com.zhangyue.iReader.bookshelf.ui.ActivityBookShelf")
        Common(DUT).wait(5)
        Common(DUT).click(189,704)

        Common(DUT).nohupTest("PowerTestCases.jar", "testReader")
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=180, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=600, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    

    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
