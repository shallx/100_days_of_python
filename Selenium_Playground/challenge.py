URL = "https://secure-retreat-92358.herokuapp.com/"

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)

fst_name = driver.find_element(By.NAME, value="fName").send_keys("Ananta")
lst_name = driver.find_element(By.NAME, value="lName").send_keys("Jamil")
email = driver.find_element(By.NAME, value="email").send_keys("example@email.com")
btn = driver.find_element(By.CLASS_NAME, value="btn").click()