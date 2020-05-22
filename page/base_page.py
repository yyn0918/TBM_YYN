from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
# 封装driver有关的操作
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 把driver提取出来
    _driver = ""
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 让python编译器知道有一个实例变量driver
        self.driver = None
        # 如果driver没有值表示第一次实例化子类
        if driver is None:
            # 复用已有浏览器
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.ie(options=opts)
            self.driver.maximize_window()
            # 隐式等待，解决元素加载过慢的问题
            self.driver.implicitly_wait(3)
        # 如果driver有值，说明不是第一次实例化
        else:
            self.driver = driver

    # using to find element
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_element(by, locator)

        # 显示等待

    def wait_for(self, fun):
        # 直到fun返回true或者超时就退出显示等待
        WebDriverWait(self._driver, 10).until(fun)


