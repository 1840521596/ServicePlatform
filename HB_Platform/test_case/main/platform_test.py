# coding=utf-8
import sys
import unittest

from selenium import webdriver
from test_case.action_public import service_login_test
from test_case.action_public import service_quit_test

from HB_Platform.test_case.action import test_create_virtual_goods_page
from HB_Platform.test_case.action import test_search_goods_page_list

reload(sys).setdefaultencoding('utf-8')


class ServicePlatform(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip(u"强制跳过搜索产品页列表")
    def test_search_platform(self):
        service_login_test.test_login(self)
        test_search_goods_page_list(self)
        service_quit_test.test_quit(self)

    @unittest.skip(u"强制跳过创建虚拟商品列表")
    def test_create_virtual_course(self):
        service_login_test.test_login(self)
        test_create_virtual_goods_page(self)
        service_quit_test.test_quit(self)

if __name__ == '__main__':
    unittest.main()
