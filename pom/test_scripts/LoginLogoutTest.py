import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.insert(0, r'C:\Users\Yik\Desktop\SeleniumPython\pom')
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.UserIndexPage import UserIndexPage
from data.data_file import *
from test_scripts.BaseTestCase import BaseTestCase

class LoginLogoutTest(BaseTestCase):
    
    def test_login_logout(self):
        self.driver.get(homeURL)
        
        if HomePage.sign_in_button(self.driver).is_displayed():
            HomePage.sign_in_button(self.driver).click()
        
        assert loginPageHeader == LoginPage.login_page_header(self.driver).text
        
        LoginPage.username_field(self.driver).send_keys(usr)
        LoginPage.password_field(self.driver).send_keys(psw)
        LoginPage.sign_in_button(self.driver).click()
        
        self.driver.back()
        
        assert usr == UserIndexPage.username_drop_down(self.driver).text
        
        UserIndexPage.username_drop_down(self.driver).click()
        
        if UserIndexPage.logout_link(self.driver).is_displayed():
            UserIndexPage.logout_link(self.driver).click()
        
        assert HomePage.sign_in_button(self.driver).is_displayed() == True
        
        