import time
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 登录后的账户名称
    account_name = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    # 设置按钮
    setting_button = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 加入超级vip
    be_vip_button = By.XPATH,"//*[@text='加入超级VIP']"

    # 判断获取账户文本
    @allure.step(title="判断获取账户文本")
    def judge_get_account_text(self):
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(),"截图",allure.attachment_type.PNG)
        try:
            text = self.find_element(self.account_name, 4, 1).text
        except:
            text = None
        if text:
            return True
        else:
            return False

    @allure.step(title="点击设置按钮")
    def click_setting_button(self):
        self.click(self.setting_button)

    @allure.step(title="点击加入超级VIP")
    def click_be_vip(self):
        self.scroll_find_element(self.be_vip_button).click()
        time.sleep(2)

