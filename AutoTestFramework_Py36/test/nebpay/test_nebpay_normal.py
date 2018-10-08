#-*- coding:utf-8 -*-
from aw import *
'''
用例标题:nebpay API Normal
测试步骤：
1.发起一笔Normal支付。
2、查看详情
3、返回DApp
预期结果：
1.支付成功。
2、上链成功
3、返回DApp
'''

######################################             
TAG=__file__.split("\\")[-1]         
TAG = TAG.split('.')[0]              
######################################
class TestScript(unittest.TestCase):
    def setUp(self):
        Common(DUT).goHome()
        Common(DUT).clearUserData("io.nebulas.wallet.android.testnet")
        Common(DUT).startActivity("io.nebulas.wallet.android.testnet/io.nebulas.wallet.android.module.launch.LaunchActivity")
        Common(DUT).wait(3)
        Common(DUT).clickByText("我已仔细阅读并同意以上用户隐私协议及服务条款", screeScroll=True)
        Common(DUT).clickByText("继续")
        Common(DUT).clickByText("添加钱包",screeScroll=True)
        Common(DUT).clickByText("立即导入")
        Common(DUT).clickByText("私钥（不安全）")
        Common(DUT).clickByText("请输入私钥")
        Common(DUT).inputText("612e58f24af35d10a1e2a8cb462c363135fb75a41bde686fd4608743bfeb4abd",if_enter="1")
        Common(DUT).goBack(1)
        Common(DUT).clickByText("同意")
        Common(DUT).clickByText("开始导入")
        Common(DUT).inputText("000000")
        Common(DUT).clickByText("同意")
        Common(DUT).clickByText("下一步")
        Common(DUT).inputText("000000")
        Common(DUT).clickByText("确认")
        Common(DUT).clickByText("好的，我知道了")
    def test_step(self):
        Common(DUT).startActivity("io.nebulas.wallet.android.testnet/io.nebulas.wallet.android.module.launch.LaunchActivity")
        Common(DUT).wait(3)
        Common(DUT).clickByText("应用中心")
        Common(DUT).wait(3)
        Common(DUT).clickById("input-geturl")
        Common(DUT).inputText("https://yupnano.github.io/LearnGit/example.html")
        Common(DUT).clickByText("打开")
        Common(DUT).wait(3)
        Common(DUT).clickById("gasLimit")
        Common(DUT).inputText("20000")
        Common(DUT).clickById("gasPrice")
        Common(DUT).inputText("2000000")
        Common(DUT).clickById("to")
        Common(DUT).inputText("n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz")
        Common(DUT).clickById("value")
        Common(DUT).inputText("0.000000000000000001")
        Common(DUT).clickByText("pay")
        Common(DUT).clickByText("确认")
        Common(DUT).inputText("000000")
        Common(DUT).clickByText("详情")
        result = Checkpoint(DUT).checkIfExist("检测点1:收款方",text="n1awhGQjpjWya785r5ht7FYTNoVAmQAqKpb")
        self.assertEqual(result, True)
        result = Checkpoint(DUT).checkIfExist("检测点2:收款方", text="n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz")
        self.assertEqual(result, True)
        Common(DUT).wait(40)
        result = Checkpoint(DUT).checkIfNotExist("检测点3:交易状态", text="(0/15)")
        self.assertEqual(result, True)
        Common(DUT).goBack(1)
        Common(DUT).clickByText("pay")
        Common(DUT).clickByText("确认")
        Common(DUT).inputText("000000")
        Common(DUT).clickByText("返回DApp")
        result = Checkpoint(DUT).checkIfExist("4:返回", text="pay")
        self.assertEqual(result, True)

    def tearDown(self):
        Common(DUT).goBack(4)
        Common(DUT).goHome()

if __name__ == "__main__":
    unittest.main()
