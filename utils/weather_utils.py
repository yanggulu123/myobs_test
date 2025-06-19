import requests
from datetime import datetime, timedelta

def get_weather_data():
    """ Qeury API and get responsee data """
    url = "https://pda.weather.gov.hk/locspc/data/ocf_data/HKO.v2.xml"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求失败：{str(e)}")


def calculate_target_date():
    """ get the day after tomorrow date format with YYYYmmdd """
    current_date = datetime.now()
    return (current_date + timedelta(days=2)).strftime("%Y%m%d")


def extract_humidity_range(data, target_date):
    """ extract the min-max range of ForecastRelativeHumidity where ForecastHour is between YYYYmmdd00 and YYYYmmdd23 """
    humidities = []
    for item in data.get("HourlyWeatherForecast", []):
        forecast_hour = item.get("ForecastHour", "")
        # 验证时间格式并筛选目标日期00-23点
        if (len(forecast_hour) == 10 and
                forecast_hour.startswith(target_date) and
                0 <= int(forecast_hour[8:10]) <= 23):
            humidity = item.get("ForecastRelativeHumidity")
            if humidity is not None:
                # print(f"HourlyWeatherForecast:{forecast_hour}")
                # print(f"ForecastRelativeHumidity:{humidity}")
                humidities.append(float(humidity))

    if not humidities:
        return "No data returned"
    return f"{min(humidities)}-{max(humidities)}%"


