# coding=utf-8
import logging
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] '
#            '%(levelname)s %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     filename='log.log',
#     filemode='w'
# )
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         info = func.__doc__
#         logging.info('testing at : %s' % info)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def errorLog(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except AssertionError:
#             logging.getLogger().exception('Exception')
#             exit()
#     return wrapper
#
#
# def consoleLog(info, level='INFO'):
#     if level is 'INFO':
#         logging.info(info)
#     elif level is 'WARNING':
#         logging.warning(info)
#     elif level is 'ERROR':
#         logging.error(info)


class Page(object):
    def __init__(self, driver, action, select, page_title, base_url):
        self.driver = driver
        self.base_url = base_url
        self.action = action
        self.select = select
        self.page_title = page_title

    def on_page(self, page_title):
        return page_title in self.driver.title

    def _open(self, base_url, page_title):
        # 使用get打开访问链接地址
        self.driver.get(base_url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(page_title), u"打开开页面失败 %s" % base_url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.page_title)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def find_layer(self, loc):
        return self.find_element(*loc).text

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.driver.execute_script(src)

    def type_input(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            self.driver.find_element(*loc).click()
        except AssertionError:
            print("%s 页面中未能找到%s元素" % (self, loc))

    def switch_to_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != handles:
                self.driver.switch_to_window(handle)
            continue

    def select_options(self, loc, text):
        option_loc = self.find_element(*loc)
        sl = self.select(option_loc)
        sl.select_by_visible_text(text)

    def click_checkboxes(self, loc):
        checkboxes = self.find_elements(*loc)
        for check in checkboxes:
            check.click()
        print(len(checkboxes))

    def right_click(self, loc):
        loc = self.find_element(*loc)
        self.action(self.driver).context_click(loc).perform()

    def double_click(self, loc):
        loc = self.find_element(*loc)
        self.action(self.driver).double_click(loc).perform()

    def drag_and_drop(self, loc_source, loc_target):
        source = self.find_element(*loc_source)
        target = self.find_element(*loc_target)
        self.action(self.driver).drag_and_drop(source, target).perform()

    def move_to_element(self, loc):
        loc = self.find_element(*loc)
        self.action(self.driver).move_to_element(loc).perform()

    def click_and_hold(self, loc):
        loc = self.find_element(*loc)
        self.action(self.driver).click_and_hold(loc).perform()

    def get_title(self):
        return self.driver.title
