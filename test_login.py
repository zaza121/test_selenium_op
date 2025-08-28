from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Optional, for special keys like Enter
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

class TestLogin():
    def setup_method(self, method):
        # Initialize the Chrome WebDriver (ensure chromedriver is in your PATH or specify its path)
        grid_url = "http://chrome_driver:4444/wd/hub"
        chrome_options = Options()
        # Add any desired options, e.g., chrome_options.add_argument("--headless")
        #driver = webdriver.Chrome()
        driver = Remote(command_executor=grid_url, options=chrome_options)
        self.driver = driver
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
    
        # Open a website
        # driver.get("https://www.python.org")
        self.driver.get("http://146.59.110.97:8083/web/database/selector")
        self.driver.set_window_size(602, 743)
        self.driver.implicitly_wait(4000000)
    
        # select database
        self.driver.find_element(By.LINK_TEXT, "21_07_2025").click()
        self.driver.implicitly_wait(5000000)
    
        # set credentials
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "login").send_keys("contact@sammi.mc")
        self.driver.find_element(By.CSS_SELECTOR, ".field-login").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("odoo2023!")
        self.driver.find_element(By.CSS_SELECTOR, ".mb-3:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.implicitly_wait(8000000)
    
        # Print the page title
        print(f"Page Title: {self.driver.title}")
        assert self.driver.title == "Odoo"

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

