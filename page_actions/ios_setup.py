def ios_setup(pages):
    pages.ios_nextwork_access.verify_page_loaded()
    pages.ios_nextwork_access.click_wifi_and_data_option()

    pages.ios_language_setup.verify_page_loaded()
    pages.ios_language_setup.click_english_option()

    pages.ios_location_access.verify_popup_loaded()
    pages.ios_location_access.click_while_using_the_app_option()

    pages.ios_location_access.verify_page_loaded()
    pages.ios_location_access.click_next_btn()

    pages.ios_notification_access.verify_popup_loaded()
    pages.ios_notification_access.click_allow_option()
    pages.ios_notification_access.click_agree_option()
    pages.ios_notification_access.click_next_btn()

    pages.ios_loc_based_notification.verify_popup_loaded()
    pages.ios_loc_based_notification.click_always_allow_option()
    pages.ios_loc_based_notification.click_next_btn()

    pages.ios_color_theme.verify_popup_loaded()
    pages.ios_color_theme.click_day_theme_color()
    pages.ios_color_theme.click_night_theme_color()
    pages.ios_color_theme.click_next_btn()

    pages.ios_finish_setting.click_finish_btn()