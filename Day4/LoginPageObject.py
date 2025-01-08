from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #Locators
    #constructor
    #action method
    txt_username_ID="Email"
    txt_pwd_ID="Password"
    button_submit_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        username_txt=self.driver.find_element(By.ID,self.txt_username_ID)
        username_txt.clear()
        username_txt.send_keys(username)

    def setPassword(self,pwd):
        pwd_txt = self.driver.find_element(By.ID, self.txt_pwd_ID)
        pwd_txt.clear()
        pwd_txt.send_keys(pwd)

    def clikLogin(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()