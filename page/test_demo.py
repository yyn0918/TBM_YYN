from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page.public_use import PublicUse

class TestDemo:
    def test1(self):
        #self.driver=webdriver.Ie()
        self.driver = webdriver.chrome()
        self.driver.get("http://10.5.86.208/TBM3")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "txtUserName").send_keys("sysadmin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("sinopec")
        #self.driver.find_element_by_id("btnLogin").send_keys(Keys.ENTER)
        #self.driver.find_element(By.ID, "btnLogin").click()
        pub=PublicUse
        pub.ele_click(self,"id","btnLogin")
        pub.ele_click(self,"xpath","//*[@id=‘menu’]/div[5]/div[1]/div[1]")

    def teardown(self):
        self.driver.quit()