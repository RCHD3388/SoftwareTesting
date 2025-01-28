
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from utilities.BaseClass import BaseClass


class TestRegister(BaseClass):
    
    def doRegister(self, email, code, first_name, mobile_number, last_name, password): 
      landingPage = LandingPage(self.driver)
      time.sleep(0.5)     

      # click go to login page
      landingPage.click_login_button()
      time.sleep(0.5)

      # click go to register page
      landingPage.click_register_button()
      time.sleep(0.5)

      landingPage.enter_register_field("email", email)
      time.sleep(0.5)
      landingPage.enter_code(code)
      time.sleep(0.5)
      landingPage.enter_register_field("mobile_number", mobile_number)
      time.sleep(0.5)
      landingPage.enter_register_field("first_name", first_name)
      time.sleep(0.5)
      landingPage.enter_register_field("last_name", last_name)
      time.sleep(0.5)
      landingPage.enter_register_field("password", password)
      time.sleep(0.5)


      # click register button
      landingPage.click_register_submit_button()
      
      # check register successfull
      assert landingPage.getRegisterToastMessage() == "Your registration is successful."
      
      time.sleep(2)

    @pytest.mark.parametrize("email, code, mobile_number, first_name, last_name, password", [
      PageData.getTestData("RegisterData", "testcase1"),
      PageData.getTestData("RegisterData", "testcase2")
    ])
    def test_register(self, email, code, first_name, mobile_number, last_name, password):
        self.doRegister(email, code, first_name, mobile_number, last_name, password)

