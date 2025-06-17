import pytest
from pages import Pages


class Test9DayWeather(object):

    def test_android_platform(self, pages: Pages):
        pages.aos_nine_days_forecast.verify_page_loaded()

    def test_ios_platform(self):
        pass
