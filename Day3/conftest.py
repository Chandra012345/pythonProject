import pytest

from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\\Users\\hp\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\\Users\\hp\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

