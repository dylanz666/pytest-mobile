from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.config_util import ConfigUtil
from tools.decorators import log_allure_step


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.global_timeout = ConfigUtil.get_global_timeout()

    @log_allure_step()
    def start_activity(self, package_name, activity_name):
        """启动指定包名和 Activity 名称的应用"""
        self.driver.start_activity(package_name, activity_name)

    @log_allure_step()
    def wait_for_element(self, by, value, timeout=10):
        """智能等待元素可见"""
        timeout = timeout if timeout else self.global_timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    @log_allure_step()
    def wait_for_element_to_disappear(self, by, value, timeout=10):
        """智能等待元素消失"""
        timeout = timeout if timeout else self.global_timeout
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((by, value)))

    @log_allure_step()
    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        """智能等待元素可点击"""
        timeout = timeout if timeout else self.global_timeout
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    @log_allure_step()
    def find_element(self, by, value):
        """查找单个元素"""
        return self.wait_for_element(by, value)

    @log_allure_step()
    def find_elements(self, by, value, timeout=10):
        """查找多个元素"""
        timeout = timeout if timeout else self.global_timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, value)))

    @log_allure_step()
    def click(self, by, value):
        """点击元素"""
        element = self.wait_for_element_to_be_clickable(by, value)
        element.click()

    @log_allure_step()
    def send_keys(self, by, value, text):
        """输入文本"""
        element = self.find_element(by, value)
        element.send_keys(text)

    @log_allure_step()
    def clear_text(self, by, value):
        """清除文本框中的文本"""
        element = self.find_element(by, value)
        element.clear()

    @log_allure_step()
    def get_text(self, by, value):
        """获取元素文本"""
        element = self.find_element(by, value)
        return element.text

    @log_allure_step()
    def get_attribute(self, by, value, attribute):
        """获取元素属性"""
        element = self.find_element(by, value)
        return element.get_attribute(attribute)

    @log_allure_step()
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """滑动操作"""
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @log_allure_step()
    def get_element_location(self, by, value):
        """获取元素位置"""
        element = self.find_element(by, value)
        return element.location

    @log_allure_step()
    def get_element_size(self, by, value):
        """获取元素大小"""
        element = self.find_element(by, value)
        return element.size

    @log_allure_step()
    def scroll_to_element(self, by, value):
        """滚动到特定元素"""
        element = self.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @log_allure_step()
    def is_element_displayed(self, by, value):
        """检查元素是否可见"""
        try:
            element = self.find_element(by, value)
            return element.is_displayed()
        except TimeoutException:
            return False

    @log_allure_step()
    def switch_to_alert(self, timeout=10):
        """切换到弹出窗口"""
        timeout = timeout if timeout else self.global_timeout
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert

    @log_allure_step()
    def accept_alert(self):
        """接受弹出窗口"""
        alert = self.switch_to_alert()
        alert.accept()

    @log_allure_step()
    def dismiss_alert(self):
        """拒绝弹出窗口"""
        alert = self.switch_to_alert()
        alert.dismiss()

    @log_allure_step()
    def switch_to_window(self, window_name):
        """切换到指定窗口"""
        self.driver.switch_to.window(window_name)

    @log_allure_step()
    def get_current_window_handle(self):
        """获取当前窗口句柄"""
        return self.driver.current_window_handle

    @log_allure_step()
    def get_all_window_handles(self):
        """获取所有窗口句柄"""
        return self.driver.window_handles

    @log_allure_step()
    def wait_for_condition(self, condition, timeout=10):
        """等待特定条件"""
        timeout = timeout if timeout else self.global_timeout
        WebDriverWait(self.driver, timeout).until(condition)

    @log_allure_step()
    def get_page_source(self):
        """获取当前页面的源代码"""
        return self.driver.page_source

    @log_allure_step()
    def complex_swipe(self, direction, duration=1000):
        """执行复杂的滑动操作"""
        size = self.driver.get_window_size()
        if direction == "up":
            self.swipe(size['width'] / 2, size['height'] * 0.8, size['width'] / 2, size['height'] * 0.2, duration)
        elif direction == "down":
            self.swipe(size['width'] / 2, size['height'] * 0.2, size['width'] / 2, size['height'] * 0.8, duration)
        elif direction == "left":
            self.swipe(size['width'] * 0.8, size['height'] / 2, size['width'] * 0.2, size['height'] / 2, duration)
        elif direction == "right":
            self.swipe(size['width'] * 0.2, size['height'] / 2, size['width'] * 0.8, size['height'] / 2, duration)

    @log_allure_step()
    def click_if_exists(self, by, value):
        """如果元素存在则点击，不存在则不做任何事"""
        try:
            element = self.wait_for_element_to_be_clickable(by, value)
            element.click()
        except TimeoutException:
            print(f"Element {by} with value {value} not found. No action taken.")

    @log_allure_step()
    def take_screenshot(self, file_name):
        """截图并保存到指定文件"""
        self.driver.save_screenshot(file_name)

    @log_allure_step()
    def execute_script(self, script, *args):
        """执行 JavaScript 脚本"""
        return self.driver.execute_script(script, *args)
