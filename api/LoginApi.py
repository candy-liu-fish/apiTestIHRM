# ihrm登录接口
import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login_api(self, mobile, password):
        login_data = {
            "mobile": mobile,
            "password": password
        }
        return requests.post(self.login_url, json=login_data, headers={"Content-Type": "application/json"})

    def login_no_params(self):
        return requests.post(self.login_url, headers={"Content-Type": "application/json"})

    def login_extra_params(self):
        return requests.post(self.login_url, json={"mobile": "13800000002", "password": "123456", "extra": "测试多参"}, headers={"Content-Type": "application/json"})

    def login_less_params(self):
        return requests.post(self.login_url, json={"password": "123456"}, headers={"Content-Type": "application/json"})
