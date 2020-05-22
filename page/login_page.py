from page.base_page import BasePage
from page.dicofdimmgr_page import DicOfDimMgrPage


class LoginPage(BasePage):
    def login(self):
        self.driver.get("http://10.5.86.208/TBM3")
        self.driver.find_element_by_id("txtUserName").send_keys("sysadmin")
        self.driver.find_element_by_id("txtPassword").send_keys("sinopec")
        self.driver.find_element_by_id("btnLogin").click()
        return DicOfDimMgrPage(self.driver)