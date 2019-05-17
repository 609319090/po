from selenium.webdriver.common.by import By
from DF.page.BasePage import BasePage


class LoginPage(BasePage):
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    loginbtn_loc = (By.CLASS_NAME, 'btn-block')
    user_loc=(By.CLASS_NAME,'user-menu')

    def open(self,url):
        super().open(url)


    def islogin(self):
        if super().find_ele(*self.user_loc):
            return True
        else:
            return False

    def input_username(self,username):
        super().find_ele(*self.username_loc).send_keys(username)


    def input_password(self,password):
        super().find_ele(*self.password_loc).send_keys(password)


    def click_btn(self):
        super().find_ele(*self.loginbtn_loc).click()




