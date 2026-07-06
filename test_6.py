from selenium import webdriver

def test_wikipedia_title():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")

    # 1. ACTUAL RESULT: Title nikalna
    actual_title = driver.title 

    # 2. EXPECTED RESULT: Jo humein chahiye
    expected_word = "Wikipedia"

    # 3. ⚖️ ASSERTION (The Real Test)
    # Agar ye condition false hoti hai, toh PyTest automatically test ko FAIL kar dega.
    assert expected_word in actual_title
    
    driver.quit()