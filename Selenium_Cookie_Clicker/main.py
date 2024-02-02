URL = "https://orteil.dashnet.org/experiments/cookie/"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)
cookie = driver.find_element(By.ID, value="cookie")



def to_number(str : str):
    return int(str.strip().replace(",", ""))

def buy_something():
    money = to_number(driver.find_element(by=By.ID, value="money").text)
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    items.pop(-1)
    # prices = [{"price": to_number(item.text.split("-")[1]), "item" : item} for item in items]

    print(money)
    try:
        for item in items[:-1]:
            item_price = to_number(item.text.split("-")[1])
            if money >= item_price:
                item.click()
                money-=item_price
    except Exception as e:
        print(e.__context__)
    # if pric



while 1:
    timeout = time.time() + 3
    for i in range(500):
        cookie.click()
        if time.time() > timeout:
            buy_something()
            break



driver.quit()