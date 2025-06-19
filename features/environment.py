import logging
from pages import Pages
from utils.driver_manager import get_driver

logging.basicConfig(level=logging.INFO)

def before_scenario(context, scenario):
    # Parse Scenario tags to get platform value
    for tag in scenario.effective_tags:
        if tag.startswith("platform."):
            context.platform = tag.split(".")[1]  # 获取 android/ios
            logging.info(f"Platform set to {context.platform}")
            break

def before_all(context):
    try:
        # Read env from cmd running, env can be dev, prod, browserstack.
        env = context.config.userdata.get("env", "dev")
        logging.info(f"Environment set to {env}")
        # Initialise Appium Driver
        if context.platform == "android":
            context.driver = get_driver(env, 'android')
        elif context.platform == "ios":
            context.driver = get_driver(env, 'ios')
        # Initialise Page objects
        context.app = Pages(context.driver)
    except Exception as e:
        logging.error(f"Fail to start driver: {str(e)}")
        raise

def after_all(context):
    context.driver.quit()