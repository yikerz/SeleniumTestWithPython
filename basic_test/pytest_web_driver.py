import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest

# Run pytest <test_file.py> --html=report.html to generate report in html format

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

def test_keyboard_type_and_mouse_click(driver):
    driver.get("https://formy-project.herokuapp.com/keypress")

    name_field = driver.find_element(By.ID, "name")
    name_field.click()
    name_field.send_keys("Travis Mong")

    button = driver.find_element(By.XPATH, "//*[contains(@id, 'button')]")
    button.click()

@unittest.skip("Cannot load google")
def test_autocomplete(driver):
    driver.get("https://formy-project.herokuapp.com/keypress")

    autocomplete_field = driver.find_element(By.ID, "autocomplete")
    autocomplete_field.send_keys("1555 Park Blvd, Palo Alto, CA")

    autocomplete_result = driver.find_element(By.CLASS_NAME, "pac-item")
    autocomplete_result.click()

def test_scroll(driver):
    driver.get("https://formy-project.herokuapp.com/scroll")
    name_field = driver.find_element(By.ID, "name")

    actions = ActionChains(driver)
    actions.move_to_element(name_field).perform()
    
    name_field.send_keys("Travis Mong")
    
    date_field = driver.find_element(By.ID, "date")
    date_field.send_keys("01/01/2020")

def test_switch_window(driver):
    driver.get("https://formy-project.herokuapp.com/switch-window")
    
    new_tab_button = driver.find_element(By.ID, "new-tab-button")
    new_tab_button.click()
    
    original_window = driver.current_window_handle
    
    for window in driver.window_handles:
        driver.switch_to.window(window)
            
    driver.switch_to.window(original_window)

def test_switch_alert(driver):
    driver.get("https://formy-project.herokuapp.com/switch-window")
    
    alert_button = driver.find_element(By.ID, "alert-button")
    alert_button.click()
    
    alert = driver.switch_to.alert
    alert.accept()

def test_run_js(driver):
    driver.get("https://formy-project.herokuapp.com/modal")
    
    modal_button = driver.find_element(By.ID, "modal-button")
    modal_button.click()
    
    close_button = driver.find_element(By.XPATH, "//*[contains(@class,'modal-footer')]//button[text()='Close']")
    driver.execute_script("arguments[0].click();", close_button)

def test_drag_drop(driver):
    driver.get("https://formy-project.herokuapp.com/dragdrop")
    
    image = driver.find_element(By.ID, "image")
    box = driver.find_element(By.ID, "box")
            
    actions = ActionChains(driver)
    actions.drag_and_drop(image, box).perform()
