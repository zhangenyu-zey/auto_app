import random
import time
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):

    # 收件人输入框
    name_edit_text = By.ID,"com.yunmall.lc:id/address_receipt_name"
    # 手机号输入框
    phone_edit_text = By.ID,"com.yunmall.lc:id/address_add_phone"
    # 详细地址输入框
    address_info = By.ID,"com.yunmall.lc:id/address_detail_addr_info"
    # 邮编输入框
    post_code = By.ID,"com.yunmall.lc:id/address_post_code"
    # 默认地址按钮
    address_default_button = By.ID,"com.yunmall.lc:id/address_default"
    # 所在地区
    region_button = By.ID,"com.yunmall.lc:id/address_province"
    # 省市区特征
    area_feature = By.ID,"com.yunmall.lc:id/area_title"
    # 保存按钮
    save_button = By.XPATH,"//*[@text='保存']"

    # 输入收件人
    def input_name(self,text):
        self.send_keys(self.name_edit_text,text)
    # 输入手机号
    def input_phone(self,text):
        self.send_keys(self.phone_edit_text,text)
    # 输入详细地址
    def input_address_info(self,text):
        self.send_keys(self.address_info,text)
    # 输入邮编
    def input_post_code(self,text):
        self.send_keys(self.post_code,text)
    # 点击默认地址按钮
    def click_address_default_button(self):
        self.click(self.address_default_button)

    # 点击所在区域
    def click_region_button(self):
        self.click(self.region_button)

    # 进入所在区域,并随机点击一个区域
    def choose_region(self):
        self.click_region_button()
        while True:
        # 所有的可选的省市区
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                break
            areas = self.find_elements(self.area_feature)
            area_count = len(areas)
            print(area_count)
            area_index = random.randint(0,area_count-1)
            areas[area_index].click()
            time.sleep(1)

    # 点击保存
    def click_save_button(self):
        self.click(self.save_button)

    # 封装输入地址方法
    def edit_address(self,name,phone,info,post_code):
        self.input_name(name)
        self.input_phone(phone)
        self.input_address_info(info)
        self.input_post_code(post_code)
        self.choose_region()
        self.click_save_button()
        time.sleep(1)