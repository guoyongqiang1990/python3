#-*- coding:utf-8 -*-
from aw import *
'''
用例标题:nebpay API NRC20
测试步骤：
1.发起一笔NRC20支付。
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
        Common(DUT).goBack(4)
        Common(DUT).goHome()

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
        Common(DUT).inputText("30000")
        Common(DUT).clickById("gasPrice")
        Common(DUT).inputText("2000000")
        Common(DUT).clickById("currency")
        Common(DUT).inputText("ATP")
        Common(DUT).clickById("nrc20to")
        Common(DUT).inputText("n1JEBqmiMeVyiD6a5Qsa6eFktWV2UAFkyZz")
        Common(DUT).clickById("nrc20value")
        Common(DUT).inputText("0.000000000000000001")
        Common(DUT).clickByText("pay",index=1)
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
        Common(DUT).clickByText("pay",index=1)
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
