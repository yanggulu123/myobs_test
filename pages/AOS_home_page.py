from pages.base_page import BasePage
from pages.locators import Locators
from hamcrest import assert_that


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.HEADER_HAM_BTN = Locators.AOS.HomePage.HEADER_HAM_BTN
        self.HEADER_TITLE = Locators.AOS.HomePage.HEADER_TITLE

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.HEADER_HAM_BTN), "Failed to go to the Home page")

    def open_header_ham_menu_btn(self):
        self.click(self.HEADER_HAM_BTN)