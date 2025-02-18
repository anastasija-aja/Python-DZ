from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)
input_number = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_number.send_keys("1000")
sleep(3)
input_number.clear()
sleep(3)
input_number.send_keys("999")
sleep(2)
driver.quit()