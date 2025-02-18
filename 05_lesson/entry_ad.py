from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://the-internet.herokuapp.com/entry_ad")
button_close = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']//p[text()='Close']"))
    )
button_close.click()
sleep(3)
driver.quit()