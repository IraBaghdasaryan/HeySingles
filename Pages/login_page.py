from Locators.locators import *
from Actions.actions import Actions
from Tests.data_storage import *
from appium.webdriver.common.touch_action import TouchAction

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.touchActions = TouchAction(driver)

    def testLogin(self, login, password):
        self.actions._type(LoginPageLocators._username_input, login)
        self.driver.implicitly_wait(5)
        self.actions._type(LoginPageLocators._password_input, password)
        self.driver.implicitly_wait(5)
        self.actions._click(LoginPageLocators._signin_button)



    def invalidusername(self):
        try:
            self.actions._wait_for_element(LoginPageLocators._wrong_username)
        except:
            print('exception')
            return False
        else:
            print("Login failed!")
            return True

    def invalidpass(self):
        try:
            self.actions._wait_for_element(LoginPageLocators._wrong_pass)
        except:
            print('exception')
            return False
        else:
            print("Incorrect user ID or password!")
            return True



