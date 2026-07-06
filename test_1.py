from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Browser khul raha hai bhai...")
driver = webdriver.Chrome() 

# 1. Dummy E-commerce website par jao
driver.get("https://www.saucedemo.com/")
print("Swag Labs E-commerce site open ho gayi!")
time.sleep(2)

# 2. Username dhundho aur type karo (Standard dummy username)
username_box = driver.find_element(By.ID, "user-name")
username_box.send_keys("standard_user")
print("Username type ho gaya!")

# 3. Password dhundho aur type karo (Standard dummy password)
password_box = driver.find_element(By.ID, "password")
password_box.send_keys("secret_sauce")
print("Password type ho gaya!")
time.sleep(1) # Bas 1 second ka wait taaki tum type hota dekh sako

# 4. Asli Jadoo: Login Button dhundho aur us par CLICK karo!
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Login button par click ho gaya!")

# 5. Login ke baad dashboard dekhne ke liye 5 second ka wait
time.sleep(5)

driver.quit()
print("E-commerce Login Test Successfully Complete!")