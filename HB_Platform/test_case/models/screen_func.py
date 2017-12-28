# coding=utf-8
import os

import time


def take_screen_shot(driver, file_name):
    # 截图函数
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    # 图片名称可以加个时间戳
    nowTime = time.strftime("%Y-%m-%d %H_%M_%S")
    file_path = base + "/report/image/" + nowTime + file_name
    driver.get_screenshot_as_file(file_path)
