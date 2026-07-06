from selenium import webdriver
import pandas as pd
from io import StringIO
import time

print("Browser start ho raha hai...")
driver = webdriver.Chrome()

# 1. Wikipedia ka link
url = "https://en.wikipedia.org/wiki/Indian_Premier_League"
driver.get(url)
print("IPL Wikipedia Page Open Ho Gaya!")

time.sleep(3)

# 2. Page ka HTML data nikalna
page_source = driver.page_source
driver.quit()
print("Data extract ho raha hai, thoda wait karo...")

# 3. THE FIX: HTML text ko properly format karna taaki Pandas parse kar sake
html_data = StringIO(page_source)

# 4. Saari tables nikalna
all_tables = pd.read_html(html_data)

# 5. IPL Results wali specific table ko select karna (Index 2 par hoti hai)
ipl_results_table = all_tables[2] 

# 6. Excel (CSV) file banana
ipl_results_table.to_csv("IPL_History_Table.csv", index=False)

print("\n=======================================================")
print("🎯 BOOM! Poora IPL History Table 'IPL_History_Table.csv' mein save ho gaya!")
print("=======================================================\n")