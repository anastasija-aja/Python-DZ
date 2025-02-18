from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://the-internet.herokuapp.com/login")
username = "#username"
password = "#password"
username_user = driver.find_element(By.CSS_SELECTOR, username)
password_pass = driver.find_element(By.CSS_SELECTOR, password )
username_user.send_keys("tomsmith")
password_pass.send_keys("SuperSecretPassword")
sleep(3)
button_login = "radius"
button = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CLASS_NAME, button_login))
)
button.click()
driver.quit()