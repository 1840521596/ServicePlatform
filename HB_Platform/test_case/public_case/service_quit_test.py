# encoding=utf-8
import sys
import time

from HB_Platform.test_case.page_obj.QuitPage import QuitPage

reload(sys).setdefaultencoding('utf-8')

# class TestServiceLogin(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def tearDown(self):
#         pass


def test_quit(self):
        driver = self.driver
        base_url = 'http://111.203.248.61:8001/'
        Quit = QuitPage(driver, base_url)
        # 退出
        # print'点击登出按钮'
        Quit.click_quit_btn()
        time.sleep(1)
        # 关闭
        # print'关闭窗口'
        self.driver.close()
        time.sleep(1)


# if __name__ == '__main__':
#     unittest.main()
