from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pypi.org/project/selenium/")


# Getting by tag name
inp = driver.find_element(By.NAME, "q")
el = inp.get_attribute("placeholder")
print(el)

# Getting by id
button = driver.find_element(By.ID, value="submit")
print(button.size)

# Getting by Selector
documentaion_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget")


# Getting by xPath
some_link = driver.find_element(By.XPATH, value='//*[@id="introduction"]/table/tbody/tr[1]/td[2]/p/a')
