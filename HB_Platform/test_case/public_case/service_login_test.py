# coding=utf-8
import sys
import unittest
import time
from HB_Platform.test_case.page_obj.LoginPage import Login
from HB_Platform.test_case.models import myunit, screen_func

sys.path.append("./models")
sys.path.append("./page_obj")


class TestServiceLogin(myunit.MyTest):
    # 测试用户登录
    def user_login_verification(self, username, password):
        Login(self.driver).user_login(username, password)

    def test_login(self, username="admin1", password="admin1"):
        """用户名、密码错误"""
        try:
            self.user_login_verification(username, password)
            time.sleep(3)
            self.assertEqual(Login(self.driver).verification_info(), "用户名密码错误!")
        except Exception as msg:
            screen_func.take_screen_shot(self.driver, "用户名密码错误.png")
            return u"异常原因:%s" % msg


if __name__ == '__main__':
    unittest.main()
