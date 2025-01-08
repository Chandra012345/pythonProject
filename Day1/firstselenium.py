from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

serv_obj = Service("C:\\Users\\hp\\Downloads\\geckodriver-v0.34.0-win-aarch64\\geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.quit()
print("Manish")

