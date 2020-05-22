class PublicUse:
    def ele_click(self, eletype, str):
        if eletype == "id":
            js = "document.getElementById('" + str + "').click();"
            self.driver.execute_script(js)
        if eletype == "xpath":
            js = "document.getElementByXPath().click('" + str + "');"
            self.driver.execute_script(js)
