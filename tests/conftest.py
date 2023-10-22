from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators as Main


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

