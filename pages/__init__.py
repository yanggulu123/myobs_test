from pages.AOS_nine_days_forecast_page import NineDaysForecastPage


class Pages:
    def __init__(self, driver):
        self._driver = driver

        self.aos_nine_days_forecast = NineDaysForecastPage(self._driver)
