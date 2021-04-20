from appium.webdriver.common.touch_action import TouchAction

from Locators.locators import *
from Actions.actions import Actions
from Tests.data_storage import biometric_cancel


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.driver.TouchAction = TouchAction(driver)

    def clickSignUp(self):
        self.actions._click(WelcomePageLocators._joinus_button)

    def clickLogin(self):
        self.actions._wait_for_element(WelcomePageLocators._login_button)
        self.actions._click(WelcomePageLocators._login_button)
        self.driver.implicitly_wait(5)
        self.driver.TouchAction.tap(biometric_cancel[0], biometric_cancel[1], biometric_cancel[2], biometric_cancel[3]).perform()


