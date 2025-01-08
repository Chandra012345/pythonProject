from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By




class TestLoginPage:
    def test_login_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        assert self.driver.title=="OrangeHRM"
        self.driver.quit()

    def test_login_edge(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_firfox(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

l=TestLoginPage()








