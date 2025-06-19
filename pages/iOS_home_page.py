from pages.AOS_home_page import HomePage
from pages.locators import Locators
from hamcrest import assert_that

# todo
class iOSHomePage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.HEADER_HAM_BTN = Locators.iOS.HomePage.HEADER_HAM_BTN
        self.HEADER_TITLE = Locators.iOS.HomePage.HEADER_TITLE
        # 其他定位器...