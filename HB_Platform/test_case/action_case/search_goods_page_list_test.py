# coding=utf-8
import unittest

from test_case.action_public.click_goods_list_test import enter_goods_list

from HB_Platform.test_case.page_obj.VirtualGoodsSearchPage import EnterSearchPage


# class TestServiceSearchGoods(unittest.test_case):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.base_url = 'http://111.203.248.61:8001/ResourceInfoVirtual/Index'
#
#     def tearDown(self):
#         pass
# @unittest.skip(u"强制跳过搜索产品页列表")
def test_search_goods_page_list(self):
        """测试搜索产品页列表"""
        # 登录
        # service_login_test.test_login(self)
        # 点击虚拟商品列表
        enter_goods_list(self)
        # EnterSearchPage实例化
        driver=self.driver
        base_url = 'http://111.203.248.61:8001/ResourceInfoVirtual/Index'
        SearchPage = EnterSearchPage(driver, base_url)
        # 点击搜索按钮
        SearchPage.click_search_btn()
        # print'点击搜索按钮'
        # 弹出的表单中输入产品ID
        SearchPage.type_input_goods_id()
        # print'弹出的表单中输入产品ID'
        # 点击表单搜索按钮
        SearchPage.click_form_search_btn()
        # print'点击表单搜索按钮'


if __name__ == '__main__':
        unittest.main()


