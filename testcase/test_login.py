from page.dicofdimmgr_page import DicOfDimMgrPage
from page.login_page import LoginPage


class TestLogin:
    def setup(self):
        self.login=LoginPage()
    def test_openDODM(self):
        ulogin=self.login.login()
        ulogin.open_page()

    def teardown(self):
        pass
