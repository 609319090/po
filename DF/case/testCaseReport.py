import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover(".",pattern="Case*.py",top_level_dir=None)
    BeautifulReport(suite_tests).report(filename='东福测试报告', description='admin测试', log_path='.')