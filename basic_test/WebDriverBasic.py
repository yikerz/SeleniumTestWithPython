import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class WebDriverBasic(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.close()
        
    @unittest.skip("Pass")
    def test_keyboard_type_and_mouse_click(self):
        self.driver.get("https://formy-project.herokuapp.com/keypress")

        name_field = self.driver.find_element(By.ID, "name")
        name_field.click()
        name_field.send_keys("Travis Mong")

        button = self.driver.find_element(By.XPATH, "//*[contains(@id, 'button')]")
        button.click()

    @unittest.skip("Cannot load google")
    def test_autocomplete(self):
        self.driver.get("https://formy-project.herokuapp.com/keypress")

        autocomplete_field = self.driver.find_element(By.ID, "autocomplete")
        autocomplete_field.send_keys("1555 Park Blvd, Palo Alto, CA")

        autocomplete_result = self.driver.find_element(By.CLASS_NAME, "pac-item")
        autocomplete_result.click()

    @unittest.skip("Pass")
    def test_scroll(self):
        self.driver.get("https://formy-project.herokuapp.com/scroll")
        name_field = self.driver.find_element(By.ID, "name")

        actions = ActionChains(self.driver)
        actions.move_to_element(name_field).perform()
        
        name_field.send_keys("Travis Mong")
        
        date_field = self.driver.find_element(By.ID, "date")
        date_field.send_keys("01/01/2020")
    
    @unittest.skip("Pass")
    def test_switch_window(self):
        self.driver.get("https://formy-project.herokuapp.com/switch-window")
        
        new_tab_button = self.driver.find_element(By.ID, "new-tab-button")
        new_tab_button.click()
        
        original_window = self.driver.current_window_handle
        
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
                
        self.driver.switch_to.window(original_window)
    
    @unittest.skip("Pass")
    def test_switch_alert(self):
        self.driver.get("https://formy-project.herokuapp.com/switch-window")
        
        alert_button = self.driver.find_element(By.ID, "alert-button")
        alert_button.click()
        
        alert = self.driver.switch_to.alert
        alert.accept()
    
    @unittest.skip("Pass")
    def test_run_js(self):
        self.driver.get("https://formy-project.herokuapp.com/modal")
        
        modal_button = self.driver.find_element(By.ID, "modal-button")
        modal_button.click()
        
        close_button = self.driver.find_element(By.XPATH, "//*[contains(@class,'modal-footer')]//button[text()='Close']")
        self.driver.execute_script("arguments[0].click();", close_button)
    
    def test_drag_drop(self):
        self.driver.get("https://formy-project.herokuapp.com/dragdrop")
        
        image = self.driver.find_element(By.ID, "image")
        box = self.driver.find_element(By.ID, "box")
                
        actions = ActionChains(self.driver)
        actions.drag_and_drop(image, box).perform()
        
            
if __name__ == '__main__':
    unittest.main()