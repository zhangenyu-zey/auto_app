import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 关于百年奥莱
    about_button = By.ID,"com.yunmall.lc:id/setting_about_yunmall"
    # 退出按钮
    quit_button = By.XPATH,"//*[@text='退出']"
    # 确定要退出当前账号？
    sure_quit = By.XPATH,"//*[@text='确定要退出当前账号？']"
    # 地址管理
    address_manager_button = By.XPATH,"//*[@text='地址管理']"

    @allure.step(title="点击百年奥莱")
    def click_about_button(self):
        self.scroll_find_element(self.about_button).click()

    @allure.step(title="点击退出")
    def click_quit_button(self):
        self.scroll_find_element(self.quit_button).click()

    @allure.step(title="获得确定退出文本")
    def get_sure_quit_text(self):
        text = self.find_element(self.sure_quit).text
        return text

    @allure.step(title="点击地址管理")
    def click_address_manager_button(self):
        self.scroll_find_element(self.address_manager_button).click()