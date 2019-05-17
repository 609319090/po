import unittest
from selenium import webdriver
from DF.page.admin.goods.CreateGoodsPage import *
import time

class CaseCreateGoods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.goodPage=GoodsPage(self.driver)
        self.url="http://admin.joy.qa.psf-dev.com/admin/goods/delivery/create"




    def testCreateGoods(self):
        self.goodPage.open(self.url)

        self.goodPage.input_merchant('635')


        self.goodPage.input_channel()

        self.goodPage.input_goods_name('测试商品'+ time.strftime("%Y%m%d %H%M%S", time.localtime()))

        self.goodPage.input_goods_code(time.strftime("%Y%m%d %H%M%S", time.localtime()))

        self.goodPage.input_first_category('454')
        time.sleep(2)

        self.goodPage.input_second_category('455')

        self.goodPage.input_warehouse()

        self.goodPage.click_btn()

        self.goodPage.click_price_page()

        self.goodPage.input_spec_name('100g')

        self.goodPage.input_spec_inventory('100')

        self.goodPage.input_spec_price('6')

        self.goodPage.input_spec_mer_price('5')

        self.goodPage.input_market_price('10')

        self.goodPage.input_code(time.strftime("%Y%m%d %H%M%S", time.localtime()))

        self.goodPage.spec_add_btn()

        time.sleep(2)

        self.goodPage.click_img_tab()
        time.sleep(2)

        self.goodPage.upload_img()

        self.goodPage.save_btn()
        time.sleep(2)

        self.goodPage.return_btn()

        time.sleep(2)
        url=self.goodPage.geturl()
        print(url)

        # self.assertEqual(url,'http://admin.joy.qa.psf-dev.com/admin/goods/delivery')


    @classmethod
    def tearDownClass(self):
        # self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()
