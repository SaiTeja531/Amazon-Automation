import time
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from Utilities.Base import BaseClass
from selenium.webdriver.common.keys import Keys


class Homepage(BaseClass):
    sign_in1 = (By.CSS_SELECTOR, "[id=nav-signin-tooltip] span[class=nav-action-inner]")
    hello_sign_in = (By.ID, "nav-link-accountList-nav-line-1")
    sign_in2 = (By.CSS_SELECTOR, "[id=nav-flyout-ya-signin] span[class=nav-action-inner]")
    logo = (By.CSS_SELECTOR, "#nav-logo-sprites")
    username = (By.CSS_SELECTOR, "#nav-link-accountList-nav-line-1")
    search_box = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    search_suggestion = (By.XPATH, "//div[@id = 'nav-flyout-searchAjax']/div[@id='suggestions-template']/div/div")
    next_button_for_banner = (By.CSS_SELECTOR, "i.a-icon.a-icon-next-rounded")
    banners_on_homepage = (By.CSS_SELECTOR, "a.a-link-normal.aok-inline-block img")
    video_on_homepage = (By.XPATH, "//a[@data-itemtype='TITLE_RECOMMENDATION']/div/img")
    greeting_element = (By.CSS_SELECTOR, "div.a-section.a-spacing-none.hud-profile-greeting h2")
    customer_since_element = (By.CSS_SELECTOR, "div.a-section.a-spacing-none.hud-profile-greeting h2+p")
    flag_element = (By.CSS_SELECTOR, ".nav-line-2 .icp-nav-flag.icp-nav-flag-in")
    flag_elements = (By.CSS_SELECTOR, "#nav-flyout-icp span:nth-child(1)")
    user_account_elements = (By.CSS_SELECTOR, "#nav-al-your-account a span")
    wish_list_elements = (By.CSS_SELECTOR, "#nav-al-wishlist a span")
    return_and_orders_element = (By.CSS_SELECTOR, "#nav-orders")
    login_cart_element = (By.XPATH, "//div[@id='nav-cart-count-container']/span[2]")
    all_button_element = (By.CSS_SELECTOR, ".hm-icon.nav-sprite")
    customer_name_in_all_menu_element = (By.CSS_SELECTOR, "#hmenu-customer-name b")
    elements_displayed_in_all_tab = (By.XPATH, "//div[@id='hmenu-content']/descendant::ul[@class='hmenu hmenu-visible']/li")

    def __init__(self, driver, wait, actions):
        super().__init__(driver, wait, actions)

    def sign_in_frame(self):
        self.click_if_visible(Homepage.sign_in1)
        # return LoginPage(self.driver, self.wait, self.actions)

    def sign_in(self):
        self.hover(Homepage.hello_sign_in)
        self.click_if_visible(Homepage.sign_in2)
        # return LoginPage(self.driver, self.wait, self.actions)

    def get_logo(self):
        self.get_text_of_element(Homepage.logo)

    def home_page_title(self):
        assert self.get_title_of_page() == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

    def username_is_displayed(self):
        assert self.text_is_displayed(Homepage.username)

    def search(self, keys):
        self.sending_keys(Homepage.search_box, keys)
        suggestions = self.wait_until_visibility_of_elements_located(Homepage.search_suggestion)
        sugest = [suggestion.text for suggestion in suggestions]
        return print(sugest)

    def next_page_title_equals_entered_search(self, keys):
        self.clearing_any_text_present(Homepage.search_box)
        self.sending_keys(Homepage.search_box, keys)
        suggestions = self.wait_until_visibility_of_elements_located(Homepage.search_suggestion)
        for suggest in suggestions:
            if suggest.text == keys:
                self.sending_keys(suggest, Keys.ENTER)
                break

    def video_suggestion_based_on_user(self):
        self.scroll_to_element(Homepage.video_on_homepage)
        video = self.wait_until_visibility_of_element_located(Homepage.video_on_homepage)
        return print(video.get_attribute("alt"))

    def banner_items_displayed(self):
        return self.wait_until_presence_of_all_elements_located(Homepage.banners_on_homepage)

    def next_button_in_banner(self):
        return self.wait_until_visibility_of_element_located(Homepage.next_button_for_banner)

    def greeting_customer_message(self):
        return self.wait_until_visibility_of_element_located(Homepage.greeting_element)

    def customer_since_message(self):
        return self.wait_until_visibility_of_element_located(Homepage.customer_since_element)

    def flag_is_displayed(self):
        return self.wait_until_visibility_of_element_located(Homepage.flag_element)

    def account_option_buttons(self):
        return self.wait_until_presence_of_all_elements_located(Homepage.user_account_elements)

    def wish_list_buttons(self):
        return self.wait_until_presence_of_all_elements_located(Homepage.wish_list_elements)

    def login_cart_button(self):
        return self.wait_until_visibility_of_element_located(Homepage.login_cart_element)

    def all_button_in_navigation(self):
        return self.wait_until_visibility_of_element_located(Homepage.all_button_element)

    def customer_name_in_all_button(self):
        return self.wait_until_visibility_of_element_located(Homepage.customer_name_in_all_menu_element)

    def visible_names_in_all_button(self):
        return self.wait_until_presence_of_all_elements_located(Homepage.elements_displayed_in_all_tab)






























