import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    platformVersion='15',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        try:
            self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        except Exception as e:
            print(f"Failed to start Appium session: {str(e)}")
            raise

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
            el.click()
        except Exception as e:
            print(f"Test failed: {str(e)}")
            raise

if __name__ == '__main__':
    unittest.main()