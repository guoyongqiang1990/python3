#-*- coding:utf-8 -*-
'''
用例标题：新建手机联系人-所有字段
测试步骤：
1.新建手机联系人；
2.填写编辑界面的所有选项，保存；
3.查看所保存联系人的各项信息。
预期结果：
2.可以正常保存（手机、账户在编辑界面点击头像可以设置大头贴，卡不可以）；
3.各项信息与填写一致。
'''
from aw import * 

######################################             
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]
add_list=["姓名拼音","即时消息","公司","地址","备注","昵称","网站","IMS通话"] 
edit_dic=["姓名:小明","姓名拼音:xm","请输入号码...:10086","即时消息:hello","请输入邮箱...:604952177@qq.com",
         "公司:金立","职务:tester","街道:中关村","邮政信箱:china","社区:启明星辰","城市:北京","邮编:065600",
         "备注:just for test","昵称:明明","网站:www.baidu.com","IMS通话:10086"]             
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
             
    def test_step(self):
        for i in range(LOOP.loop1):
            Common(DUT).clickByText("联系人",screeScroll=True,direction="left_right")
            Common(DUT).wait(1)
            Common(DUT).clickWhenExist(text="新建联系人")
#             Common(DUT).clickWhenExist(text="新建")
            Common(DUT).goBack()
            for text in add_list:
                Common(DUT).clickByText("添加更多", screeScroll=True)
                Common(DUT).clickByText(text, screeScroll=True)
             
            Common(DUT).swipeToTop()
            for j in range(16):
                item=edit_dic[j].split(":")
                key=item[0]
                value=item[1]
                Common(DUT).clickByText(key,screeScroll=True)
                Device(DUT)(text=key,className="android.widget.EditText").set_text(value)
            Common(DUT).swipeToTop()
            Common(DUT).clickById("com.android.contacts:id/frame")
            Common(DUT).clickByText("拍照")
            Common(DUT).wait(1)
            Common(DUT).clickById("com.android.camera:id/shutter_button_icon")
            Common(DUT).clickById("com.android.camera:id/review_btn_done")
            Common(DUT).clickById("com.gionee.gallery:id/crop_done")
            Common(DUT).clickByText("保存")
            result = Checkpoint(DUT).checkIfExist("检测点1",text="10086")
             
            self.assertEqual(result, True)
    def tearDown(self):
        Common(DUT).goBack()
        Common(DUT).long_clickByText("小明")
        Common(DUT).clickByText("删除联系人")
        Common(DUT).clickById("com.android.contacts:id/amigo_button1")
        Common(DUT).goHome()
        Common(DUT).clearRecentApp()

if __name__ == "__main__":
    unittest.main()
