
class Locators:
    class AOS:
        class HomePage:
            HEADER_HAM_BTN = ('xpath', '//android.widget.ImageButton[@content-desc="Navigate up"]')
            HEADER_TITLE = ('xpath', '//*[contains(@text, "MyObservatory")]')
            # add other locators here

        class HomeHeaderHamMenuPage:
            FORECAST_WARNING_SERVICE_DROPDOWN_LIST = ('xpath', '//*[contains(@text, "Forecast & Warning Services")]')
            # add other locators here

    class iOS:
        class HomePage:
            HEADER_HAM_BTN = ('xpath', '完善此处的定位器')
            HEADER_TITLE = ('xpath', '完善此处的定位器')
            # add other locators here

        class HomeHeaderHamMenuPage:
            FORECAST_WARNING_SERVICE_DROPDOWN_LIST = ('xpath', '完善此处的定位器')
            # add other locators here