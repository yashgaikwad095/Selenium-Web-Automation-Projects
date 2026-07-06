from selenium import webdriver

# Function ka naam 'test_' se shuru kiya hai
def test_title_check():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")
    
    actual_title = driver.title
    expected_word = "Wikipedia"
    
    # ⚖️ PYTEST MAGIC: 'assert' keyword
    # Agar expected word actual title mein hai, toh PyTest isko PASS kar dega.
    # Agar nahi hai, toh fail karke error de dega. (Humein If/Else likhne ki zaroorat nahi)
    assert expected_word in actual_title
    
    driver.quit()