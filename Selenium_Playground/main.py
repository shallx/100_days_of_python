from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pypi.org/project/selenium/")
inp = driver.find_element(By.NAME, "q")
print(inp.get_attribute("placeholder"))