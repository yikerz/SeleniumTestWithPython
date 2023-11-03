from selenium.webdriver.common.by import By

class LoginPage:
    
    @staticmethod
    def username_field(driver):
        return driver.find_element(By.NAME, "user_login")
    
    @staticmethod
    def password_field(driver):
        return driver.find_element(By.NAME, "user_password")
    
    @staticmethod
    def sign_in_button(driver):
        return driver.find_element(By.NAME, "submit")
    
    @staticmethod
    def login_page_header(driver):
        return driver.find_element(By.TAG_NAME, "h3")