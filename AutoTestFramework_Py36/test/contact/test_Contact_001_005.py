#-*- coding:utf-8 -*-
'''
用例标题:信息选择收件人时进入联系人界面
测试步骤：
1.信息选择收件人时进入联系人界面。
预期结果：
1.可正常进入到联系人。
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
        Common(DUT).clickByText("信息",screeScroll=True,direction="left_right")
        Common(DUT).clickByText("新信息")
        Common(DUT).clickById("com.android.mms:id/pick_contacts")
        Common(DUT).clickByText("联系人")
        
        Common(DUT).wait(1)
        result = Checkpoint(DUT).checkIfExist("检测点1",text="没有任何联系人")
        self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).goBack(1)
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
