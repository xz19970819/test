'''
@File:page_login.py
@DateTime:2022/1/21 14:14 
@Author:eason 
@Desc:
'''

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.account = By.ID,"account"
        self.password = By.NAME,"password"
        self.button = By.ID,"submit"
        self.driver = driver
    def type_username(self,username):
        self.driver.find_element(*self.account).send_keys(username)

    def type_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)
    def click_button(self):
        self.driver.find_element(*self.button).click()

