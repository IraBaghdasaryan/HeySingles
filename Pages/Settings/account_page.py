from Locators.locators import *
from Actions.actions import Actions


class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def signout(self):
        self.actions._click(Account._signout_button)
        try:
            self.actions._wait_for_element(WelcomePageLocators._login_button)
            self.actions._is_displayed(WelcomePageLocators._login_button)
        except:
            print('exception')
            return False
        else:
            print("Logout Success!")
            return True

    def hideaccount(self):
        self.actions._click(Account._hideaccount_button)

    def backtosettings(self):
        self.actions._click(Account._back_button)


