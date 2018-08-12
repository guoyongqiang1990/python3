import unittest
from ceshi_test_location import *
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':

    suite=unittest.TestSuite()        #定义一个单元测试容器
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))  # 用testloader加载测试用例
    suite.addTest(AppMainPage("test_location"))  #将测试用例加入到测试容器中

    #filename="./myAppiumLog.html"        #定义个报告存放路径，支持相对路径。  路径格式待研究


    with open('myAppiumLog.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='AppLocation Test Report',
                                description='Report_description.',
                                verbosity=2
                                )
        runner.run(suite)