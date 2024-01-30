from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")

dict = {}
for index,el in enumerate(elements):
    row = el.text.split('\n')
    dict[index] = {
        "time" : row[0],
        "name" : row[1],
    }

print(dict)
