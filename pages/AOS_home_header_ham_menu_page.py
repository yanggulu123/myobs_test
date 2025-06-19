from pages.base_page import BasePage
from pages.locators import Locators
from hamcrest import assert_that


class HomeHeaderHamMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.FORECAST_WARNING_SERVICE_DROPDOWN_LIST = Locators.AOS.HomeHeaderHamMenuPage.FORECAST_WARNING_SERVICE_DROPDOWN_LIST

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.FORECAST_WARNING_SERVICE_DROPDOWN_LIST), "Failed to go to the Home page")

    def open_forecast_warning_service_dropdownlist(self):
        self.click(self.FORECAST_WARNING_SERVICE_DROPDOWN_LIST)

    def select_nine_days_forecast(self):
        self.click(self.NINE_DAYS_FORECAST)