import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def submit_form(driver):
    driver.find_element(By.ID, "first-name").send_keys("Travis")
    driver.find_element(By.ID, "last-name").send_keys("Mong")
    driver.find_element(By.ID, "job-title").send_keys("Developer")
    
    driver.find_element(By.ID, "radio-button-3").click()
    driver.find_element(By.ID, "checkbox-1").click()
    
    driver.find_element(By.ID, "select-menu").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
    
    driver.find_element(By.ID, "datepicker").send_keys("05/28/2022")
    driver.find_element(By.ID, "datepicker").send_keys(Keys.ENTER)
    
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()
    
def wait_for_alert(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))

class AllTogether(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def tearDown(self):
        self.driver.close()
    
    def test_automate_form(self):
        self.driver.get("https://formy-project.herokuapp.com/form")
        
        submit_form(self.driver)
        
        wait_for_alert(self.driver)
        
        assert wait_for_alert(self.driver).text == "The form was successfully submitted!"
    
if __name__ == '__main__':
    unittest.main()