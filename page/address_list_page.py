import time
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 新增地址
    add_address_button = By.XPATH,"//*[@text='新增地址']"
    # 地址管理
    address_manager = By.XPATH,"//*[@text='地址管理']"


    @allure.step(title="点击新增地址")
    def click_add_address_button(self):
        self.scroll_find_element(self.add_address_button).click()

    # 判断当前页面是否有地址管理
    def judge_address_manager(self):
        self.is_feature_exit(self.address_manager)