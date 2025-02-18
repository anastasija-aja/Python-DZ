from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(3)
add_element = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_element.click()
delete_buttons = WebDriverWait(driver, 3).until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Delete']"))
)
print(f"Размер списка {len(delete_buttons)}")
sleep(3)
driver.quit()