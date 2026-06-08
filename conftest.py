
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from config import Config

@pytest.fixture
def driver(request):
    firefox_options = Options()
    firefox_options.page_load_strategy = 'normal'
    
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    
    request.addfinalizer(driver.quit)
    
    driver.get(Config.BASE_URL)
    return driver

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)