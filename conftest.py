import pytest
from utils.driver_manager import get_driver
from pages import Pages


@pytest.fixture(scope="function")
def platform(request):
    # try to read platform from cmd, eg feature test running
    cli_platform = request.config.getoption("--platform", None)
    if cli_platform:
        return cli_platform

    raise Exception("No platform parameter provide (android/ios), eg. --platform ios")


@pytest.fixture(scope="function")
def driver(platform):
    """Initial driver on every function test"""
    driver = get_driver(platform)
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    """Initial pages on demand"""
    return Pages(driver)
