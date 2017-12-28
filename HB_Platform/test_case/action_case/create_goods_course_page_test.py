# coding=utf-8
# import unittest
# from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from HB_Platform.test_case.public_case import enter_goods_list
from HB_Platform.test_case.page_obj.CreateGoodsCoursePage import CreateCourse


# class TestServiceCreateVirtualGoods(unittest.test_case):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def tearDown(self):
#         pass


# @unittest.skip(u"强制跳过虚拟商品列表")
def test_create_virtual_goods_page(self):
    # 进入虚拟商品列表
    enter_goods_list(self)
    # CreateCourse实例化
    driver = self.driver
    base_url = 'http://111.203.248.61:8001/'
    self.AddNewCourse=CreateCourse(driver, base_url, action=ActionChains, select=Select, page_title='')
    # 新增课程
    self.AddNewCourse.click_add_course_process()
    # 添写基本信息
    self.AddNewCourse.type_basic_info()
