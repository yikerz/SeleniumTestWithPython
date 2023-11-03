from selenium.webdriver.common.by import By

class HomePage:
    
    @staticmethod
    def sign_in_button(driver):
        return driver.find_element(By.ID, "signin_button")
    
    @staticmethod
    def zeroBankLink(driver):
        return driver.find_element(By.LINK_TEXT, "Zero Bank")
    