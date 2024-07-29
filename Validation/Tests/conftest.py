import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and PATH is set
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
