from Locators.locators import *
from Actions.actions import Actions
from appium.webdriver.common.touch_action import TouchAction


class ChatPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.driver.TouchAction = TouchAction(driver)


    def backfromchat(self):

        #self.actions._wait_for_element(Chat._back_from_chat)
        self.actions._click(Chat._back_from_chat)
        self.driver.TouchAction.long_press(x=88, y=181).release().perform()

    def chat_text(self):
        self.actions._wait_for_element(Chat._chat_text)
        self.actions._is_displayed(Chat._chat_text)
