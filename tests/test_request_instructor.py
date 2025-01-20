from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.AdminPage import AdminPage
from pageObjects.StudentPage import StudentPage
from utilities.BaseClass import BaseClass
from pageObjects.LandingPage import LandingPage

class TestRequestInstructor(BaseClass):
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("firstName, lastName, phoneNumber, address, cv, bio, title", [
      PageData.getTestData("RequestInstructor", "testcase1")
    ])
    
    @pytest.mark.parametrize("firstName, lastName, phoneNumber, address, cv, bio, title", [
        PageData.getTestData("RequestInstructor", "testcase1"),
        PageData.getTestData("RequestInstructor", "testcase2"),
        # Add more test cases here
    ])
    def test_request_instructor(self, setup, email, password, firstName, lastName, phoneNumber, address, cv, bio, title):
      landingPage = LandingPage(self.driver)
      landingPage.doLogin(email, password)
      time.sleep(2)
      studentPage = StudentPage(self.driver)
      studentPage.doRequestInstructor(firstName, lastName, phoneNumber, address, cv, bio, title)
      time.sleep(2)
