from Locators.locators import *
from Actions.actions import Actions


class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)


    def go_to_Me(self):
        self.actions._wait_for_element(MenuLocators._me_button)
        self.actions._click(MenuLocators._me_button)
