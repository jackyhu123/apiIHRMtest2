import unittest
import app
import time
from script.login import Login
from tools.HTMLTestRunner import HTMLTestRunner
from script.test_emp import TestIHRMEmp
# 初始化测试套件
suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))

# 生成测试报告路径和名称
# os.path.dirname(os.path.abspath(__file__))的意思是获取当前执行文件的父级的目录
report_path =app.BASE_DIR + '/report/IHRMLogin.html'
# 打开测试报告文件，初始化HTMLTestRunner，执行测试套件，生成测试报告
with open(report_path, mode='wb') as f:
    runner = HTMLTestRunner(f, verbosity=1, title='IHRM人力资源登录接口测试', description='V1.0.0')
    # 使用初始化的runner实例运行测试套件生成测试报告
    runner.run(suite)
