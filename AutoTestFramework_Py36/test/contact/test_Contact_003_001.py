#-*- coding:utf-8 -*-
'''
用例标题：点击新建联系人
测试步骤：
1.点击新建联系人。
预期结果：
1.输入法自动弹出，编辑界面显示正常
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
        for i in range(LOOP.loop1):
            Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")
            Common(DUT).wait(1)
            Common(DUT).clickByText("新建联系人")
        
            result = Checkpoint(DUT).checkIfNotExist("检测点1",text="添加更多") \
            and Checkpoint(DUT).checkIfExist("检测点2",text="保存")
            self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).goBack(1)
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
