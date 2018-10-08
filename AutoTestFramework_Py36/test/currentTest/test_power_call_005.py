#-*- coding:utf-8 -*-
'''
用例标题：
测试步骤：
1.进入拨号盘
2.输入10086
3.验证输入正确性
4-1.输入错误，长按删除，加一次循环，继续
4-2.输入正确，通话30s后解锁挂断，等待10s
4.重复步骤2至步骤4，执行15次
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
        Common(DUT).startActivity("com.android.contacts/.activities.PeopleActivity")
        Common(DUT).clickByText("拨号")

        Common(DUT).nohupTest("PowerTestCases.jar", "testCall")
        USB.disconnectUsb()
        PM.powerMeasure(sample=100, mTime=520, Vout=CONST.POWER.Vout, delay=CONST.POWER.delay[60], caseName=TAG, tPath=CONST.POWER.tPath)
        USB.connectUsb()    
        Common(DUT).unlockScreen()
        Common(DUT).clickWhenExist(resourceId="com.android.incallui:id/endButton")
    def tearDown(self):
        Common(DUT).wait(10)
        Common(DUT).goBackHome()

if __name__ == "__main__":
    unittest.main()
