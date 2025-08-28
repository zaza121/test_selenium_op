from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Optional, for special keys like Enter
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

# Initialize the Chrome WebDriver (ensure chromedriver is in your PATH or specify its path)

grid_url = "http://chrome_driver:4444/wd/hub"
chrome_options = Options()
# Add any desired options, e.g., chrome_options.add_argument("--headless")
#driver = webdriver.Chrome()
driver = Remote(command_executor=grid_url, options=chrome_options)

try:
    # Open a website
    driver.get("https://www.python.org")

    # Print the page title
    print(f"Page Title: {driver.title}")

    # Find the search bar by its name attribute
    # search_bar = driver.find_element(By.NAME, "q")

    # Type a search query and press Enter
    # search_bar.send_keys("Selenium Python tutorial" + Keys.RETURN)

    # Wait for a moment to see the results (optional, for demonstration)
    # driver.implicitly_wait(5)

    # Find and print the text of a specific element on the results page (example)
    # This part would depend on the actual structure of the search results page
    # result_element = driver.find_element(By.CSS_SELECTOR, "h3.LC20lb")
    # print(f"First search result: {result_element.text}")

finally:
    # Close the browser
    driver.quit()
