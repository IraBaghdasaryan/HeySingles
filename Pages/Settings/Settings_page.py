from Locators.locators import *
from Actions.actions import Actions


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    #def basicinfo(self):
        #self.actions._click()

    def account(self):
        self.actions._wait_for_element(Settings._account_button)
        self.actions._click(Settings._account_button)


