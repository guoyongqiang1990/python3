#-*- coding:utf-8 -*-
'''
用例标题：检查联系人界面显示
测试步骤：
1.无联系人时检查界面显示；
预期结果：
1.显示新建联系人，导入联系人，从云端导入，其他手机导入四个选项；
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
        
            result = Checkpoint(DUT).checkIfExist("检测点1",text="扫名片") \
            and Checkpoint(DUT).checkIfExist("检测点2",text="新建联系人")\
            and Checkpoint(DUT).checkIfExist("检测点3",text="导入联系人") \
            and Checkpoint(DUT).checkIfExist("检测点4",text="扫二维码")
            self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).goBack(1)
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
