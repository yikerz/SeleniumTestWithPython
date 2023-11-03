import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Synchronization(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def tearDown(self):
        self.driver.close()
    
    @unittest.skip("Cannot load google")
    def test_implicit_wait(self):
        self.driver.get("https://formy-project.herokuapp.com/autocomplete")
        
        autocomplete_field = self.driver.find_element(By.ID, "autocomplete")
        autocomplete_field.send_keys("1555 Park Blvd, Palo Alto, CA")
        
        self.driver.implicitly_wait(5)
        
        autocomplete_result = self.driver.find_element(By.CLASS_NAME, "pac-item")
        autocomplete_result.click()
    
    @unittest.skip("Cannot load google")
    def test_explicit_wait(self):
        self.driver.get("https://formy-project.herokuapp.com/autocomplete")
        
        autocomplete_field = self.driver.find_element(By.ID, "autocomplete")
        autocomplete_field.send_keys("1555 Park Blvd, Palo Alto, CA")
        
        wait = WebDriverWait(self.driver, 10)
        autocomplete_result = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pac-item")))
        
        autocomplete_result.click()
        
    def test_fluent_wait(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element(By.NAME, "q").send_keys("FDM Group" + Keys.ENTER)
        
        wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
        fb_link = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Facebook")))
        
        fb_link.click()
        
        
if __name__ == '__main__':
    unittest.main()
    