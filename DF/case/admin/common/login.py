from DF.page.admin.LoginPage import LoginPage

class Login(LoginPage):

    def __init__(self,driver):

        self.driver=driver
        self.url="http://admin.joy.qa.psf-dev.com/admin"
        self.username="admin@psf.com"
        self.password='123456'

    def log(self):
        print(self.url)
        super().open(self.url)
        if super().islogin():
            return self.driver
        else:
            super().input_username(self.username)
            super().input_password(self.password)
            super().click_btn()
            return self.driver




