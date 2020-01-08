import pymysql

import app
import json


# 断言函数
def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))  # 断言success
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(message, response.json().get('message'))


def read_login_data():
    p_list = list()
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, mode='r', encoding='utf-8') as f:
        # 加载文件为json格式的数据
        jsonData = json.load(f)
        for data in jsonData:
            # 遍历文件取出其中的数据并保存到列表中中
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append((mobile,
                           password,
                           http_code,
                           success,
                           code,
                           message)
                          )
    print(p_list)
    return p_list


def read_add_emp_data():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)

        add_emp_data = jsonData.get('add_emp')
        result_list = []
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')
        http_code = add_emp_data.get('http_code')
        result_list.append((username, mobile, success, code, message, http_code))

    print("读取添加员工的数据", result_list)
    return result_list


def read_query_emp_data():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)

        query_emp_data = jsonData.get('query_emp')
        result_list = []
        success = query_emp_data.get('success')
        code = query_emp_data.get('code')
        message = query_emp_data.get('message')
        http_code = query_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))

    print("查询员工的数据", result_list)
    return result_list


def read_update_emp_data():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)

        update_emp_data = jsonData.get('update_emp')
        result_list = []
        username = update_emp_data.get('username')
        success = update_emp_data.get('success')
        code = update_emp_data.get('code')
        message = update_emp_data.get('message')
        http_code = update_emp_data.get('http_code')
        result_list.append((username, success, code, message, http_code))
    print("修改员工的数据", result_list)
    return result_list


def read_delete_emp_data():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)

        delete_emp_data = jsonData.get('delete_emp')
        result_list = []
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')
        http_code = delete_emp_data.get('http_code')
        result_list.append((success, code, message, http_code))
    print("删除员工的数据", result_list)
    return result_list

class DBUtils:
    def __init__(self,host='182.92.81.159',user='readuser',password='iHRM_user_2019',database='ihrm'):
        self.host=host
        self.user=user
        self.password =password
        self.database=database

    def __enter__(self):
        self.conn =pymysql.connect(self.host,self.user,self.password,self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()






if __name__ == '__main__':
    read_delete_emp_data()
