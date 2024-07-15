from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")

# for Ids
ids = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in ids]

timeout = time.time() + 5
five_min = time.time() + 60*1  #5 min

while True:
    cookie.click()

    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store div b")

        # dictionary store items and price
        item_dict = {}
        for i in range(len(items) - 1):
            x = items[i].text.split()
            item_dict[item_ids[i]] = int(x[-1].replace(",", ""))
        print(item_dict)
        # current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # find affordable upgrades
        affordable_cost = {}
        for item, cost in item_dict.items():
            if cookie_count > cost:
                affordable_cost[cost] = item

        highest_price_affordable = max(affordable_cost)
        print(highest_price_affordable)
        to_purchase_id = affordable_cost[highest_price_affordable]

        driver.find_element(By.ID, value=to_purchase_id).click()
        # adding 5 sec more
        timeout = time.time() + 5

        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, value="cps").text
            print(cookie_per_s)
            break
