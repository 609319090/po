from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from DF.case.admin.common.login import *
from DF.page.BasePage import BasePage


class GoodsPage(BasePage):



   #供应商
    merchant_loc = (By.ID,'merchant-select')

    merchant_search_loc=(By.CLASS_NAME,'select2-search__field')

    #频道
    channel_loc = (By.ID,'channel-select')

    #商品名称
    goods_name_loc = (By.ID,'name')

    #商品英文名
    good_enname_loc = (By.ID,'en_name')

    #副标题
    goods_subtitile_loc=(By.ID,'subtitle')

    #英文副标题
    goods_en_subtitile_loc=(By.ID,'en_subtitle')


    #商品编号
    goods_code_loc= (By.ID,'goods_code')

    #礼包备用code
    backup_code_loc = (By.ID,'backup_code')

    #父分类
    first_category_loc = (By.ID,'parent-category-select')

    #子分类
    second_category_loc = (By.ID,'category-select')

    #仓库
    warehouse_loc = (By.NAME,'warehouses[]')

    #提交按钮
    btn_loc = (By.CLASS_NAME,'btn-primary')

   #价格tab
    price_tab_loc=(By.LINK_TEXT,'价格信息')

   #规格名称
    spec_name_loc=(By.ID,'spec_name')

   #规格库存
    spec_inventory_loc=(By.ID,'spec_inventory')

   #规格价格
    spec_price_loc=(By.ID,'spec_price')

   #规格结算价
    spec_mer_price_loc=(By.ID,'spec_mer_price')


   #规格市场价
    spec_market_price_loc=(By.ID,'spec_market_price')

   #规格供应商货号
    codes_loc=(By.NAME,'codes')

   #添加按钮
    spec_add_btn_loc=(By.ID,'spec-add-btn')

   #pic tab
    pic_tab_loc=(By.LINK_TEXT,'商品图片')


    #upload img btn
    upload_img_btn_loc=(By.NAME,'image')

   #SAVA btn
    save_btn_loc=(By.CLASS_NAME,'btn-primary')

   #return list
    return_btn_loc=(By.LINK_TEXT,'返回')

    def __init__(self,driver):
        self.driver=driver
        Login(self.driver).log()


    def open(self,url):
        super().open(url)


    #输入merchant
    def input_merchant(self,merchant):
        ele = super().find_ele(*self.merchant_loc)

        Select(ele).select_by_value(merchant)




    def input_channel(self):
        ele=super().find_ele(*self.channel_loc)

        Select(ele).select_by_index(1)


    def input_goods_name(self,goods_name):
        super().find_ele(*self.goods_name_loc).send_keys(goods_name)


    def input_goods_code(self,goods_code):
        super().find_ele(*self.goods_code_loc).send_keys(goods_code)


    def input_first_category(self, first_category):
        ele=super().find_ele(*self.first_category_loc)

        Select(ele).select_by_value(first_category)



    def input_second_category(self,second_category):
        ele=super().find_ele(*self.second_category_loc)

        Select(ele).select_by_value(second_category)


    def input_warehouse(self):
        super().find_ele(*self.warehouse_loc).click()

       #保存按钮
    def click_btn(self):
        super().find_ele(*self.btn_loc).click()


    #点击价格tab
    def click_price_page(self):
        super().find_ele(*self.price_tab_loc).click()

    #输入规格

    def input_spec_name(self,spec_name):
        super().find_ele(*self.spec_name_loc).send_keys(spec_name)

    #输入库存

    def input_spec_inventory(self,spec_inventory):
        super().find_ele(*self.spec_inventory_loc).send_keys(spec_inventory)


    #输入价格

    def input_spec_price(self,price):
        super().find_ele(*self.spec_price_loc).send_keys(price)

    #输入结算价

    def input_spec_mer_price(self,mer_price):
        super().find_ele(*self.spec_mer_price_loc).send_keys(mer_price)

    #输入市场价
    def input_market_price(self,market_price):
        super().find_ele(*self.spec_market_price_loc).send_keys(market_price)

    #供应商货号
    def input_code(self,code):
        super().find_ele(*self.codes_loc).send_keys(code)

    #保存

    def spec_add_btn(self):
        super().find_ele(*self.spec_add_btn_loc).click()


    #点击图片tab
    def click_img_tab(self):
        super().find_ele(*self.pic_tab_loc).click()


    #上传图片
    def upload_img(self):
        super().find_ele(*self.upload_img_btn_loc).send_keys('D:\\Image\\3.jpg')

    #点击保存
    def save_btn(self):
        super().find_eles(*self.save_btn_loc)[2].click()


    #点击返回
    def return_btn(self):
        super().find_ele(*self.return_btn_loc).click()
