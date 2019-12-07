import logging
import unittest
from api.emp_api import EmpApi
import app
import pymysql
from utils import assert_common, DButils


class TestIHRMEmp(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_add_emp(self):
        # 调用 员工管理接口下的添加员工
        response = self.emp_api.add_emp("奇异博士17", "13312345644")
        logging.info("调用添加员工接口返回结果：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 10000, True, "操作成功")
        # 保存添加成功的员工id，以便后期查询员工使用
        jsonData = response.json()
        # 将员工id保存到qpp.py文件
        # 注意需要新建一个员工id到app.py文件中
        emp_id = jsonData.get('data').get('id')
        app.EMPID = emp_id
        # 打印保存到全局变量中的 员工id信息
        logging.info("保存到全局变量中的员工id为：{}".format(app.EMPID))

    def test02_query_emp(self):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 打印查询信息
        logging.info("查询员工得到的数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, 10000, True, "操作成功")

    def test03_modify_emp(self):
        # 调用 修改员工接口
        response = self.emp_api.modify_emp("黑寡妇3")
        logging.info("修改员工得到的数据：{}".format(response.json()))
        assert_common(self, response, 200, 10000, True, '操作成功')
        # 查询数据库 并断言修改的名字 跟数据库查询结构是否一致
        # 建立连接
        # conn = pymysql.connect("182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm")
        # # 获取游标
        # cursor = conn.cursor()
        # # 执行SQL语句
        # query_sql = "select username from bs_user where id={} limit1".format(app.EMPID)
        # cursor.execute(query_sql)
        # # 断言
        # result = cursor.fetchone()
        # print(result)
        # # 打印一下数据库中id为{}的username数据
        # logging.info("-----数据库中id为{}的username为：{}".format(app.EMPID,result[0]))
        # self.assertEqual("黑寡妇2", result[0])
        # # 关闭连接/游标
        # cursor.close()
        # conn.close()
        with DButils("182.92.81.159","readuser","iHRM_user_2019","ihrm") as db:
            query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()

        logging.info("------查询数据库中员工id为{}的username是：{}".format(app.EMPID,result[0]))

    def test04_delete_emp(self):
        # 调用 修改员工接口
        response = self.emp_api.delete_emp()
        logging.info("删除之后返回的数据：{}".format(response.json()))
        assert_common(self, response, 200, 10000, True, '操作成功')