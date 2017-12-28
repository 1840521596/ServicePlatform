# coding=utf-8
import sys

from HB_Platform.test_case.page_obj.VirtualGoodsSearchPage import EnterSearchPage

reload(sys).setdefaultencoding('utf-8')


# class TestServiceCreateVirtualGoods(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def tearDown(self):
#         pass

def enter_goods_list(self):
    """进入虚拟商品列表"""
    driver = self.driver
    base_url = 'http://111.203.248.61:8001/ResourceInfoVirtual/Index'
    SearchPage = EnterSearchPage(driver, base_url)
    # 点击电商服务
    SearchPage.click_ec_service()
    # print'点击电商服务'
    # 点击商品管理
    SearchPage.click_goods_manager()
    # print'点击商品管理'
    # 点击虚拟商品列表
    SearchPage.click_virtual_goods_list()
    # print'点击虚拟商品列表'
    # print'打印虚拟商品链接：', base_url