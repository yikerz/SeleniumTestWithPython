import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ComponentInteractions(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def tearDown(self):
        self.driver.close()
    
    @unittest.skip("Pass")
    def test_radio_button(self):
        self.driver.get("https://formy-project.herokuapp.com/radiobutton")
        
        self.driver.find_element(By.ID, "radio-button-1").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='option2']").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/input").click()
        
    @unittest.skip("Pass")
    def test_date_picker(self):
        self.driver.get("https://formy-project.herokuapp.com/datepicker")
        
        date_field = self.driver.find_element(By.ID, "datepicker")
        date_field.click()
        date_field.send_keys("03/03/2024")
        date_field.send_keys(Keys.ENTER)
    
    @unittest.skip("Pass")
    def test_drop_down(self):
        self.driver.get("https://formy-project.herokuapp.com/dropdown")
        
        drop_down_menu = self.driver.find_element(By.ID, "dropdownMenuButton")
        drop_down_menu.click()
        autocomplete_item = self.driver.find_element(By.ID, "autocomplete")
        autocomplete_item.click()
        
    def test_file_upload(self):
        self.driver.get("https://formy-project.herokuapp.com/fileupload")
        
        upload_field = self.driver.find_element(By.ID, "file-upload-field")
        upload_field.send_keys("passport.jpg")
        
            
if __name__ == '__main__':
    unittest.main()