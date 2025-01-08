import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCLI:
    def test_logo(self,setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(5)
        try:
            self.status = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-branding']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            assert self.status==True
            self.driver.close()
        except:
            self.driver.close()
            assert False