# ihrm 登录测试用例
import logging
import unittest
from api.LoginApi import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


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

    @parameterized.expand(read_login_data)
    def test_login_success(self, mobile, password, http_code, code, success, message):
        """登陆测试用例"""
        response = self.login_api.login_api(mobile, password)
        logging.info("登录接口返回数据为：{}".format(response.json()))

        assert_common(self, response, http_code, code, success, message)
