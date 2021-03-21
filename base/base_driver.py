from appium import webdriver

def init_driver(noReset = True):
    desired_caps = dict()
    # 平台的名字（大小写无所谓，不能乱写）
    desired_caps['platformName'] = 'Android'
    # 平台的版本（只写大版本也可以）
    desired_caps['platformVersion'] = '4.4'
    # 设备的名字（andriod可以随便写，ios的不能乱写）
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # 要打开的应用程序(这里是设置)
    desired_caps['appPackage'] = 'com.yunmall.lc'
    # 要打开的界面
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 不重置应用
    desired_caps["noReset"] = noReset
    # 支持中文,默认输入中文是有问题的
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 使用Uiautomator1框架
    desired_caps['automationName'] = 'Uiautomator1'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver