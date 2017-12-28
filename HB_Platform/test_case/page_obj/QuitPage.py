# coding=utf-8
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from HB_Platform.test_case.page_obj import Page


class QuitPage(Page):
    base_url = 'http://111.203.248.61:8001/'
    quit_button = (By.LINK_TEXT, '登出')
    # 图片名称可以加个时间戳
    nowTime = time.strftime("%Y-%m-%d %H_%M_%S")
    dir_path = "C:\Python27\Scripts\ServicePlatform\Page2\error_pic\error_" \
               + nowTime + '.jpg'

    def __init__(self, driver, base_url, action=ActionChains,
                 select=Select, page_title=''):
        Page.__init__(self, driver, base_url, action, select, page_title)

    def click_quit_btn(self):
        try:
            self.click(self.quit_button)
        except Exception as msg:
            self.take_screen_shot(self.dir_path)
            return u"print异常原因%s" % msg
