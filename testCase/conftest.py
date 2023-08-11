import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def setup():
    # options = Options()
    # options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    # TRY IN GIT REPOSITORY
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver
