from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from LoginPageObject import LoginPage

class TestLogin:
    def test_login(self):
        self.serv_obj = Service("C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clikLogin()
        self.title=self.driver.title
        self.driver.close()

        assert self.title=="Dashboard / nopCommerce administration"