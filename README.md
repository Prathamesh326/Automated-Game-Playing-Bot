
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
