import json

import pymysql
from requests import Response

# 封装通用断言
import app


def assert_common(self, response, status_code, code, success, message):
    """
    @type response:Response
    前一个response 是参数，后一个Response是对象，想要那个产生提示信息，就可以写入那个对象，前提是requests库有封装的对象
    """
    # 三引号注释里边的内容，可以再写代码时产生提示信息
    jsonData = response.json()  # type:dict
    self.assertEqual(status_code, response.status_code)
    # 断言code的值
    self.assertEqual(code, jsonData.get("code"))
    # 断言success的值
    self.assertEqual(success, jsonData.get("success"))
    # 断言 message的值
    self.assertIn(message, jsonData.get("message"))


class DButils:

    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host, user, password, database)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    # enter和exit 这两个魔法函数，是python内置函数，在使用with语法打卡文件对象时，要执行的函数，
    # 执行顺序：with打开时，执行enter函数，退出with时执行exit函数
    #  with open（filename，mode=‘r'）as f： pass
    # 引用 with DButils（） as db： db execute（）


def read_login_data():
    """读取json中的数据实现 参数化"""
    read_data_path = app.BASE_DIR + "/data/login_data.json"
    print(read_data_path)
    with open(read_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            mobile = login_data.get('mobile')
            password = login_data.get('password')
            http_code = login_data.get('http_code')
            code = login_data.get('code')
            success = login_data.get('success')
            message = login_data.get('message')
            result_list.append((mobile, password, http_code, code, success, message))
    print("读取的数据为：", format(result_list))
    return result_list


def read_add_emp_data():
    add_emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(add_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        add_list = []
        add_emp_data = jsonData.get('add_emp')
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        http_code = add_emp_data.get('http_code')
        code = add_emp_data.get('code')
        success = add_emp_data.get('success')
        message = add_emp_data.get('message')
        add_list.append((username, mobile, http_code, code, success, message))
    print("add_list的值是：", add_list)
    return add_list


def read_query_emp_data():
    query_emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(query_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        query_list = []
        query_emp_data = jsonData.get('query_emp')
        http_code = query_emp_data.get('http_code')
        code = query_emp_data.get('code')
        success = query_emp_data.get('success')
        message = query_emp_data.get('message')
        query_list.append((http_code, code, success, message))
    print("query_list的值是：", query_list)
    return query_list


def read_modify_emp_data():
    modify_emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(modify_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        modify_list = []
        modify_emp_data = jsonData.get('modify_emp')
        username = modify_emp_data.get('username')
        http_code = modify_emp_data.get('http_code')
        code = modify_emp_data.get('code')
        success = modify_emp_data.get('success')
        message = modify_emp_data.get('message')
        modify_list.append((username, http_code, code, success, message))
    print("add_list的值是：", modify_list)
    return modify_list


def read_delete_emp_data():
    delete_emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(delete_emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        delete_list = []
        delete_emp_data = jsonData.get('query_emp')
        http_code = delete_emp_data.get('http_code')
        code = delete_emp_data.get('code')
        success = delete_emp_data.get('success')
        message = delete_emp_data.get('message')
        delete_list.append((http_code, code, success, message))
    print("query_list的值是：", delete_list)
    return delete_list


if __name__ == '__main__':
    read_query_emp_data()
