# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from HB_Platform.test_case.page_obj.base import Page


class Login(Page):
    username_loc = (By.ID, 'UserName')
    password_loc = (By.ID, 'Password')
    login_btn_loc = (By.CSS_SELECTOR, '.btn.btn-success')
    head_url = u'http://betacloud.eeduol.com/AdminCommon'
    hao_ban_url = head_url + u'/LogOn?returnUrl=http%3A%2F%2Fbetacloud.eeduol.com%2F'

    def __init__(self, driver, action=ActionChains,
                 select=Select, page_title='', base_url=hao_ban_url):
        Page.__init__(self, driver, action, select, page_title, base_url)

    def open_url(self):
        self.open()

    # 输入用户名
    def type_input_username(self, username):
        try:
            self.type_input(self.username_loc, username)
        except Exception as msg:
            return u"异常原因%s" % msg

    # 输入密码
    def type_input_password(self, password):
        try:
            self.type_input(self.password_loc, password)
        except Exception as msg:
            return u"异常原因%s" % msg

    # 点击登录按钮
    def click_login_btn(self):
        try:
            self.click(self.login_btn_loc)
        except Exception as msg:
            return u"异常原因%s" % msg

    # 定义统一登录入口
    def user_login(self, username, password):
        self.open_url()
        self.type_input_username(username)
        self.type_input_password(password)
        self.click_login_btn()

    validation_summary_errors = (By.CSS_SELECTOR, ".validation-summary-errors>ul>li")

    # 验证信息
    def verification_info(self):
        """错误验证信息"""
        return self.find_layer(self.validation_summary_errors)

