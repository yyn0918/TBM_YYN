from time import sleep

from page.base_page import BasePage


class DicOfDimMgrPage(BasePage):
    def open_page(self):
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[5]/div[1]/div[1]').click()
        self.driver.find_element_by_xpath('//*[@id="_easyui_tree_4"]/span[3]').click()
        self.driver.find_element_by_xpath('//*[@id="_easyui_tree_9"]/span[4]').click()
        sleep(6)