import pytest
from PageObjects.HomePage import Homepage
from PageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class Fixture:

    @pytest.fixture(name="login")
    def login(self):
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
