from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculator:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay_value):
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(delay_value)

    def click_button(self, button_text, button_class):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(@class, '{button_class}') and text()='{button_text}']")
            )
        )
        button.click()

    def get_result(self):
        return self.driver.find_element(
            By.XPATH, "//div[contains(@class, 'screen')]"
        ).text

    def wait_for_result(self, expected_result, timeout):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(
                By.XPATH, "//div[contains(@class, 'screen')]"
            ).text == expected_result
        )