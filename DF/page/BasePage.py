from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_ele(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda x : x.find_element(loc[0],loc[1]))
            return self.driver.find_element(loc[0],loc[1])
        except Exception as e:
            print("%s 元素找不到",loc[0])
            print(e)

    def find_eles(self,*loc):

        try:
            WebDriverWait(self.driver,10).until(lambda x : x.find_elements(loc[0],loc[1]))
            return self.driver.find_elements(loc[0],loc[1])
        except Exception as e:
            print("%s 元素找不到",loc[0])
            print(e)

    def switch_to_alert(self):
        self.driver.switch_to.alert.accept()

    def geturl(self):
        return self.driver.current_url

    def gettittle(self):
        return self.driver.title()





