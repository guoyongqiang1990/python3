#-*- coding:utf-8 -*-
from aw import * 
'''
用例标题:云盘里选择一文件用邮件分享时点击添加联系人按钮
测试步骤：
1.云盘里选择一文件用邮件分享时点击添加联系人按钮 (根据项目看是否配置才有）。
预期结果：
1.可正常进入到联系人。
'''

######################################             
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
    def test_step(self):
        Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")

        result = Checkpoint(DUT).checkIfExist("检测点1",text="新建联系人")
        self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).goBack(1)
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
