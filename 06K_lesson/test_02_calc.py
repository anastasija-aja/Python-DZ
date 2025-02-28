import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator_result(driver):
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


        delay = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")


        seven_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class, 'btn-outline-primary') and text()='7']")
            )
        )
        seven_button.click()


        plus_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[contains(@class, 'operator btn btn-outline-success') and text()='+']",
                )
            )
        )
        plus_button.click()


        eight_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class, 'btn btn-outline-primary') and text()='8']")
            )
        )
        eight_button.click()


        equally_button = WebDriverWait(driver, 46).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[contains(@class, 'btn btn-outline-warning') and text()='=']",
                )
            )
        )
        equally_button.click()


        WebDriverWait(driver, 46).until(
            lambda d: d.find_element(By.XPATH, "//div[contains(@class, 'screen')]").text == "15"
        )
        result_text = driver.find_element(By.XPATH, "//div[contains(@class, 'screen')]").text

        assert result_text == "15", f"Ожидается 15, но получено {result_text}"

    except Exception as e:
        pytest.fail(f"Тест завершился с ошибкой: {str(e)}")
