from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Opening Amazon...")
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in")

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("new toy cars")
search_box.send_keys(Keys.RETURN)

print("Search completed for 'new toy cars'.")
time.sleep(5)

driver.quit()
print("Test Successfully Complete!")