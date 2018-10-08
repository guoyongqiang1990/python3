#-*- coding:utf-8 -*-
'''
用例标题：无联系人时点击新建联系人
测试步骤：
1.无联系人时点击新建联系人。
预期结果：
1-1.无卡时，正常新建到手机或者账户（第一次点击才会出现）上，并正常显示在列表里；
1-2.有卡时，正常新建到手机、卡上(手机登入exchange账户会有账户选项），并正常显示在列表里（双卡项目，新建到卡1、卡2上都要测试）。
'''
from aw import * 

###################################### 
contactName="zhangsan"            
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
            Common(DUT).clickByText("新建联系人",screeScroll=True,direction="left_right")
            Common(DUT).inputText(contactName)
            Common(DUT).clickByText("请输入号码...")
            Common(DUT).inputText("10086")
            Common(DUT).clickByText("保存")
            Common(DUT).goBack()
        
            result = Checkpoint(DUT).checkIfExist("检测点1",text=contactName)
            self.assertEqual(result, True)
            
    def tearDown(self):
        Common(DUT).long_clickByText(contactName)
        Common(DUT).clickByText("删除联系人")
        Common(DUT).clickById("com.android.contacts:id/amigo_button1")
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
