import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from slow_calculator import SlowCalculator


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        # Тестируемый URL медленного калькулятора

        calculator = SlowCalculator(driver)

        calculator.set_delay("45")

        calculator.click_button("7", "btn-outline-primary")
        calculator.click_button("+", "operator btn btn-outline-success")
        calculator.click_button("8", "btn btn-outline-primary")
        calculator.click_button("=", "btn btn-outline-warning")

        calculator.wait_for_result("15", 46)

        result_text = calculator.get_result()
        assert result_text == "15", f"Ожидается 15, но получено {result_text}"

    except WebDriverException as e:
        pytest.fail(f"Ошибка WebDriver: {str(e)}")
    except AssertionError as e:
        pytest.fail(f"Тест не прошел: {str(e)}")
    finally:
        driver.quit()