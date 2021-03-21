import time
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstPage(BaseAction):

    # 关闭对话框按钮
    close_update_button = By.ID,"com.yunmall.lc:id/img_close"

    # 我按钮
    my_button = By.XPATH,"//*[@text='我']"

    @allure.step(title="点击关闭更新按钮")
    def click_close_update_button(self):
        try:
            self.click(self.close_update_button)
        except Exception as e:
            pass


    @allure.step(title="点击我按钮")
    def click_my_button(self):
        self.click(self.my_button)

    # page在测试函数时传self.page
    # 判断是否登录，如果未登录则进行登录
    def login_if_not(self,page):
        self.click_my_button()
        time.sleep(1)
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            pass
        else:
            page.register.click_login_button()
            page.login.login("itheima_test","itheima")
