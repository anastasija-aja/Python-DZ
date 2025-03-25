from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataTypesPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы для полей формы
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

    # Методы для заполнения полей
    def fill_field(self, field_locator, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(field_locator)
        )
        element.clear()
        element.send_keys(value)

    def fill_form(self, fields_data):
        for field_name, value in fields_data.items():
            locator = getattr(self, field_name.upper().replace("-", "_"), None)
            if locator is None:
                raise ValueError(f"Локатор для поля '{field_name}' не найден.")
            self.fill_field(locator, value)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        submit_button.click()

    def get_zip_code_background_color(self):
        zip_code_element = self.driver.find_element(By.ID, "zip-code")  # или другой локатор
        return zip_code_element.value_of_css_property("background-color")

    # Метод для проверки цвета фона поля zip-code
    #def get_zip_code_background_color(self):
     #   zip_code_field = WebDriverWait(self.driver, 10).until(
      #      EC.presence_of_element_located(self.ZIP_CODE)
       # )
        #return zip_code_field.value_of_css_property("background-color")

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