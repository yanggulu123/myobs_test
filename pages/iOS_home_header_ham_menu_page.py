from pages.AOS_home_header_ham_menu_page import HomeHeaderHamMenuPage
from pages.locators import Locators
from hamcrest import assert_that

# todo
class iOSHomeHeaderHamMenuPage(HomeHeaderHamMenuPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.FORECAST_WARNING_SERVICE_DROPDOWN_LIST = Locators.iOS.HomeHeaderHamMenuPage.FORECAST_WARNING_SERVICE_DROPDOWN_LIST