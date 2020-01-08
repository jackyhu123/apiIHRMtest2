import unittest, logging
from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()

    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据
        logging.info('登录成功返回数据:{}'.format(jsonData))

        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get('success'))  # 断言success
        # self.assertEqual(10000, jsonData.get('code'))
        # self.assertIn('操作成功', jsonData.get('message'))

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login('13234345234', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号不存在时输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test03_password_is_error(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', 'error')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('密码错误时输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test04_username_have_special_char(self):
        # 调用封装的登录接口
        response = self.login_api.login('1380#$00002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('用户名有特殊字符输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test05_username_is_empty(self):
        # 调用封装的登录接口
        response = self.login_api.login('', 'error')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号为空时输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test06_password_is_empty(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('密码为空时输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test07_username_have_chinese(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800三毛002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号有中文时时输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test08_username_have_space(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800 002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号有空格时输出的数据为：{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')
