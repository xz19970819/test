'''
@File:test_login.py
@DateTime:2022/1/20 14:39 
@Author:eason 
@Desc:
'''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from script_1.config.config import driver_path,driver_url,file,sheet
from script_1.deta.test_user import Table_user
from script_1.pageobjects.page_login import LoginPage

class TestCase(unittest.TestCase):

    def setUp(self):
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(driver_url)
        self.page = LoginPage(self.driver)
        self.dco1 = Table_user(file,sheet)
        self.red = self.dco1.read()
        print("打开浏览器")

    def tearDown(self):
        self.driver.quit()
        print("关闭浏览器")

    def test_login_success(self):
        '''登录成功'''
        sleep(2)
        self.page.type_username(self.red[0][0])
        self.page.type_password(self.red[0][1])
        self.page.click_button()
        sleep(2)
        self.assertIn(self.driver.title,"我的地盘 - 禅道",msg="验证正确的账号和密码，登录成功---failed")
        print("验证正确的账号和密码，登录成功---passed")

    def test_login_wrongpassword(self):
        '''错误密码登录失败'''
        sleep(2)
        self.page.type_username(self.red[1][0])
        self.page.type_password(self.red[1][1])
        self.page.click_button()
        sleep(2)
        alert=self.driver.switch_to.alert.text
        self.assertIn("失败",alert,msg="验证正确的账号和错误的密码，登录失败---failed")
        print("验证正确的账号和错误的密码，登录失败---passed")


    def test_login_empty_account(self):
        '''错误账号登录失败'''
        sleep(2)
        self.page.type_username(self.red[2][0])
        self.page.type_password(self.red[2][1])
        self.page.click_button()
        sleep(2)
        alert = self.driver.switch_to.alert.text
        self.assertIn("失败", alert, msg="验证错误的账号和正确的密码，登录失败---failed")
        print("验证错误的账号和正确的密码，登录失败---passed")


