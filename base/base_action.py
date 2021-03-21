from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class BaseAction():
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, feature, timeout=15, poll=1):
        '''
        根据特征找元素
        :param feature:特征
        :param timeout: 超时时间
        :param poll: 点击间隔时间
        :return: 元素
        '''
        if isinstance(feature, tuple):
            feature_by, feature_value = feature
            ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
            return ele
        else:
            print("传参类型错误")

    # 查找多个元素
    def find_elements(self, feature, timeout=15, poll=1):
        '''
        根据特征找多个元素，返回元素列表
        :param feature:特征
        :param timeout: 超时时间
        :param poll: 点击间隔时间
        :return: 元素列表
        '''
        if isinstance(feature, tuple):
            feature_by, feature_value = feature
            eles = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
            return eles
        else:
            print("传参类型错误")

    # 点击
    def click(self, feature, timeout=15, poll=1):
        self.find_element(feature, timeout, poll).click()

    # 输入
    def send_keys(self, feature, txt):
        self.find_element(feature).send_keys(txt)

    # 返回
    def press_back(self):
        self.driver.press_keycode(4)

    # 回车
    def press_enter(self):
        self.driver.press_keycode(66)

    # 获取元素文本
    def get_text(self,feature):
        return self.find_element(feature).text

    # 判断toast是否存在
    def is_toast_exit(self, message):
        feature = By.XPATH, "//*[contains(@text,'%s')]" % (message)
        try:
            self.find_element(feature)
            return True
        except TimeoutError:
            return False

    # 获取toast内容
    def get_toast_text(self, message):
        if self.is_toast_exit(message):
            feature = By.XPATH, "//*[contains(@text,'" + message + "')]"
            ele = self.find_element(feature, 4, 1)
            return ele.text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    def scroll_page_one_time(self,direction="up"):
        '''
        滑动一次屏幕
        :param direction: 方向
        :return:
        '''
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_width = width / 2
        left_width = width / 4 * 1
        right_width = width / 4 * 3
        center_height = height / 2
        top_height = height / 4 * 1
        bottom_height = height / 4 * 3

        # 滑动距离
        if direction == "up":
            self.driver.swipe(center_width, bottom_height, center_width, top_height, 2000)
        elif direction == "down":
            self.driver.swipe(center_width, top_height, center_width, bottom_height, 2000)
        elif direction == "left":
            self.driver.swipe(right_width, center_height, left_width, center_height, 1500)
        elif direction == "right":
            self.driver.swipe(left_width, center_height, right_width, center_height, 1500)
        else:
            raise Exception("参数错误，请传参数：up/down/left/right")

    def scroll_find_element(self, feature,direction="up"):
        '''
        滑动找元素
        :param feature:元素特征
        :param direction: 方向
        :return:元素
        '''
        page_source = ''
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)
                # 判断是否滑动后的page_source是否发生变化
                if page_source == self.driver.page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

    def is_keyword_in_page_source(self,keyword):
        '''
        如果keyword在page_source中，返回True,否则返回false
        :return:
        '''
        while True:
            i = 0
            if keyword in self.driver.page_source:
                return True
            else:
                time.sleep(0.5)
                i += 1
                if i > 3:
                    return False

    def is_feature_exit(self,feature):
        '''
        元素是否存在
        :param feature:
        :return:
        '''
        try:
            self.find_element(feature)
            return True
        except:
            return False

