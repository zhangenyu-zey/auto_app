import time
import pytest

from base.base_analyze import get_file_data
from base.base_driver import init_driver
from data.data_path import Path
from page.page import Page


class TestAddress():
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("address",get_file_data("test_address",Path.address_data()))
    def test_address(self,address):
        self.page.first.click_close_update_button()
        self.page.first.login_if_not(self.page)
        self.page.me.click_setting_button()
        self.page.setting.click_address_manager_button()
        self.page.address_list.click_add_address_button()
        self.page.edit_address.edit_address(address['name'],address['phone'],address['info'],address['post_code'])
        assert self.page.address_list.judge_address_manager() == address['assert']
