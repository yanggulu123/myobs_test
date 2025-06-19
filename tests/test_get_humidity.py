import requests
import pytest
from utils.weather_utils import get_weather_data, calculate_target_date, extract_humidity_range
from datetime import datetime


def test_api_response():
    """ Verify the request response code and functionality"""
    # Verify the request response code
    response = requests.get("https://pda.weather.gov.hk/locspc/data/ocf_data/HKO.v2.xml")
    assert response.status_code == 200, "HTTP状态码非200"

    # Verify the function: extract humidity range of day after tomorrow
    try:
        data = get_weather_data()
        target_date = calculate_target_date()
        result = extract_humidity_range(data, target_date)
        assert "-" in result
    except Exception as e:
        pytest.fail(f"Function error：{str(e)}")


def test_print_weather_info():
    try:
        data = get_weather_data()
        target_date = calculate_target_date()
        current_date_str = datetime.now().strftime('%Y-%m-%d')
        humidity_range = extract_humidity_range(data, target_date)
        print(f"Current date：{current_date_str}")
        print(f"Target date：{target_date}")
        print(f"Target date humidity range：{humidity_range}")
    except Exception as e:
        pytest.fail(f"Error in printing weather info: {str(e)}")