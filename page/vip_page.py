import time
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):

    # 邀请码输入框
    invite_edit_text = By.XPATH,"//input[@type='tel']"
    # 立即成为会员
    be_vip_button = By.XPATH,"//input[@value='立即成为会员']"

    @allure.step(title="输入邀请码")
    def input_invite(self,text):
        self.send_keys(self.invite_edit_text,text)
    @allure.step(title="点击立即成为会员")
    def click_be_vip_button(self):
        self.click(self.be_vip_button)