
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from utilities.BaseClass import BaseClass


class TestOrganization(BaseClass):
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    def test_organization(self, email, password):
      landingPage = LandingPage(self.driver)
      landingPage.doLogin(email, password)

    

