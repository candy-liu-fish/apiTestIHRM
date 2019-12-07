# 执行测试套件 生成测试报告
# 导包
import time
import unittest, app
from script.test_ihrm_emp import TestIHRMEmp
from script.test_ihrm_login import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner

# 实例化测试套件
suite = unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmp))

# 设置测试报告路径和名称
report_file = app.BASE_DIR + "/report/ihrm_report.html"
with open(report_file, "wb") as f:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=f, title="ihrm项目登录接口测试报告", description="基于Windows10测试登录接口和员工管理模块",verbosity=1)
    # 使用runner 实行测试套件
    runner.run(suite)
