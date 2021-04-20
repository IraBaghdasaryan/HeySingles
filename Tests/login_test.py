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


class Login_Test():

  def test_valid_login(self):
    driver = Driver()
    Welcome = WelcomePage(driver.driver)
    Login = LoginPage(driver.driver)
    Swipe = SwipePage(driver.driver)


    rand = randrange(len(list_correct_username_pass))
    Welcome.clickLogin()
    Login.testLogin(list_correct_username_pass[rand][0], list_correct_username_pass[rand][1])
    assert Swipe.successlogin() == True
    driver.tearDown()


  def test_logout(self):
    driver = Driver()
    menu = MenuPage(driver.driver)
    settings = SettingsPage(driver.driver)
    profile = MyprofilePage(driver.driver)
    account = AccountPage(driver.driver)

    menu.go_to_Me()
    profile.go_to_settings()
    settings.account()
    assert account.signout()
    del driver

  def test_invalid_login(self):
    driver = Driver()
    random = randrange(len(list_wrong_username))
    Welcome = WelcomePage(driver.driver)
    Login = LoginPage(driver.driver)

    Welcome.clickLogin()
    Login.testLogin(list_wrong_username[random][0], list_wrong_username[random][1])
    assert Login.invalidusername() == True
    del driver

  def test_invalid_pass(self):
    driver = Driver()

    Welcome = WelcomePage(driver.driver)
    Login = LoginPage(driver.driver)

    random = randrange(len(list_wrong_pass))
    Welcome.clickLogin()
    Login.testLogin(list_wrong_pass[random][0], list_wrong_pass[random][1])
    assert Login.invalidpass() == True
    del driver



LoginTest = Login_Test()

LoginTest.test_valid_login()
LoginTest.test_logout()
LoginTest.test_invalid_login()
LoginTest.test_invalid_pass()



