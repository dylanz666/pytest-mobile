import pytest
import allure

from constants.severity import Severity
from pages.home_page import HomePage
from tools.appium_driver import AppiumDriver

from tools.decorators import screenshot_at_the_end


@allure.feature("Feature: Demo android")
class TestAndroidDemo:
    def setup_class(self):
        self.driver = AppiumDriver().start_driver()
        self.home_page = HomePage(self.driver)

    def teardown_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.mark.P0
    @allure.severity(Severity.BLOCKER.value)
    @allure.title("Demo android")
    @allure.description("Demo android")
    @allure.testcase("https://platform/test/case?id=6123")
    @screenshot_at_the_end(driver=lambda self: self.driver)
    # @pytest.mark.skip
    def test_demo(self):
        assert self.home_page.is_opened()
        connection_status = self.home_page.get_connection_status()
        assert connection_status == "Paired Connection Status: DISCONNECTED"
