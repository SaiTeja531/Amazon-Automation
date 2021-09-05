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
            '''
            home.search("time")
            home.hover(Homepage.flag_element)
            assert home.flag_is_displayed().is_displayed()
            languages = home.wait_until_visibility_of_elements_located(Homepage.flag_elements)
            for language in languages:
                print(language.text)
            home.hover(Homepage.username)
            wish_list = home.wish_list_buttons()
            for wish in wish_list:
                assert wish.is_enabled()
                print(wish.text)
            your_account_options = home.account_option_buttons()
            for options in your_account_options:
                assert options.is_enabled()
                print(options.text)
            home.hover(Homepage.return_and_orders_element)
            home.username_is_displayed()
            home.video_suggestion_based_on_user()
            sliders = home.banner_items_displayed()
            next_button = home.next_button_in_banner()
            for slide in sliders:
                next_button.click()
                print(slide.get_attribute("alt"))
            print(home.greeting_customer_message().text)
            print(home.customer_since_message().text)
            '''














            






