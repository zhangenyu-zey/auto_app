from page.address_list_page import AddressListPage
from page.edit_address_page import EditAddressPage
from page.first_page import FirstPage
from page.login_page import LoginPage
from page.me_page import MePage
from page.register_page import RegisterPage
from page.setting_page import SettingPage
from page.vip_page import VipPage


class Page():

    def __init__(self,driver):
        self.driver = driver

    @property
    def first(self):
        # 返回首页
        return FirstPage(self.driver)

    @property
    def register(self):
        # 返回注册页面
        return RegisterPage(self.driver)

    @property
    def login(self):
        # 返回登录页面
        return LoginPage(self.driver)

    @property
    def me(self):
        # 返回我的页面
        return MePage(self.driver)

    @property
    def setting(self):
        # 返回设置页面
        return SettingPage(self.driver)

    @property
    def vip(self):
        # 返回vip页面
        return VipPage(self.driver)

    @property
    def address_list(self):
        # 返回地址管理页面
        return AddressListPage(self.driver)

    @property
    def edit_address(self):
        # 返回新增编辑地址页面
        return EditAddressPage(self.driver)