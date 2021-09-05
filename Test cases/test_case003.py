import pytest
from PageObjects.HomePage import Homepage
from Utilities.fixture import Fixture


class TestHome(Fixture):
    # @pytest.mark.usefixtures("login")
    def test_homepage_navigation(self):
        home = Homepage(self.driver, self.wait, self.actions)
        all_button = home.all_button_in_navigation()
        assert all_button.is_enabled()
        home.all_button_in_navigation().click()
        home.how_much_time_u_want_to_stop_the_script_to_see_the_view_of_actions(3)
        print(home.customer_name_in_all_button())
        button_list = []
        button = []

        for e, buttons in enumerate(home.visible_names_in_all_button()):
            if buttons.text != "":
                button_list.append(buttons.text)
                button.append(buttons)
            if e <= 29:
                continue
            else:
                break
        home.how_much_time_u_want_to_stop_the_script_to_see_the_view_of_actions(3)
        dictionary = dict(zip(button_list, button))
        # print(dictionary.keys())
        dictionary.get('Best Sellers').click()
        if home.get_title_of_page() != "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            print(home.get_title_of_page())
            home.back_to_previous_page()












