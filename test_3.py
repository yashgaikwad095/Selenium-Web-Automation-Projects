from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_wikipedia_search():
    driver = webdriver.Chrome()

    # 1. Wikipedia par jao
    driver.get("https://www.wikipedia.org")

    # 2. Search box dhundho aur type karo
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Indian Premier League")
    search_box.send_keys(Keys.RETURN)

    # Page load hone ka wait
    time.sleep(3)

    # 3. Data extract karna
    heading = driver.find_element(By.ID, "firstHeading")

    # 4. ⚖️ ASSERTION: Check karo ki sahi page khula ya nahi
    assert "Indian Premier League" in heading.text
    
    driver.quit()