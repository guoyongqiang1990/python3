#-*- coding:utf-8 -*-
'''
用例标题:退出联系人
测试步骤：
1.联系人界面按back键。
2.联系人界面按home键。
预期结果：
1.正常退出联系人。
2.正常退出联系人。
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
        Common(DUT).goHome()
        Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")
        Common(DUT).goBack(1)
        result = Checkpoint(DUT).checkIfExist("检测点1",text="新建联系人")
        self.assertEqual(result, True)
        Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")
        Common(DUT).goHome()
        result = Checkpoint(DUT).checkIfExist("检测点2",text="新建联系人")
        self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).goBack(1)
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
