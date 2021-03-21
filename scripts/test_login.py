import pytest

from base.base_analyze import get_file_data
from data.data_path import Path
from page.page import Page
from base.base_driver import init_driver
import time

class TestLogin:
    def setup(self):
        self.driver = init_driver(noReset= False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("user",get_file_data("test_login",Path.login_data()))
    def test_login(self,user):
        # 关闭更新框
        self.page.first.click_close_update_button()
        # 点击我
        self.page.first.click_my_button()
        # 点击已有账号，登录
        self.page.register.click_login_button()
        # 登录
        self.page.login.login(user["account"],user["password"])
        # 断言
        assert self.page.me.judge_get_account_text() == user["assert_account"]