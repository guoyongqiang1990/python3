#-*- coding:utf-8 -*-
'''
用例标题:从近期任务进入联系人
测试步骤：
1.点击menu键，从近期任务进入联系人。
预期结果：
1.正常进入联系人。

'''
from aw import * 

######################################             
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
    def test_step(self):
        Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")
        Common(DUT).goHome()
        Common(DUT).pressRecent()
        Common(DUT).wait(1)
        Common(DUT).click(131,1204)
        Common(DUT).wait(1)
        result = Checkpoint(DUT).checkIfExist("检测点1",text="新建联系人")
        self.assertEqual(result, True)          
    def tearDown(self):
        Common(DUT).goBack(1)
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()
if __name__ == "__main__":
    unittest.main()
