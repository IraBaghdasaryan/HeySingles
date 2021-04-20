from Actions.actions import Actions
from Pages.Swipe.Swipe_page import SwipePage
from config.driver import Driver
from Pages.Swipe.FilterSwipe_page import FilterPage
from Pages.Swipe.Locations_page import LocationPage
from Pages.Settings.Settings_page import SettingsPage
from Pages.Swipe.Swipe_page import SwipePage
from Pages.Settings.account_page import AccountPage
from Pages.login_page import LoginPage
from Pages.menu_page import MenuPage
from Pages.myprofile_page import MyprofilePage
from Pages.welcome_page import WelcomePage
from Tests.data_storage import *
from random import randrange
from config.driver import Driver
from appium.webdriver.common.touch_action import TouchAction
from Locators.locators import *
from re import search

class Swipe_Test():


  def Filter_Location(self):
    driver = Driver()
    Swipe = SwipePage(driver.driver)
    Filter = FilterPage(driver.driver)
    Location = LocationPage(driver.driver)

    Swipe.gotofilter()
    Filter.filter()
    Filter.taplocation()
    Location.writelocation("Berlin")
    Location.chooselocation("Berlin")
    Filter.save()
    Swipe.filtersaved()
    Swipe.scroll_down()
    location = Swipe.location_text().split(sep=",")[0]
    # city = location[0]
    # country = location[1].strip()
    # "Germany"
    if location == "Berlin":
      print("Yohoo")
    del driver

  def Swipe_left(self):
    driver = Driver()
    Swipe = SwipePage(driver.driver)
    user1 = Swipe.check_name_age()
    Swipe.swipe_left()
    user2 = Swipe.check_name_age()
    assert (user1 != user2)
    del driver





    #Swipe.swipe_right()
    #Swipe.undo()

  def check_text(self):
    driver = Driver()
    Swipe = SwipePage(driver.driver)
    Swipe.check_name_age()







Swipe_Test = Swipe_Test()

#Swipe_Test.Filter_Location()
Swipe_Test.Swipe_left()
#Swipe_Test.check_text()


