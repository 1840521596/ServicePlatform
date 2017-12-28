# coding=utf-8
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from HB_Platform.test_case.page_obj import Page


class CreateCourse(Page):
    """创建虚拟课程"""
    # 商品列表新增课程按钮元素集
    virtual_add_course_loc = (By.LINK_TEXT, u'新增课程')
    virtual_add_course_url = 'http://111.203.248.61:8001/VirtualResource/AddResource?Classification=200'
    virtual_list_div_loc = (By.CLASS_NAME, u'panel-body')

    def __init__(self, driver, base_url, action=ActionChains, select=Select, page_title=None):
        Page.__init__(self, driver, base_url, action, select, page_title)

    # 商品列表新增课程功能测试
    # 点击新增课程按钮
    def click_add_course_process(self):
        # print '打印当前窗口的链接：', self.virtual_add_course_url
        self.find_element_layers(self.virtual_list_div_loc)
        time.sleep(1)
        self.click(self.virtual_add_course_loc)
        time.sleep(5)
        self.switch_to_window()
        # text = self.driver.title
        # print'此页面为：', text

    # 商品列表填写基本信息元素集
    virtual_manufacture_id = (By.ID, 'ManufacturerID')
    virtual_manufacture_value = u'清大自营'
    virtual_resource_title = (By.NAME, 'ResourceTitle')
    virtual_resource_text = u'清大自营产品_英语课程'
    virtual_type_id = (By.NAME, 'TypeID')
    virtual_type_value = u'虚拟商品'
    virtual_recommend_name = (By.NAME, 'Recommend')
    virtual_recommend_text = u'好，很好，非常好'
    virtual_manufacture_description = (By.ID, 'description')
    virtual_manufacture_text = u'清大课程值得信赖'
    virtual_ApplicablePeople_id = (By.ID, 'ApplicablePeople')
    virtual_ApplicablePeople_text = u'学生'
    virtual_unit_id = (By.ID, 'unit')
    virtual_unit_value = u'人'
    virtual_KeyWord_name = (By.NAME, 'KeyWord')
    virtual_KeyWord_text = u'人次'
    virtual_add_attr_btn = (By.XPATH, ".//*[@id='baseForm']/div[10]/div/input")
    virtual_attr_name = (By.ID, 'attrName')
    virtual_attr_text = u'课程自选型'
    virtual_add_attr_table = (By.ID, 'addAttrTable')
    virtual_attr_value01 = (By.ID, 'attrValue01')
    virtual_attr_value_text01 = u'语法课程'
    virtual_attr_value02 = (By.XPATH, ".//*[@id='attrTable']/tbody/tr[3]/td[2]/input")
    virtual_attr_value_text02 = u'读写'
    virtual_attrMome = (By.ID, 'attrMome')
    virtual_attrMome_text = u'读写课程'
    virtual_submit_attr_btn = (By.ID, 'submitattr')
    virtual_click_tip_btn = (By.XPATH, 'html/body/div[7]/div/div/div[3]/button')
    virtual_click_close_btn = (By.XPATH, ".//*[@id='attrForm']/div[2]/button[2]")
    virtual_attrID_name = (By.NAME, 'AttrID')
    virtual_attrID_value = u'课程自选型'
    virtual_attr_value = (By.ID, 'attrValue')
    virtual_attr_value_type_checkboxes = (By.CSS_SELECTOR, 'input[type=checkbox]')
    virtual_confirm_att_value = (By.XPATH, ".//*[@id='subbtn']")
    virtual_table_filed = (By.ID, 'tbfield')
    virtual_table_filed_type_checkboxes = (By.CSS_SELECTOR, 'input[type=checkbox]')
    virtual_submit_btn = (By.ID, 'submit')
    virtual_save_submit_btn = (By.ID, 'savasubmit')
    virtual_return_list_btn = (By.ID, 'returnList')

    # 添写基本信息
    def type_basic_info(self):
        self.select_options(self.virtual_manufacture_id, self.virtual_manufacture_value)
        time.sleep(1)
        self.type_input(self.virtual_resource_title, self.virtual_resource_text)
        time.sleep(1)
        self.select_options(self.virtual_type_id, self.virtual_type_value)
        time.sleep(1)
        self.type_input(self.virtual_recommend_name, self.virtual_recommend_text)
        self.type_input(self.virtual_manufacture_description, self.virtual_manufacture_text)
        self.type_input(self.virtual_ApplicablePeople_id, self.virtual_ApplicablePeople_text)
        time.sleep(1)
        self.select_options(self.virtual_unit_id, self.virtual_unit_value)
        time.sleep(2)
        self.type_input(self.virtual_KeyWord_name, self.virtual_KeyWord_text)
        time.sleep(1)
        self.click(self.virtual_add_attr_btn)
        time.sleep(1)
        self.type_input(self.virtual_attr_name, self.virtual_attr_text)
        self.click(self.virtual_add_attr_table)
        time.sleep(1)
        self.type_input(self.virtual_attr_value01, self.virtual_attr_value_text01)
        time.sleep(1)
        self.type_input(self.virtual_attr_value02, self.virtual_attr_value_text02)
        time.sleep(1)
        self.type_input(self.virtual_attrMome, self.virtual_attrMome_text)
        time.sleep(1)
        self.click(self.virtual_submit_attr_btn)
        time.sleep(1)
        # result = EC.alert_is_present()(self.driver)
        # if result:
        #     # print result.text
        #     result.accept()
        # alert = self.driver.switch_to_alert()
        # alert.accept()
        self.click(self.virtual_click_tip_btn)
        time.sleep(1)
        self.click(self.virtual_click_close_btn)
        time.sleep(1)
        self.select_options(self.virtual_attrID_name, self.virtual_attrID_value)
        time.sleep(3)
        # 点击属性值复选框
        self.find_element_layers(self.virtual_attr_value)
        time.sleep(1)
        self.click_checkboxes(self.virtual_attr_value_type_checkboxes)
        time.sleep(1)
        self.click(self.virtual_confirm_att_value)
        # 点击表字段复选框
        self.find_element_layers(self.virtual_table_filed)
        time.sleep(1)
        self.click_checkboxes(self.virtual_table_filed_type_checkboxes)
        time.sleep(1)
        self.click(self.virtual_submit_btn)
        time.sleep(0.5)
        self.click(self.virtual_save_submit_btn)
        self.click(self.virtual_click_tip_btn)
        self.click(self.virtual_return_list_btn)

        # 商品列表填写价格和主题图元素集
        # def type_price_mainPicture_info(self):
        #     self.click(self.virtual_list_search_btn_loc)
        #     time.sleep(1)
