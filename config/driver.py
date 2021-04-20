from appium import webdriver
from config.options import desired_cap, options

class Driver():
    def __init__(self):
        self.driver = webdriver.Remote(options["appium_url"], desired_cap)

    #def __del__(self):
        #self.driver.quit()

    def tearDown(self):
        self.driver.quit()



