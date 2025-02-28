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
    driver_instance.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

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
        "company": "SkyPro",
    }

    for field, value in fields.items():
        fill_field(driver, field, value)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[type=submit]"))
    )
    submit_button.click()
    

def test_other_fields_green_background(driver, fill_form):

    other_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    expected_green_color = "rgba(209, 231, 221, 1)"
    collected_colors = {}
    all_green = True

    #wait = WebDriverWait(driver, 50)

    for field in other_fields:
        try:
            # Используем уникальный селектор для каждого поля
            element = driver.find_element(By.CSS_SELECTOR, f"#{field}")

            def is_background_green(driver):
                return (
                    element.value_of_css_property("background-color")
                    == expected_green_color
                )


            background_color = element.value_of_css_property("background-color")
            collected_colors[field] = background_color
            print(f"Цвет фона для '{field}': {background_color}")

            if background_color != expected_green_color:
                print(
                    f"Цвет для '{field}' не соответствует ожидаемому зеленому. "
                    f"Получено: {background_color}, Ожидалось: {expected_green_color}"
                )
                all_green = False
        except Exception as e:
            collected_colors[field] = f"Ошибка ({type(e).__name__}): {str(e)}"
            print(
                f"Ошибка при получении цвета для '{field}': "
                f"{type(e).__name__}: {e}"
            )
            all_green = False

    assert all_green, (
        f"Некоторые элементы не соответствуют ожидаемому зеленому цвету. "
        f"Собраны цвета: {collected_colors}"
    )

    if all_green:
        print("Все элементы имеют правильный зеленый фон!")