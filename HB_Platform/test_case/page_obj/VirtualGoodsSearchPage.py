# coding=utf-8
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from HB_Platform.test_case.page_obj import Page


class EnterSearchPage(Page):
    # 菜单导航电商服务元素集
    menu_div_loc = (By.CLASS_NAME, u'panel-body')
    menu_ec_link_text = (By.LINK_TEXT, u'电商服务')
    menu_ul_loc = (By.CLASS_NAME, u'dropdown-menu')
    menu_goods_manager_link = (By.LINK_TEXT, u'商品管理')
    menu_ul1_loc = (By.CLASS_NAME, u'dropdown-menu')
    menu_virtual_goods_list = (By.LINK_TEXT, u'虚拟商品列表')
    menu_virtual_url = 'http://111.203.248.61:8001/ResourceInfoVirtual/Index'
    # 图片名称加时间戳
    nowTime = time.strftime("%Y-%m-%d %H_%M_%S")
    dir_path = "C:\Python27\Scripts\ServicePlatform\Page2\error_pic\error_" \
               + nowTime + '.jpg'

    def __init__(self, driver, base_url, action=ActionChains, select=Select, page_title=None):
        Page.__init__(self, driver, base_url, action, select, page_title)

    # 菜单导航_电商服务_执行步骤
    # 点击电商服务
    def click_ec_service(self):
        try:
            self.find_element_layers(self.menu_div_loc)
            self.click(self.menu_ec_link_text)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"异常原因%s" % msg

    # 点击商品管理
    def click_goods_manager(self):
        try:
            # self.move_to_element(self.menu_ul_loc)
            self.click(self.menu_goods_manager_link)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"异常原因%s" % msg

    # 点击虚拟商品列表
    def click_virtual_goods_list(self):
        try:
            # self.move_to_element(self.menu_ul1_loc)
            self.click(self.menu_virtual_goods_list)
            self.driver.get(self.menu_virtual_url)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"异常原因%s" % msg

    # 商品列表搜索功能元素集
    # virtual_list_div_loc = (By.CLASS_NAME, u'panel-body')
    virtual_list_search_btn_link_text = (By.LINK_TEXT, u'搜索')
    virtual_list_searchForm_loc = (By.ID, u'searchForm')
    virtual_list_goods_id_loc = (By.ID, u'ResourceID')
    virtual_list_goods_id_text = '103606'
    virtual_list_search_btn_loc = (By.ID, u'btnSubmit')

    # 商品列表搜索功能测试
    # 点击搜索按钮
    def click_search_btn(self):
        try:
            # self.find_element_layers(self.virtual_list_div_loc)
            self.click(self.virtual_list_search_btn_link_text)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"异常原因%s" % msg

    # 弹出的表单中输入产品ID
    def type_input_goods_id(self):
        try:
            self.find_element_layers(self.virtual_list_searchForm_loc)
            self.type_input(self.virtual_list_goods_id_loc, self.virtual_list_goods_id_text)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"异常原因%s" % msg

    # 点击表单搜索按钮
    def click_form_search_btn(self):
        try:
            self.click(self.virtual_list_search_btn_loc)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"异常原因%s" % msg

