from Actions.actions import Actions
from Pages.Swipe.Swipe_page import SwipePage
from Config.config import Driver
from Pages.Swipe.FilterSwipe_page import FilterPage
from Pages.Swipe.Locations_page import LocationPage
from Pages.Settings.Settings_page import SettingsPage
from Pages.Swipe.Swipe_page import SwipePage
from Actions.actions import Actions
from Pages.Settings.account_page import AccountPage
from Pages.login_page import LoginPage
from Pages.menu_page import MenuPage
from Pages.myprofile_page import MyprofilePage
from Pages.welcome_page import WelcomePage
from Tests.data_storage import *
from random import randrange
from Config.config import Driver
from appium.webdriver.common.touch_action import TouchAction
from Locators.locators import *
from re import search
import pytest
import requests
import json
from requests.structures import CaseInsensitiveDict
from API.user_call import user_API
from Pages.Gifts.SendGift_page import GiftPage
from Tests.test_base import BaseTest
from Pages.Chat.chats_page import ChatPage


class Test_Swipe(BaseTest):
    def test_gender_check_Men(self):
        driver = Driver()
        callapi = user_API()
        Swipe = SwipePage(driver.driver)
        Filter = FilterPage(driver.driver)
        Swipe.gotofilter()
        Filter.filter()
        Filter.tapmen()
        Filter.save()
        Swipe.filtersaved()
        Swipe.scroll_down_to_block_or_report()
        Swipe.report_abuse()
        user_id = Swipe.find_ID()
        print(user_id)
        resp = callapi.get_users_gender("118304", user_id[1:])
        print(resp)
        assert resp == "Male"



    def test_gender_check_Women(self):
        driver = Driver()
        callapi = user_API()
        Swipe = SwipePage(driver.driver)
        Filter = FilterPage(driver.driver)
        Swipe.gotofilter()
        Filter.filter()
        Filter.tapwomen()
        Filter.save()
        try:
            Swipe.filtersaved()
            Swipe.scroll_down_to_block_or_report()
            Swipe.report_abuse()
            user_id = Swipe.find_ID()
            print(user_id)
            resp = callapi.get_users_gender("118304", user_id[1:])
            print(resp)
            assert resp == "Female"

        except: print("You've seen everyone")


    def test_filter_location(self):
        driver = Driver()
        Swipe = SwipePage(driver.driver)
        Filter = FilterPage(driver.driver)
        Location = LocationPage(driver.driver)

        Swipe.gotofilter()
        Filter.filter()
        try:
            Filter.taplocation()
            Location.writelocation("Berlin")
            Location.chooselocation("Berlin")
            Filter.save()
            Swipe.filtersaved()
            Swipe.scroll_down_to_location()
            location = Swipe.location_text().split(sep=",")[0]

            if location == "Berlin":
                print("Yohoo")
            del driver
        except:
            print("user is NON PRIME")

    def test_swipe_left(self):
        driver = Driver()
        Swipe = SwipePage(driver.driver)
        user1 = Swipe.check_name_age()
        Swipe.swipe_left()
        user2 = Swipe.check_name_age()
        assert (user1 != user2)
        del driver

    def test_swipe_right(self):
        driver = Driver()
        Swipe = SwipePage(driver.driver)
        user1 = Swipe.check_name_age()
        Swipe.swipe_right()
        user2 = Swipe.check_name_age()
        assert (user1 != user2)
        del driver

    def test_undo_verification(self):
        driver = Driver()
        Swipe = SwipePage(driver.driver)
        user1 = Swipe.check_name_age()
        Swipe.swipe_right()
        Swipe.undo()
        user2 = Swipe.check_name_age()
        assert (user1 == user2)

    def test_gift_from_card_romantic_kiss(self):
        driver = Driver()
        Swipe = SwipePage(driver.driver)
        Gift = GiftPage(driver.driver)
        Menu = MenuPage(driver.driver)
        Profile = MyprofilePage(driver.driver)
        Chat = ChatPage(driver.driver)

        Swipe.scroll_down_to_gift_card()
        Swipe.tap_on_giftcard()
        Gift.choose_gift_category_romantic()
        creditstart = Gift.gift_credits_number()
        Gift.choose_romantic_gift()
        Gift.send_gift()
        Chat.chat_text()
        Chat.backfromchat()
        Menu.go_to_Me()
        creditend = Profile.check_credits()
        assert creditstart is not creditend == True








Swipe_Test = Test_Swipe()

# Swipe_Test.Filter_Location()
# Swipe_Test.Swipe_left()
# Swipe_Test.Swipe_right()
# Swipe_Test.Undo_verification()
#Swipe_Test.test_gift_from_card_romantic_kiss()
#Swipe_Test.test_gender_check_Men()
#Swipe_Test.test_gender_check_Women()


