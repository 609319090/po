from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from DF.case.admin.common.login import Login

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from DF.page.BasePage import BasePage
class PublishGoods(BasePage):

    #status
    status_loc=(By.NAME,'status')

    #search btn
    search_btn_loc=(By.ID,'search')

    #CHECKbox

    checkbox_loc=(By.CLASS_NAME,'icheckbox_minimal')



    #publish btn

    publish_btn_loc=(By.LINK_TEXT,'上架')


    #offline btn

    offline_btn_loc=(By.CLASS_NAME,'multi-offline-btn')

    #comfirm div



    def __init__(self,driver):

        self.driver=driver
        Login(self.driver).log()



    def select_publish_status(self):
        Select(super().find_ele(*self.status_loc)).select_by_value('2')


    def click_search_btn(self):
        super().find_ele(*self.search_btn_loc).click()

    def select_goods(self):
        handles1 = self.driver.current_window_handle
      #  print(handles1)
        super().find_eles(*self.checkbox_loc)[0].click()
        super().find_ele(*self.publish_btn_loc).click()

        try:
            time.sleep(10)
          #  handles2 = self.driver.window_handles
          #  print(handles2)
            # WebDriverWait(self.driver,10).until(EC.alert_is_present())
            super().switch_to_alert()
            time.sleep(2)
        except:
            print('找不到元素')







