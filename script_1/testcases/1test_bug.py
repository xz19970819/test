'''
@File:test_bug.py
@DateTime:2022/1/20 16:22 
@Author:eason 
@Desc:
'''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from script_1.config.config import driver_path1,driver_url
from script_1.deta.test_user import Table_user
import win32gui
import win32con

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service(driver_path1)
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.get(driver_url)

        print("打开浏览器")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("关闭浏览器")

    def setUp(self):
        sleep(2)
        self.driver.find_element(By.NAME, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()
        print("登录账号")

    def tearDown(self):
        sleep(2)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'shelly')]").click()
        self.driver.find_element(By.LINK_TEXT,"退出").click()
        print("登出账号")
#测试用例1
    # def test_login_success(self):
    #     '''成功添加bug'''
    #     sleep(2)
    #     self.driver.find_element(By.LINK_TEXT, "测试").click()
    #     sleep(2)
    #     self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
    #     self.driver.find_element(By.LINK_TEXT, "提Bug").click()
    #     sleep(2)
    #     self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/div[1]/div[1]/ul[1]").click()
    #     self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
    #     self.driver.find_element(By.NAME, "title").send_keys("03")
    #     js = "var q=document.documentElement.scrollTop=10000"
    #     self.driver.execute_script(js)
    #     self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
    #     sleep(2)
    #     dialog = win32gui.FindWindow("#32770", "打开")
    #     combo_32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    #     combobox = win32gui.FindWindowEx(combo_32, 0, "ComboBox", None)
    #     edit = win32gui.FindWindowEx(combobox, 0, "Edit", None)
    #     button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
    #     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"D:\1.jpg")
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #     sleep(2)
    #     self.driver.find_element(By.ID, "submit").click()
    #     sleep(2)
    #     self.assertTrue(self.driver.find_element(By.LINK_TEXT,"提Bug"),msg="添加bug成功-----failed")
    #     print("添加bug成功-----passed")

# 测试用例2
#     def test_bug_confirm(self):
#         '''确认bug'''
#         sleep(2)
#         self.driver.find_element(By.LINK_TEXT, "测试").click()
#         sleep(2)
#         self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
#         self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[1]/i[1]").click()
#         sleep(2)
#         self.driver.switch_to.frame("iframe-triggerModal")
#         sleep(2)
#         self.driver.find_element(By.ID,"submit").click()
#         self.driver.switch_to.default_content()
#         sleep(2)
#         self.assertTrue(self.driver.find_element(By.LINK_TEXT,"提Bug"),msg="确认bug成功-----failed")
#         print("确认bug成功-----passed")

# 测试用例3
    def test_bug_solve(self):
        '''解决bug'''
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[2]/i[1]").click()
        sleep(2)
        self.driver.switch_to.frame("iframe-triggerModal")  #进入弹窗页
        print("1")
        sleep(2)
        # select=self.driver.find_element(By.ID,"resolution")  #定位select
        # Select(select).select_by_value("bydesign")         #选择value为bydesign的元素
        # Select(select).select_by_visible_text("重复Bug")
        self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/div[1]/a[1]/span[1]").click()
        sleep(3)
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/a[1]/div[2]/input[1]").send_keys("已解决")
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/a[1]/div[2]/input[1]").send_keys(Keys.ENTER)
        print("2")
        sleep(2)
        self.driver.find_element(By.XPATH,"//tbody/tr[3]/td[2]/div[1]/div[1]/a[1]").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()


        print("2")
        self.driver.find_element(By.ID, "submit").click()  #点击保存
        print("3")
        self.driver.switch_to.default_content()
        sleep(2)
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "提Bug"), msg="解决bug成功-----failed")
        print("解决bug成功-----passed")

