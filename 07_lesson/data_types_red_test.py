import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data_types_page import DataTypesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "[name=first-name]").is_displayed()
    )
    yield driver
    driver.quit()


@pytest.fixture
def data_types_page(driver):
    return DataTypesPage(driver)


@pytest.fixture
def fill_form(data_types_page):
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    data_types_page.fill_form(fields)
    data_types_page.submit_form()
    yield


def test_zip_code_red_background(data_types_page, fill_form):
    zip_code_background_color = data_types_page.get_zip_code_background_color()
    print(f"Цвет фона для поля zip-code: {zip_code_background_color}")

    expected_red_color = "rgba(248, 215, 218, 1)"
    assert zip_code_background_color == expected_red_color, (
        f"Ожидался красный фон ({expected_red_color}), "
        f"но получен {zip_code_background_color}"
    )
    print("Проверка для поля Zip code прошла успешно! Поле подсвечено красным.")