import time

import pytest

from base.base_analyze import get_file_data
from base.base_driver import init_driver
from data.data_path import Path
from page.page import Page


class TestVip:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("key",get_file_data("test_vip",Path.vip_data()))
    def test_vip(self,key):
        self.page.first.click_close_update_button()
        self.page.first.login_if_not()
        self.page.me.click_be_vip()
        # 切换到webview
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.page.vip.input_invite(key["keyword"])
        self.page.vip.click_be_vip_button()
        # 断言
        assert self.page.vip.is_keyword_in_page_source(key["expect"]),"{}不在page_source中".format(key["expect"])
        # 切换到原生环境
        self.driver.switch_to.content(self.driver.contexts[0])
