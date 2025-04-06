"""
Импортируются необходимые модули Selenium для работы с веб-элементами и ожиданиями
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataTypesPage:
    """
    Создается класс для работы со страницей, принимающий драйвер как параметр
    """
    def __init__(self, driver):
        self.driver = driver

    """
    Определяются локаторы для всех полей формы
    """
    FIRST_NAME = (By.CSS_SELECTOR, "[name=first-name]")
    LAST_NAME = (By.CSS_SELECTOR, "[name=last-name]")
    ADDRESS = (By.CSS_SELECTOR, "[name=address]")
    E_MAIL = (By.CSS_SELECTOR, "[name=e-mail]")
    PHONE = (By.CSS_SELECTOR, "[name=phone]")
    ZIP_CODE = (By.CSS_SELECTOR, "[name=zip-code]")
    CITY = (By.CSS_SELECTOR, "[name=city]")
    COUNTRY = (By.CSS_SELECTOR, "[name=country]")
    JOB_POSITION = (By.CSS_SELECTOR, "[name=job-position]")
    COMPANY = (By.CSS_SELECTOR, "[name=company]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type=submit]")

    """
    Метод для заполнения отдельного поля:
    - Ждет появления элемента,
    - Очищает поле,
    - Вводит значение
    """
    def fill_field(self, field_locator, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(field_locator)
        )
        element.clear()
        element.send_keys(value)

    """
    Метод для заполнения всей формы:
    - Принимает словарь с данными,
    - Находит соответствующие локаторы,
    - Заполняет каждое поле
    """
    def fill_form(self, fields_data):
        for field_name, value in fields_data.items():
            locator = getattr(self, field_name.upper().replace("-", "_"), None)
            if locator is None:
                raise ValueError(f"Локатор для поля '{field_name}' не найден.")
            self.fill_field(locator, value)

    """
    Метод submit_form:
    - Метод для отправки формы после заполнения
    """
    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        submit_button.click()

    """
    Метод проверки цвета фона zip-code:
    - Получает цвет фона элемента zip-code
    """
    def get_zip_code_background_color(self):
        zip_code_element = self.driver.find_element(By.ID, "zip-code") 
        return zip_code_element.value_of_css_property("background-color")