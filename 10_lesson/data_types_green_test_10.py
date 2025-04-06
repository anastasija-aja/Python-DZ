import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data_types_page_10 import DataTypesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import allure_pytest


@pytest.fixture(scope="module")
def driver():
    with allure.step("Инициализация WebDriver"):
        driver_instance = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver_instance.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        WebDriverWait(driver_instance, 10).until(
            lambda d: d.find_element(By.CSS_SELECTOR, "[name=first-name]").is_displayed()
        )
    yield driver_instance
    with allure.step("Закрытие WebDriver"):
        driver_instance.quit()


@pytest.fixture
def data_types_page(driver):
    return DataTypesPage(driver)


@pytest.fixture
def fill_form(data_types_page):
    with allure.step("Заполнение формы данными"):
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

        data_types_page.fill_form(fields)
        data_types_page.submit_form()
    yield


@allure.title("Проверка зеленого фона для заполненных полей формы")
@allure.description(
    "Тест проверяет, что после отправки формы поля имеют ожидаемый зеленый фон"
)
@allure.feature("Группировка теста по функциональности. Формы")
@allure.severity("Уровень важности теста")
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

    for field in other_fields:
        with allure.step(f"Проверка цвета фона для поля '{field}'"):
            try:
                element = driver.find_element(By.CSS_SELECTOR, f"#{field}")

                def is_background_green(driver):
                    return (
                        element.value_of_css_property("background-color")
                        == expected_green_color
                    )

                background_color = element.value_of_css_property("background-color")
                collected_colors[field] = background_color
                print(f"Цвет фона для '{field}': {background_color}")

                with allure.step(f"Сравнение цвета фона для поля '{field}'"):
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
                allure.attach(
                    name=f"Ошибка для поля '{field}'",
                    body=str(e),
                    attachment_type=allure.attachment_type.TEXT,
                )
                all_green = False

    with allure.step("Проверка, что все поля имеют правильный зеленый фон"):
        assert all_green, (
            f"Некоторые элементы не соответствуют ожидаемому зеленому цвету. "
            f"Собраны цвета: {collected_colors}"
        )

    if all_green:
        print("Все элементы имеют правильный зеленый фон!")