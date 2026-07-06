from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_ecommerce_login():
    driver = webdriver.Chrome() 
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    username_box = driver.find_element(By.ID, "user-name")
    username_box.send_keys("standard_user")

    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("secret_sauce")
    time.sleep(1) 

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2) 

    # ⚖️ ASSERTION: Verify login success by checking the new URL
    assert "inventory.html" in driver.current_url
    
    driver.quit()