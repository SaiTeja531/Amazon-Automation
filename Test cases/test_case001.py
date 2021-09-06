from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import Homepage
from Utilities.fixture import Fixture


class TestLogin(Fixture):

    def test_login(self):
        home = Homepage(self.driver, self.wait, self.actions)
        home.home_page_title()
        try:
            home.sign_in_frame()
        except Exception as e:
            home.sign_in()
        finally:
            lg = LoginPage(self.driver, self.wait, self.actions)
            lg.login()
            lg.continue_click()
            lg.password_filed()
           














            






