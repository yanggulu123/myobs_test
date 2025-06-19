from pages import Pages
import pytest
from page_actions.android_setup import android_setup
from page_actions.ios_setup import ios_setup
from page_actions.app_features import app_features

@pytest.mark.android
def test_android_app(pages: Pages):
    android_setup(pages)
    app_features(pages, "android")

@pytest.mark.ios
def test_ios_app(pages: Pages):
    ios_setup(pages)
    app_features(pages, "ios")