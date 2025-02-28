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


def test_positive_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    assert "inventor" in driver.current_url, "Ошибка входа в систему"


def test_positive_checkout(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    items_to_add = [
        "#add-to-cart-sauce-labs-backpack",
        "#add-to-cart-sauce-labs-bolt-t-shirt",
        "#add-to-cart-sauce-labs-onesie",
    ]

    for item in items_to_add:
        driver.find_element(By.CSS_SELECTOR, item).click()

    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Anastasija")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Karasa")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("143041")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    try:
        total_label = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'summary_total_label')]")
            )
        )
        total_label_text = total_label.text
        print(f"Значение ячейки: {total_label_text}")

        cleaned_text = total_label_text.replace("Total: ", "")

        print(cleaned_text)
        driver.quit()
        expected_value = "$58.29"

        if cleaned_text == expected_value:
            print("Значение cleaned_text совпадает с ожидаемым значением.")
        else:
            print(f"Значение cleaned_text не совпадает с ожидаемым значением.")

        assert cleaned_text == expected_value, (
            f"Expected {expected_value} but got {cleaned_text}"
        )

    except Exception as e:
        pytest.fail(f"Тест не пройден: {str(e)}")