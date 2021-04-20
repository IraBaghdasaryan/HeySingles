from Locators.locators import *
from Actions.actions import Actions

class LocationPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

    def writelocation(self, city):
        #self.actions._wait_for_element(SwipeLocationLocators._search_box)
        self.actions._type(SwipeLocationLocators._search_box, city)
        self.driver.implicitly_wait(5)

    def chooselocation(self, city_name):
        self.actions._wait_for_element_dynamic(SwipeLocationLocators._line_results, city_name)
        self.actions._click_dynamic(SwipeLocationLocators._line_results, city_name)

    def findfirstline(self):
        self.actions._find(SwipeLocationLocators._line_results)

    def tapfirstline(self):
        self.actions._wait_for_element(SwipeLocationLocators._line_results)
        self.actions._click(SwipeLocationLocators._line_results)



