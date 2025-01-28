
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from utilities.BaseClass import BaseClass

class TestLogin(BaseClass):

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    def test_login(self, email, password):
      landingPage = LandingPage(self.driver)
      landingPage.doLogin(email, password)

