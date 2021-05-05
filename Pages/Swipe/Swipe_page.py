from Locators.locators import *
from Actions.actions import Actions
from appium.webdriver.common.touch_action import TouchAction


class SwipePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.driver.TouchAction = TouchAction(driver)

    def cometoswip(self):
        self.driver.implicitly_wait(5)
        self.actions._is_displayed(MenuLocators._me_button)

    def successlogin(self):
        self.actions._wait_for_element(SwipePageLocators._filter_button)
        try:
            self.actions._is_displayed(SwipePageLocators._filter_button)
        except:
            print('exception')
            return False
        else:
            print("Login Success!")
            return True

    def filtersaved(self):
        self.actions._wait_for_element(SwipePageLocators._filter_button)
        try:
            self.actions._is_displayed(SwipePageLocators._filter_button)
        except:
            print('exception')
            return False
        else:
            print("Filter was Changed!")
            return True

    def gotofilter(self):

        self.actions._wait_for_element(SwipePageLocators._filter_button)
        self.actions._click(SwipePageLocators._filter_button)

    def GetPageSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def scroll_down_to_block_or_report(self):
        self.driver.TouchAction.long_press(x=524, y=1760).move_to(x=524, y=400).release().perform()

        try:
            self.actions._is_displayed(SwipePageLocators._block_button)
            self.actions._click(SwipePageLocators._block_button)
            print("block button found")

        except:
            self.scroll_down_to_block_or_report()

    def report_abuse(self):
        self.actions._click(SwipePageLocators._report_abuse_button)

    def find_ID(self):
        self.actions._wait_for_element(IDlocators._user_Id)
        return self.actions._get_text(IDlocators._user_Id)

    def scroll_down_to_gift_card(self):
        self.driver.TouchAction.long_press(x=524, y=1760).move_to(x=524, y=400).release().perform()

        try:
            self.actions._is_displayed(SwipePageLocators._gift_card_button)
            print("GIft button found")

        except:
            print("Gift button is not found")
            self.scroll_down_to_gift_card()

    def scroll_down_to_location(self):
        self.driver.TouchAction.long_press(x=524, y=1760).move_to(x=524, y=400).release().perform()

        try:
            self.actions._is_displayed(SwipePageLocators._location_value)
            print("uraaaa gtanq")
        except:
            print('Location is not found')
            self.scroll_down_to_location()

    def location_text(self):
        return self.actions._get_text(SwipePageLocators._location_value)


    def swipe_left(self):
        self.actions._wait_for_element(SwipePageLocators._filter_button)
        self.driver.TouchAction.long_press(x=524, y=1760).move_to(x=400, y=1760).release().perform()
        print("Don't like!")

    def swipe_right(self):
        self.actions._wait_for_element(SwipePageLocators._filter_button)
        self.driver.TouchAction.long_press(x=524, y=1760).move_to(x=700, y=1760).release().perform()
        print("Like!")

    def tap_dislike_button(self):
        self.actions._wait_for_element(SwipePageLocators._dislike_button)
        self.actions._click(SwipePageLocators._dislike_button)
        print("Dislike!")

    def tap_like_button(self):
        self.actions._wait_for_element(SwipePageLocators._like_button)
        self.actions._click(SwipePageLocators._like_button)
        print("Like")


    def check_name_age(self):
        self.actions._wait_for_element(SwipePageLocators._user_name)
        self.actions._wait_for_element(SwipePageLocators._user_age)
        return self.actions._get_text(SwipePageLocators._user_name) + self.actions._get_text(SwipePageLocators._user_age)


    def undo(self):
        try:
            self.actions._wait_for_element(SwipePageLocators._undo_button)
            self.actions._click(SwipePageLocators._undo_button)
            self.actions._is_displayed(SwipePageLocators._photo_)
            self.driver.implicitly_wait(3)
            print("UNDO")
        except:
            print('Locator is not found, user is NOT PRIME')

    def tap_on_giftcard(self):
        self.actions._wait_for_element(SwipePageLocators._gift_card_button)
        self.actions._click(SwipePageLocators._gift_card_button)
        self.actions._wait_for_element(GiftLocators._friendship_gift_category)




