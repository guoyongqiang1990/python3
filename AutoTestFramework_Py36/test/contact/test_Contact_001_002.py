#-*- coding:utf-8 -*-
from aw import * 
'''
用例标题:从拨号盘点击联系人图标
测试步骤：
1.从拨号盘点击联系人图标。
预期结果：
1.正常进入联系人。
'''

######################################             
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
    def test_step(self):

        Common(DUT).clickByText("拨号",screeScroll=True,direction="left_right")
        Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")
        Common(DUT).wait(1)
        result = Checkpoint(DUT).checkIfExist("检测点1",text="新建联系人")
        self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
