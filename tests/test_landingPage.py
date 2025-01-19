
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    
    def doLogin(self): 
      landingPage = LandingPage(self.driver)
      time.sleep(2)    

      landingPage.click_login_button()
      time.sleep(2)

    def test_login(self):
        self.doLogin()

