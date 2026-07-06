from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_saucedemo_portfolio_login():
    print("\n[INFO] Browser start ho raha hai...")
    driver = webdriver.Chrome()
    
    # 1. Target Website open karna
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window() # Professional touch: Browser full screen karna
    
    try:
        # 2. Credentials enter karna
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # 3. Login Button par click
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2) # Dashboard load hone ka wait
        
        # 4. Asli Validation: Check URL change hua ya nahi
        assert "inventory.html" in driver.current_url
        
        # Agar assertion pass hua, toh yeh line chalegi
        print("\n=====================================")
        print("🎯 [PASS] Login Successful")
        print("=====================================")

    except AssertionError as error:
        # PRO MOVE: Agar login fail hua ya URL match nahi hua, toh yeh block chalega
        print("\n⚠️ [ERROR] Test fail ho gaya bhai! Screen ka X-ray le raha hoon...")
        
        # Automatic unique screenshot capture
        driver.save_screenshot("portfolio_login_failure.png")
        
        print("📸 Screenshot saved as 'portfolio_login_failure.png'")
        raise error # PyTest ko batane ke liye ki test fail hua hai
        
    finally:
        # Hamesha browser close hoga, chahe pass ho ya fail
        driver.quit()
        print("[INFO] Browser safely closed.")