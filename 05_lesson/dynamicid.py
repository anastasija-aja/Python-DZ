from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")
btn_btn_primary = ".btn.btn-primary"
button = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, btn_btn_primary))
)
button.click()
driver.quit()