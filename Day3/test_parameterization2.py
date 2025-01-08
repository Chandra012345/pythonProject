import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClass:
    @pytest.mark.parametrize('username,pwd',[("Admin","admin123"),("Admin","admin"),("admi","admin123"),("admin","admin")])
    def test_login(self,username,pwd):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\\Users\\hp\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
        breakpoint()
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            assert self.status==True
            self.driver.close()
        except:
            self.driver.close()
            assert False


