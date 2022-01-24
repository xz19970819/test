'''
@File:config.py
@DateTime:2022/1/21 17:37 
@Author:eason 
@Desc:
'''
import os

driver_path = "D:\B_python\script_1\driver\chromedriver.exe"

driver_path1= f"{os.getcwd()}\driver\chromedriver.exe"

driver_url = "http://139.224.113.59/zentao/user-login.html"
file =r"D:\B_python\script_1\deta\table_test.xlsx"
sheet = "Sheet1"
start_dir = r"D:\B_python\script_1\testcases"
report_dir = r"D:\B_python\script_1\report"


if __name__ == '__main__':
    print(driver_path)
    print(driver_path1)
