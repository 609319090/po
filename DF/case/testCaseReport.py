import unittest
from BeautifulReport import BeautifulReport
from DF.case.admin.goods.CaseCreateGoods import CaseCreateGoods

if __name__ == '__main__':
    # suite_tests = unittest.defaultTestLoader.discover(".",pattern="CaseCreateGoods.py",top_level_dir=None)
    # BeautifulReport(suite_tests).report(filename='东福测试报告', description='admin测试', log_path='.')
    suite_tests=unittest.defaultTestLoader.loadTestsFromNames(['testF','testG'],module=CaseCreateGoods)
    BeautifulReport(suite_tests).report(filename='单独用例',description='单个用例',log_path='.')
