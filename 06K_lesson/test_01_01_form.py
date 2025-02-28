import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver_instance = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver_instance.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver_instance, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[name=first-name]"))
    )
    yield driver_instance
    driver_instance.quit()


def fill_field(driver, field_name, value):
    driver.find_element(By.CSS_SELECTOR, f"[name={field_name}]").send_keys(value)


@pytest.fixture
def fill_form(driver):
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

    for field, value in fields.items():
        fill_field(driver, field, value)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[type=submit]"))
    )
    submit_button.click()

def test_zip_code_red_background(driver, fill_form):

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    zip_code_background_color = zip_code_field.value_of_css_property("background-color")
    print(f"Цвет фона для поля zip-code: {zip_code_background_color}")

    expected_red_color = "rgba(248, 215, 218, 1)"
    assert zip_code_background_color == expected_red_color, (
        f"Ожидался красный фон ({expected_red_color}), "
        f"но получен {zip_code_background_color}"
    )
    print("Проверка для поля Zip code прошла успешно! Поле подсвечено красным.")