import pytest

from base.base_analyze import get_file_data
from data.data_path import Path
from page.page import Page
from base.base_driver import init_driver
import time

class TestSetting:
    def setup(self):
        self.driver = init_driver(noReset= True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_setting(self):
        # 关闭更新弹窗
        self.page.first.click_close_update_button()
        # 如果没有登录就先登录
        self.page.first.login_if_not(self.page)
        # 点击设置按钮
        self.page.me.click_setting_button()
        # 点击退出按钮
        self.page.setting.click_quit_button()
        # 断言
        assert self.page.setting.get_sure_quit_text() == "确定要退出当前账号？"
