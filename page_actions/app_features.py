from time import sleep

def app_features(pages, platform):
    if platform == "android":
        home_page = pages.aos_home
        home_header_ham_menu = pages.aos_home_header_ham_menu
        nine_days_forecast = pages.aos_nine_days_forecast
    else:
        home_page = pages.ios_home
        home_header_ham_menu = pages.ios_home_header_ham_menu
        nine_days_forecast = pages.ios_nine_days_forecast

    # home page
    home_page.verify_page_loaded()
    home_page.open_header_ham_menu_btn()
    home_header_ham_menu.verify_page_loaded()

    # home_header_ham_menu page
    home_header_ham_menu.open_forecast_warning_service_dropdownlist()
    sleep(3)
    home_header_ham_menu.select_nine_days_forecast()

    # nine_days_forecast page
    nine_days_forecast.verify_page_loaded()