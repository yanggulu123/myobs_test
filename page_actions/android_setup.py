from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def android_setup(pages):
    # Scenario 1 - disclaimer page
    pages.aos_disclaimer.verify_page_loaded()
    pages.aos_disclaimer.click_agree_btn()

    # Scenario 2 - privacy_policy_statements page
    pages.aos_privacy_policy_statements.verify_page_loaded()
    pages.aos_privacy_policy_statements.click_agree_btn()

    # Scenario 3 - device_notification_setting page
    noti_locator = pages.aos_device_notification_setting.NOTIFICATION_POPUP_TITLE
    try:
        noti_element = WebDriverWait(pages.aos_device_notification_setting.driver, 10).until(
            EC.visibility_of_element_located(noti_locator))
        pages.aos_device_notification_setting.verify_page_loaded()
        pages.aos_device_notification_setting.click_allow_option()
    except Exception as e:
        print(f"We could not find the element in 10s, skip related tests and move on with rest test steps. : {e}")

    # Scenario 4 - background_location_access page
    pages.aos_background_location_access.verify_page_loaded()
    pages.aos_background_location_access.click_OK_btn()

    # Scenario 5 - device_location_access page
    pages.aos_device_location_access.verify_page_loaded()
    pages.aos_device_location_access.click_while_using_the_app_option()

    # Scenario 6 - location_permission_config page
    pages.aos_location_permission_config.verify_page_loaded()
    pages.aos_location_permission_config.click_allow_all_the_time_option()
    pages.aos_location_permission_config.press_device_back_btn()
    sleep(3)

    # Scenario 7 - whats_new page
    whats_new_locator = pages.aos_whats_new.NEXT_BUTTON
    try:
        whats_new_element = WebDriverWait(pages.aos_whats_new.driver, 10).until(
            EC.visibility_of_element_located(whats_new_locator))
        pages.aos_whats_new.verify_sub_page1_loaded()
        pages.aos_whats_new.click_next_btn()
        pages.aos_whats_new.verify_sub_page2_loaded()
        pages.aos_whats_new.click_not_show_btn()
    except Exception as e:
        print(f"We could not find the element in 10s, skip related tests and move on with rest test steps. : {e}")