
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.organization_related.OrganizationPage import OrganizationPage
from utilities.BaseClass import BaseClass
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestOrganizationConsultation(BaseClass):
    
    def delay(self, t=0.5):
        time.sleep(t)
        

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("current, old, textarea, result", [
      PageData.getTestData("OrganizationConsultData", "testcase1"),
      PageData.getTestData("OrganizationConsultData", "testcase2"),
      PageData.getTestData("OrganizationConsultData", "testcase3")
    ])
    def test_organization_consultation(self, email, password, current, old, textarea, result):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_head_button("8")
      self.delay()
      organizationPage.click_dashboard_consult()
      self.delay()

      # FIELD
      availinput = organizationPage.get_inputdashboard("inlineCheckbox1")
      availinput.click()
      self.delay()
      
      typeinput = organizationPage.get_inputdashboard("inlineCheckbox5")
      typeinput.click()
      self.delay()
      
      areainput = organizationPage.get_inputdashboard("consultancyArea2")
      areainput.click()
      self.delay()
      
      hourlyinput = organizationPage.get_inputdashboard("hourlyRate")
      self.driver.execute_script("arguments[0].value = arguments[1];", hourlyinput, current)
      self.delay()
      
      hourlyoldinput = organizationPage.get_inputdashboard("hourlyOldRate")
      self.driver.execute_script("arguments[0].value = arguments[1];", hourlyoldinput, old)
      self.delay()
      
      offlinestatusinput = organizationPage.get_inputdashboard("offlineStatus")
      self.driver.execute_script("arguments[0].checked = true;", offlinestatusinput)
      self.delay()
      
      textareadashboard = organizationPage.get_textareadashboard()
      self.driver.execute_script("arguments[0].value = arguments[1];", textareadashboard, textarea)
      self.delay()

      organizationPage.click_consultsubmit()

      self.delay()
      try:
          organizationPage.getToastMessage()
      except NoSuchElementException:
          assert result != "berhasil"
          return

      assert result == "berhasil"

      time.sleep(2)
        