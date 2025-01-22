from appium import webdriver
from appium.options.android import UiAutomator2Options

from tools.config_util import ConfigUtil


class AppiumDriver:
    _instance = None

    def __init__(self):
        self.driver = None
        # appium server
        global_config = ConfigUtil.get_global_config()
        self.appium_host = global_config.get("appium_host")
        self.appium_port = global_config.get("appium_port")
        self.appium_server = f'http://{self.appium_host}:{self.appium_port}'
        # appium options
        self.appium_options = UiAutomator2Options()
        self.appium_options.platform_name = global_config.get("platform_name")
        self.appium_options.platform_version = global_config.get("platform_version")
        self.appium_options.udid = global_config.get("udid")
        self.appium_options.app_package = global_config.get("app_package")
        self.appium_options.app_activity = global_config.get("app_activity")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppiumDriver, cls).__new__(cls)
            cls._instance.driver = None
        return cls._instance

    def start_driver(self, appium_options=None):
        if self.driver:
            return self.driver
        options = appium_options if appium_options else self.appium_options
        self.driver = webdriver.Remote(command_executor=self.appium_server, options=options)
        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
