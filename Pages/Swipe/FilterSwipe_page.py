from Locators.locators import *
from Actions.actions import Actions
from Tests.data_storage import Filter_Swipe


class FilterPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.driver.TouchAction = TouchAction(driver)

    def filter(self):
        self.actions._wait_for_element(SwipeFilterLocator._save_button)

    def tapmen(self):
        self.driver.TouchAction.tap(Filter_Swipe.filter_men[0], Filter_Swipe.filter_men[1], Filter_Swipe.filter_men[2], Filter_Swipe.filter_men[3]).perform()

    def tapwomen(self):
        self.driver.TouchAction.tap(Filter_Swipe.filter_women[0], Filter_Swipe.filter_women[1], Filter_Swipe.filter_women[2], Filter_Swipe.filter_women[3]).perform()

    def tapboth(self):
        self.driver.TouchAction.tap(Filter_Swipe.filter_both[0], Filter_Swipe.filter_both[1], Filter_Swipe.filter_both[2], Filter_Swipe.filter_both[3]).perform()

    def taplocation(self):
        self.driver.TouchAction.tap(Filter_Swipe.filter_location[0], Filter_Swipe.filter_location[1], Filter_Swipe.filter_location[2], Filter_Swipe.filter_location[3]).perform()
        self.driver.implicitly_wait(5)

    def save(self):
        self.actions._find(SwipeFilterLocator._save_button)
        self.actions._click(SwipeFilterLocator._save_button)







