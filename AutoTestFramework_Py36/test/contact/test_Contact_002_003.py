#-*- coding:utf-8 -*-
'''
用例标题：无联系人时点击导入联系人
测试步骤：
1.无联系人时点击导入联系人；
2.从账户导入；
3.从SD卡导入；
4.从内部存储器导入。
预期结果：
正常导入联系人，并正常显示在列表里。
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
