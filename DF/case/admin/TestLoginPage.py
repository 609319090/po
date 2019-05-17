import unittest
from DF.page.admin.LoginPage import LoginPage
from selenium import webdriver

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')

        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)

        self.url="http://admin.joy.qa.psf-dev.com/admin/login"
        self.username="admin@psf.com"
        self.password="123456"


    def testLogin(self):

        loginPage=LoginPage(self.driver,self.url)

        loginPage.open(self.url)

        loginPage.input_username(self.username)

        loginPage.input_password(self.password)

        loginPage.click_btn()

        self.assertEqual(self.driver.title,'东方福利网管理后台')


    @classmethod
    def tearDown(self):
        return self


if __name__ =="__main__":
    unittest.main()






