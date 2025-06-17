from appium.options.android import UiAutomator2Options
from appium import webdriver
import yaml
import os


def get_driver(platform="android"):

    config_path = os.path.join("config", "env.yaml")
    with open(config_path) as f:
        config = yaml.safe_load(f)

    if platform == "android":
        caps = config["android"]
        return webdriver.Remote("http://localhost:4723", options=UiAutomator2Options().load_capabilities(caps))

    elif platform == "ios":
        # todo
        pass
