import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from saucedemo import Saucedemo


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def base_page(driver):
    return Saucedemo(driver)


def test_positive_login(base_page):
    base_page.open("https://www.saucedemo.com/")
    base_page.login("standard_user", "secret_sauce")
    assert "inventory" in base_page.driver.current_url, "Ошибка входа в систему"


def test_positive_checkout(base_page):
    base_page.open("https://www.saucedemo.com/")
    base_page.login("standard_user", "secret_sauce")

    items_to_add = [
        "#add-to-cart-sauce-labs-backpack",
        "#add-to-cart-sauce-labs-bolt-t-shirt",
        "#add-to-cart-sauce-labs-onesie",
    ]
    base_page.add_items_to_cart(items_to_add)

    base_page.checkout("Anastasija", "Karasa", "143041")

    try:
        total_label = base_page.get_total_label_text()
        print(f"Значение ячейки: {total_label}")

        cleaned_text = total_label.replace("Total: ", "")
        print(cleaned_text)

        expected_value = "$58.29"

        assert cleaned_text == expected_value, (
            f"Expected {expected_value} but got {cleaned_text}"
        )

    except ValueError as e:
        pytest.fail(f"Тест не пройден: {str(e)}")