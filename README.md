# MyObservatory APP Automation Testing Framework on Android and iOS

A cross-platform automation testing framework for Android and iOS apps using ​**Appium**, ​**pytest**, ​**behave**, ​**Page Object Model**. Designed for maintainability, scalability, and ease of use.

---

## 🚀 Features
- ​**Cross-Platform Support**: Single codebase for Android and iOS.
- ​**BDD Testing**: Write tests in Gherkin syntax with `behave`.
- ​**Page Object Model**: Separate UI interactions from test logic.
- ​**Dynamic Device Management**: Automatically detect Android/iOS devices.
- ​**Multi-Environment Configs**: Manage dev/staging/prod environments via YAML.

---

## 🛠️ Prerequisites
- ​**Python 3.8+**
- ​**Node.js 14+** (for Appium)
- ​**Appium Server 2.0+**
- ​**Java JDK 8+** (for Android)
- ​**Android SDK** (for Android testing)
- ​**Xcode 13+** (for iOS testing)

---

## 📥 Installation
1. ​**Clone the repository**:
   ```bash
   git clone https://github.com/yanggulu123/myobs_test.git
   cd myobs_test

2. ​**​Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. ​**Configure environments**:
- Update config/dev.yaml, config/browserstack.yaml, and config/prod.yaml with your app/device details.

4. ​**Start Appium Server**:
- When we test locally, we need start the appium server. If we need to trigger the test in Cloud Platform like browserstack, no need to do this
   ```bash
   appium

## 🧪 Run Tests
- ​**Run with pytest**:
   ```bash
   # pytest run android tests only
   pytest tests/ -m android -s -v --env=dev

   # pytest run ios tests only
   pytest tests/ -m ios -s -v --env=dev

   # pytest run all tests only
   pytest tests/ -s -v --env=dev

- ​**Run BDD Tests with behave**:
   ```bash
   behave features/verify_nine-days_forecast_page.feature -D env=dev

- ​**Run test in browserstack**:
   - Save browserstack credentials in .env file under root folder
      * BROWSERSTACK_USERNAME=your_username
      * BROWSERSTACK_ACCESS_KEY=your_access_key
   - Then run command below:
   ```bash
   # Android
   pytest tests/ -m android --env=browserstack


## 📂 Project Directory Structure
```plaintext
myobservatory_app_automation/
├── README.md
├── assets
├── config
├── conftest.py
├── features
├── page_actions
├── pages
├── pytest.ini
├── requirements.txt
├── scripts
├── tests
│   ├── test_9days_weather.py
│   └── test_get_humidity.py
└── utils
    ├── driver_manager.py
    └── weather_utils.py

```

## 🔧 Troubleshooting
- ​**Device Not Detected**:
   - Run scripts/get_android_device_info.sh (Android) or check Xcode device logs (iOS).
- ​**​Appium Connection Errors**:
   - Verify Appium server is running: appium --log-level=error
   - Check port conflicts (4723 by default).
- ​**Other checkpoints**:
   - Adjust Appium/WebDriverAgent versions according to your OS and device setup.
   - For iOS real-device testing, ensure WebDriverAgent is properly signed in Xcode.


