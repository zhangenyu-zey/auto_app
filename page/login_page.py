import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 账号输入框
    account_input = By.XPATH,"//*[@text='请输入手机/昵称']"
    # 密码输入框
    password_input = By.ID,"com.yunmall.lc:id/logon_password_textview"
    # 登录按钮
    login_button = By.XPATH,"//*[@text='登录']"

    # 输入账号
    @allure.step(title="输入账号")
    def input_account(self,txt):
        allure.attach(txt,"账号",allure.attachment_type.TEXT)
        self.send_keys(self.account_input,txt)
        allure.attach(self.driver.get_screenshot_as_png(),"截图",allure.attachment_type.PNG)
    # 输入密码
    @allure.step(title="输入密码")
    def input_password(self,txt):
        allure.attach(txt, "密码", allure.attachment_type.TEXT)
        self.send_keys(self.password_input,txt)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
    # 点击登录
    @allure.step(title="点击登录")
    def click_login_button(self):
        self.click(self.login_button)
    # 封装登录
    def login(self,account,password):
        self.input_account(account)
        self.input_password(password)
        self.click_login_button()
