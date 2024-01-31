URL = "https://orteil.dashnet.org/experiments/cookie/"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)
cookie = driver.find_element(By.ID, value="cookie")
timeout = time.time() + 3

# Finding prices
items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
items.pop(-1)
prices = [int(item.text.split("-")[1].strip().replace(",", "")) for item in items]


def to_number(str : str):
    return str.strip().replace(",", "")

def buy_something():
    money = to_number(driver.find_element(by=By.ID, value="money").text)
    # if pric


while 1:

    for i in range(500):
        cookie.click()
        if time.time() > timeout:
            break



driver.quit()