from selenium.webdriver.common.by import By

class UserIndexPage:
    
    @staticmethod
    def username_drop_down(driver):
        return driver.find_element(By.XPATH, "//*[@id='settingsBox']/ul/li[3]/a")
    
    @staticmethod
    def logout_link(driver):
        return driver.find_element(By.LINK_TEXT, "Logout")
