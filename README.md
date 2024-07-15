
# Cookie Clicker Automation Script

This repository contains a Python script that automates the Cookie Clicker game using Selenium WebDriver. The script continuously clicks the cookie, purchases the most expensive affordable upgrade every 5 seconds, and stops after 5 minutes, displaying the cookies per second rate.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Prathamesh326/Automated-Game-Playing-Bot.git
   cd Automated-Game-Playing-Bot
   ```

2. **Install the required packages:**

   ```sh
   pip install selenium
   ```

3. **Download Chrome WebDriver:**

   Download the appropriate version of Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your PATH or the same directory as your script.

## Usage

1. **Run the script:**

   ```sh
   python main.py
   ```

2. **The script will:**
   - Open the Cookie Clicker game in a Chrome browser.
   - Continuously click the cookie.
   - Every 5 seconds, check the available upgrades and purchase the most expensive affordable one.
   - Stop after 5 minutes and print the cookies per second rate.

## Code Explanation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")

# for Ids
ids = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in ids]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 min

while True:
    cookie.click()

    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store div b")

        # dictionary to store items and price
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
```

- **chrome_options = webdriver.ChromeOptions()**: Initializes Chrome options.
- **driver = webdriver.Chrome()**: Creates a new instance of the Chrome driver.
- **driver.get("https://orteil.dashnet.org/experiments/cookie/")**: Navigates to the Cookie Clicker game.
- **cookie = driver.find_element(By.ID, value="cookie")**: Locates the cookie button.
- **item_ids**: List of IDs for all the upgrade items.
- **timeout**: Time limit for the next upgrade check.
- **five_min**: Total run time limit of 5 minutes.
- **while True**: Main loop for clicking the cookie and purchasing upgrades.
- **item_dict**: Dictionary storing items and their prices.
- **cookie_count**: Current number of cookies.
- **affordable_cost**: Dictionary of affordable upgrades.
- **highest_price_affordable**: Most expensive affordable upgrade.
- **cookie_per_s**: Cookies per second rate displayed after 5 minutes.

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file further as per your needs.
