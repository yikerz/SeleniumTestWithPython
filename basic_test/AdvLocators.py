import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class AdvLocators(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def tearDown(self):
        self.driver.close()
    
    def test_css_selector(self):
        self.driver.get("https://formy-project.herokuapp.com/")
        
        logo1 = self.driver.find_element(By.CSS_SELECTOR, "a#logo")
        logo2 = self.driver.find_element(By.CSS_SELECTOR, "a[id='logo']")
        assert logo1 == logo2
        
        nav = self.driver.find_element(By.CSS_SELECTOR, ".navbar.navbar-expand-lg.bg-light")
        print(id(nav))
        
if __name__ == '__main__':
    unittest.main()
    