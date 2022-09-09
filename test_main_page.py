import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(10)
