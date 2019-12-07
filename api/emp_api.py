# 导包
import requests

import app


class EmpApi:
    def __init__(self):
        self.add_emp_url = "http://182.92.81.159/api/sys/user"

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-11-01",
            "formOfEmployment": 2,
            "workNumber": "123321",
            "departmentName": "开发部",
            "departmentId": "1066240656856453120",
            "correctionTime": "2020-01-30T16:00:00.000Z"
        }
        return requests.post(self.add_emp_url, json=data, headers=app.HEAdERS)

    def query_emp(self):
        """查询员工接口"""
        query_emp_url = self.add_emp_url + "/" + app.EMPID
        return requests.get(query_emp_url, headers=app.HEAdERS)

    def modify_emp(self, username):
        """修改员工接口"""
        modify_emp_url = self.add_emp_url + "/" + app.EMPID
        return requests.put(modify_emp_url, json={"username": username}, headers=app.HEAdERS)

    def delete_emp(self):
        """修改员工接口"""
        delete_emp_url = self.add_emp_url + "/" + app.EMPID
        return requests.delete(delete_emp_url, headers=app.HEAdERS)


# if __name__ == '__main__':
#     test_add_emp = EmpApi()
#     add_emp = test_add_emp.add_emp("哪吒11","13133332222")
