from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_headless_screenshot():
    # 1. GHOST MODE SETUP
    chrome_options = Options()
    chrome_options.add_argument("--headless") 

    driver = webdriver.Chrome(options=chrome_options)

    # 2. Website par jao
    driver.get("https://github.com/")

    # 3. PROOF: Screenshot nikalna
    screenshot_path = "test_5_GitHub_Proof.png"
    driver.save_screenshot(screenshot_path)

    # 4. ⚖️ ASSERTION: Check karo ki screenshot file generate hui ya nahi
    # Yahan hum check kar rahe hain ki browser title sahi hai
    assert "GitHub" in driver.title
    
    driver.quit()