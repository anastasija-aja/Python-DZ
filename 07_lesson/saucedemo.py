from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saucedemo:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def wait_for_element(self, by, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def login(self, username, password):
        self.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_items_to_cart(self, items):
        for item in items:
            self.find_element(By.CSS_SELECTOR, item).click()

    def checkout(self, first_name, last_name, postal_code):
        self.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
        self.find_element(By.CSS_SELECTOR, "#checkout").click()
        self.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
        self.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total_label_text(self):
        total_label = self.wait_for_element(
            By.XPATH, "//div[contains(@class, 'summary_total_label')]"
        )
        return total_label.text