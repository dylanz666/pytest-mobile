from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tools.decorators import log_allure_step, screenshot_on_failure


class HomePage(BasePage):
    # element locators
    FIRMWARE_VERSION = '//*[@text="FIRMWARE VERSION"]'
    GET_CONNECTION_STATUS = '//*[@text="GET CONNECTION STATUS"]'
    PAIRED_CONNECTION_STATUS = '//*[contains(@text, "Paired Connection Status:")]'

    def __init__(self, driver):
        self.driver = driver

        super().__init__(self.driver)

    @log_allure_step()
    @screenshot_on_failure()
    def is_opened(self):
        return self.is_element_displayed(By.XPATH, self.FIRMWARE_VERSION)

    @log_allure_step()
    @screenshot_on_failure()
    def get_connection_status(self):
        self.click(By.XPATH, self.GET_CONNECTION_STATUS)
        element = self.find_element(By.XPATH, self.PAIRED_CONNECTION_STATUS)
        assert element is not None
        return element.text
