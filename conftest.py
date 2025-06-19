import pytest
from typing import Optional
from utils.driver_manager import get_driver
from pages import Pages


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev",
                     help="Environment: dev/prod/browserstack")


@pytest.fixture(scope="session")
def env(request) -> str:
    """get env from cmd running"""
    return request.config.getoption("--env")


@pytest.fixture(scope="function")
def platform(request) -> Optional[str]:
    # try to read platform from cmd, eg feature test running
    cli_platform = request.config.getoption("--platform", None)
    if cli_platform:
        return cli_platform

    # parce pytest.mark to get platform
    platform_markers = [
        marker.name for marker in request.node.iter_markers()
        if marker.name in ("android", "ios")
    ]
    if platform_markers:
        return platform_markers[0]

    pytest.skip("No platform provide (android/ios)")


@pytest.fixture(scope="function")
def driver(env: str, platform: Optional[str]):
    """Initial driver on every function test"""
    driver = get_driver(env, platform)
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    """Initial pages on demand"""
    return Pages(driver)