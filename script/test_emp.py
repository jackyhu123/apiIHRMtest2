import logging
import unittest
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, read_update_emp_data, read_delete_emp_data
import app
from parameterized import parameterized
import pymysql


class TestIHRMEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.emp_api = EmpApi()

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        response = self.emp_api.add_emp(username, mobile)
        jsonDate = response.json()
        logging.info('添加员工接口返回数据为：{}'.format(jsonDate))
        assert_common(self, response, http_code, success, code, message)

        # 获取员工ID保存在全局变量
        app.EMP_ID = jsonDate.get('data').get('id')
        logging.info('员工ID为：{}'.format(app.EMP_ID))

    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self, success, code, message, http_code):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        jsonData = response.json()
        logging.info('查询员工接口返回数据{}'.format(jsonData))
        #         断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_update_emp_data)
    def test03_update_emp(self, username, success, code, message, http_code):
        response = self.emp_api.update_emp(username)
        jsonData = response.json()
        logging.info('修改员工接口返回数据{}'.format(jsonData))
        # # 建立数据库连接一
        # # with DBUtils()as db_utils:
        # #     sql = 'select username from bs_user where id={}'.format(app.EMP_ID)
        # #     db_utils.execute(sql)
        # #     result = db_utils.fetchone()[0]
        # #     logging.info('从数据库中查询出的员工用户名是：{}'.format(result))
        # # 建立数据库连接二
        # conn = pymysql.connect('182.92.82.159','readuser','iHRM_user_2019','ihrm')
        # # 获取游标
        # cursor = conn.cursor()
        # sql = "select username from bs_user where id ={}".format(app.EMP_ID)
        # cursor.execute(sql)
        # # 获取呢执行结果
        # result = cursor.fetchone()[0]
        # logging.info('从数据库中查询出的员工用户名是：{}'.format(result))
        # self.assertEqual(username,result)
        # cursor.close()
        # conn.close()
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self, success, code, message, http_code):
        response = self.emp_api.delete_emp()
        jsonData = response.json()
        logging.info('删除员工接口返回数据{}'.format(jsonData))
        assert_common(self, response, http_code, success, code, message)
