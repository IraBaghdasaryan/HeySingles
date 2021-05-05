from Locators.locators import *
from Actions.actions import Actions

class MyprofilePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def go_to_settings(self):
        self.actions._click(MyProfile._settings_button)

    def check_credits(self):
        self.actions._wait_for_element(MyProfile._credits_number)
        creditstotal = self.actions._get_text(MyProfile._credits_number)
        print(creditstotal)




