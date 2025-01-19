
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    
    def doLogin(self, username, password): 
      landingPage = LandingPage(self.driver)
      time.sleep(2)    

      # click go to login page
      landingPage.click_login_button()
      time.sleep(0.5)

      # enter username
      landingPage.enter_username(username)
      time.sleep(0.5)
      # enter password
      landingPage.enter_password(password)
      time.sleep(0.5)
      # click login button
      landingPage.click_login_submit_button()
      time.sleep(2)

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    def test_login(self, email, password):
        self.doLogin(email, password)

