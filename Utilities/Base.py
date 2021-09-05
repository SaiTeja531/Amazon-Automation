import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseClass:

    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def find_element_by_selector(self, element):
        return self.driver.find_element(element)

    def wait_until_visibility_of_element_located(self, element):
        return self.wait.until(EC.visibility_of_element_located(element))

    def wait_until_element_clickable_link_text(self, element):
        return self.wait.until(EC.element_to_be_clickable(element))

    def wait_until_presence_of_all_elements_located(self, element):
        return self.wait.until(EC.presence_of_all_elements_located(element))

    def click_if_visible(self, element):
        self.wait.until(EC.visibility_of_element_located(element)).click()

    def hover(self, element):
        locator = self.wait.until(EC.presence_of_element_located(element))
        self.actions.move_to_element(locator).perform()

    def sending_keys(self, locator, keys):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(keys)

    def get_text_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_title_of_page(self):
        return self.driver.title

    def text_is_displayed(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    def wait_until_visibility_of_elements_located(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def clearing_any_text_present(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()

    def scroll_to_element(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].scrollIntoView;", element)

    def how_much_time_u_want_to_stop_the_script_to_see_the_view_of_actions(self, seconds):
        return time.sleep(seconds)

    def back_to_previous_page(self):
        self.driver.back()














