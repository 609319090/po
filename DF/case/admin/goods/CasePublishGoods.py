import unittest
from selenium import webdriver

# import sys
#
# sys.path.append('./page/admin/goods')
from DF.page.admin.goods.PublishGoods import PublishGoods



class CasePublishGoods(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome()

        self.publishGoods = PublishGoods(self.driver)

        self.url1 = 'http://admin.joy.qa.psf-dev.com/admin/goods/delivery'

    def testPublishGoods(self):
        self.publishGoods.open(self.url1)

        self.publishGoods.select_publish_status()

        self.publishGoods.click_search_btn()

        self.publishGoods.select_goods()

        self.assertEqual(self.publishGoods.geturl(),'http://admin.joy.qa.psf-dev.com/admin/goods/delivery')




    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':

    unittest.main()








