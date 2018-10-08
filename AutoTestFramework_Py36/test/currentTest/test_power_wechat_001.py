#-*- coding:utf-8 -*-
'''
用例标题：
1.进入微信对话
2.语音输入5秒发送，等待10秒
3.重复步骤2，执行60次
4.返回待机    
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
        Common(DUT).startActivity("com.tencent.mm/.ui.LauncherUI")
        Common(DUT).clickByText("名字头像不要动")
        if Common(DUT).exists(resourceId="com.tencent.mm:id/yw"):
            Common(DUT).clickById("com.tencent.mm:id/yt")
        Common(DUT).nohupTest("PowerTestCases.jar", "testWechat")
        USB.disconnectUsb()
#         Power.sampleResult(sPath="d:\powerResult", mTime=300, delay=180, caseName=TAG)
        PM.powerMeasure(sample=100, mTime=900, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
  
    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
