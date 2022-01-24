'''
@File:test_user.py
@DateTime:2022/1/20 14:40 
@Author:eason 
@Desc:
'''

import unittest

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("打开浏览器")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")

    def setUp(self):
        print("登入账号")

    def tearDown(self):
        print("登出账号")

    def test_adduser(self):
        print("添加用户")

    def test_deleteuser(self):
        print("删除用户")

    def test_showuser(self):
        print("查看用户")
