
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.organization_related.OrganizationPage import OrganizationPage
from utilities.BaseClass import BaseClass
from selenium.common.exceptions import WebDriverException
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestOrganizationNotice(BaseClass):
    
    def delay(self, t=0.5):
        time.sleep(t)
        
    def fillNoticeField(self, organizationPage, topic, detail):
        organizationPage.enter_ins_field("Notice Topic", topic)
        self.delay()  
        organizationPage.enter_ins_textarea("Notice Details", detail, "placeholder")
        self.delay() 
        

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("topic, detail, previous", [
      PageData.getTestData("OrganizationNoticeData", "testcase1"),
      PageData.getTestData("OrganizationNoticeData", "testcase2"),
      PageData.getTestData("OrganizationNoticeData", "testcase3")
    ])
    def test_organization_add_notice(self, email, password, topic, detail, previous):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Notice Board")
      self.delay()
      organizationPage.click_viewNotice()
      self.delay()
      organizationPage.click_sidebar_child_button("Add Notice")
      self.delay()
      self.fillNoticeField(organizationPage, topic, detail)
      self.delay()
      organizationPage.click_ins_button("Create")
      self.delay()
      
      body_text = self.driver.find_element(By.TAG_NAME, "body").text
      assert "ERROR" not in body_text, "terjadi error pada halaman website ketika Create Data Notice"
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("topic, detail, previous", [
      PageData.getTestData("OrganizationNoticeData", "testcase4"),
      PageData.getTestData("OrganizationNoticeData", "testcase5"),
      PageData.getTestData("OrganizationNoticeData", "testcase6")
    ])
    def test_organization_edit_notice(self, email, password, topic, detail, previous):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Notice Board")
      self.delay()
      organizationPage.click_viewNotice()
      self.delay()
      organizationPage.click_notice_button_bar(previous, 2)
      self.delay()
      organizationPage.enter_ins_field("Enter your notice topic", topic)
      self.delay()  
      organizationPage.enter_ins_textarea("Enter your notice details", detail, "placeholder")
      self.delay() 
      organizationPage.click_ins_button("Update")
      self.delay()

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("topic, detail, previous", [
      PageData.getTestData("OrganizationNoticeData", "testcase4"),
      PageData.getTestData("OrganizationNoticeData", "testcase5"),
      PageData.getTestData("OrganizationNoticeData", "testcase6")
    ])
    def test_organization_view_notice(self, email, password, topic, detail, previous):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Notice Board")
      self.delay()
      organizationPage.click_viewNotice()
      self.delay()
      organizationPage.click_notice_button_bar(topic, 1)
      self.delay()

      try:
          WebDriverWait(self.driver, 60).until(
              EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{topic}']")),
              EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{detail}']"))
          )
          element_present = True
      except TimeoutError:
          element_present = False
      except NoSuchElementException:
          element_present = False

      assert element_present, "Topic atau detail notice tidak sesuai"


    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("topic, detail, previous", [
      PageData.getTestData("OrganizationNoticeData", "testcase4"),
      PageData.getTestData("OrganizationNoticeData", "testcase5"),
      PageData.getTestData("OrganizationNoticeData", "testcase6")
    ])
    def test_organization_delete_notice(self, email, password, topic, detail, previous):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Notice Board")
      self.delay()
      organizationPage.click_viewNotice()
      self.delay()
      organizationPage.click_notice_button_bar(topic)
      self.delay()
      organizationPage.click_ins_button("Yes, Delete It!")
      self.delay()

    


