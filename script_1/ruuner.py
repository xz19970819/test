'''
@File:ruuner.py
@DateTime:2022/1/20 15:57 
@Author:eason 
@Desc:
'''
import unittest
from BeautifulReport import BeautifulReport
from script_1.config.config import report_dir,start_dir

# 加载测试用例
loader = unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
# 执行测试用例
suit = BeautifulReport(loader)
# 生成测试报告
suit.report(description="测试报告",filename="01版本测试报告",report_dir=report_dir)