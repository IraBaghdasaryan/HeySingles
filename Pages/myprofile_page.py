from Locators.locators import *
from Actions.actions import Actions

class MyprofilePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def go_to_settings(self):
        self.actions._click(MyProfile._settings_button)




