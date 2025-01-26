
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.SkenarioPasswordPage import SkenarioPasswordPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestSkenarioChangePassword(BaseClass):

    def delay(self, t=0.5):
        time.sleep(t)

    def gotopassPage(self, skenario_password_page, latestpassword):
      skenario_password_page.click_profile()
      self.delay()
      skenario_password_page.click_changepassword()
      self.delay()
      
      skenario_password_page.fillinput("password", latestpassword)
      skenario_password_page.fillinput("password_confirmation", latestpassword)
      self.delay()
      skenario_password_page.click_updatepassword()
      self.delay()

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    def test_skenario_password(self, email, password):
      landingPage = LandingPage(self.driver)
      skenario_password_page = SkenarioPasswordPage(self.driver)
      landingPage.doLogin(email, password)
      
      self.delay()
      
      self.gotopassPage(skenario_password_page, skenario_password_page.newpassword)

      assert skenario_password_page.getToastMessage() == "Password updated successfully."
      skenario_password_page.click_profile()
      self.delay()
      skenario_password_page.click_logout()
      self.delay()

      landingPage.doLogin(email, skenario_password_page.newpassword)

      try:
          skenario_password_page.getToastMessage()
          element_present = False
          assert element_present, "Password tidak terganti"
          return
      except NoSuchElementException:
          element_present = True

      self.gotopassPage(skenario_password_page, password)
      skenario_password_page.click_profile()
      self.delay()
      skenario_password_page.click_logout()
      self.delay()





      


