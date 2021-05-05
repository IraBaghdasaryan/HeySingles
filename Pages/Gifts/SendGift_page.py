from Locators.locators import *
from Actions.actions import Actions
from appium.webdriver.common.touch_action import TouchAction


class GiftPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.driver.TouchAction = TouchAction(driver)

    def choose_gift_category_romantic(self):
        self.actions._wait_for_element(GiftLocators._romatic_gift_category)
        self.actions._click(GiftLocators._romatic_gift_category)
        self.actions._wait_for_element(GiftLocators._romantic_gift_selector_rose)

    def choose_romantic_gift(self):
        self.actions._wait_for_element(GiftLocators._romantic_gift_selector_kiss)
        self.actions._click(GiftLocators._romantic_gift_selector_kiss)
        self.actions._wait_for_element(GiftLocators._send_gift_screen_paid_button)

    def send_gift(self):
        self.actions._wait_for_element(GiftLocators._send_gift_screen_paid_button)
        self.actions._click(GiftLocators._send_gift_screen_paid_button)
        self.driver.implicitly_wait(7)


    def romantic_gift_is_visible_kiss(self):
        self.actions._wait_for_element(GiftLocators._romantic_gift_selector_kiss)
        self.actions._is_displayed(GiftLocators._romantic_gift_selector_kiss)

    def gift_credits_number(self):
        self.actions._wait_for_element(GiftLocators._gift_credits)
        credits = self.actions._get_text(GiftLocators._gift_credits)
        print (credits)



