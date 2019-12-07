# ihrm 登录测试用例
import logging,app
import unittest
from api.LoginApi import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        """登录成功"""
        response = self.login_api.login_api("13800000002", "123456")
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # # 断言 http 响应状态码
        # self.assertEqual(200,response.status_code)
        # # 断言code的值
        # self.assertEqual(10000,response.json().get("code"))
        # # 断言success的值
        # self.assertEqual(True,response.json().get("success"))
        # # 断言 message的值
        # self.assertIn("操作成功",response.json().get("message"))

        assert_common(self, response, 200, 10000, True, "操作成功")
        # 获取登录成功之后的token值
        jsonData = response.json()
        # 将 jsonData中的的data值拼接为token值Bearer xxx 保存到全局变量中
        token = "Bearer " + jsonData.get('data')
        app.HEAdERS = {"Content-Type": "application/json", "Authorization": token}
        logging.info("保存的登录的请求头信息：{}".format(app.HEAdERS))   # 必须用占位符才能够打印日志信息



    def test02_login_failure(self):
        response = self.login_api.login_api("13900000002", "123456")
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 20001, False, "用户名或密码错误")

    def test03_password_error(self):
        response = self.login_api.login_api("13800000002", "error")
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 20001, False, "用户名或密码错误")

    def test04_none_params(self):
        response = self.login_api.login_no_params()
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 99999, False, "抱歉，系统繁忙")

    # 测试账号为空
    def test05_mobile_none(self):
        response = self.login_api.login_api("", "123456")
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 20001, False, "用户名或密码错误")

    # 测试密码为空
    def test06_password_none(self):
        response = self.login_api.login_api("13900000002", "")
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 20001, False, "用户名或密码错误")

    # 测试多参
    def test07_more_params(self):
        response = self.login_api.login_extra_params()
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 10000, True, "操作成功")

    # 测试少参
    def test08_less_params(self):
        response = self.login_api.login_less_params()
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 20001, False, "用户名或密码错误")