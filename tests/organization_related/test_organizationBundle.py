
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

class TestOrganizationBundle(BaseClass):
    
    def delay(self, t=0.5):
        time.sleep(t)
        
    def createBundle(self, organizationPage, name, access, overview, price, status, image, output, buttonname="Create & Next"):
        organizationPage.enter_ins_field("Enter your bundles courses name", name)
        self.delay()  
        organizationPage.enter_ins_field("If there is no expiry duration, leave the field blank. ", access)
        self.delay()  
        organizationPage.enter_ins_textarea("Write your bundles courses overview", overview, "placeholder")
        self.delay()  
        organizationPage.enter_ins_field("Enter your price", price)
        self.delay()  
        organizationPage.enter_ins_select_field("name", "status", status)
        self.delay()  
        
        file_path = os.path.abspath(image)
        file_path =file_path.replace("\\", "/") # UNTUK MAC LINUX
        # file_path =file_path.replace("\\", "\\\\")
        self.delay()
        organizationPage.enter_ins_img_field(file_path)

        organizationPage.click_ins_button(buttonname)
        self.delay()

        assert organizationPage.getToastMessage() == output
        self.delay()

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("name, access, overview, price, status, image, output", [
      PageData.getTestData("OrganizationBundleData", "testcase1"),
      PageData.getTestData("OrganizationBundleData", "testcase2"),
      PageData.getTestData("OrganizationBundleData", "testcase3")
    ])
    def test_organization_add_bundle(self, email, password, name, access, overview, price, status, image, output):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Bundles Courses")
      self.delay()
      organizationPage.click_sidebar_child_button("Create Bundles Courses")
      self.delay()

      # FIELD
      self.createBundle(organizationPage, name, access, overview, price, status, image, output)
      self.delay()
      organizationPage.checked_all_coursebundle()
      time.sleep(0.5)
      organizationPage.click_done_bundle()

      time.sleep(2)

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    def test_delete_bundle(self, email, password):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Bundles Courses")
      self.delay()
      organizationPage.click_delete_bundle()
      self.delay()
      organizationPage.click_ins_button("Yes, Delete It!")
      self.delay()

      assert organizationPage.getToastMessage() == "Bundle deleted successfully"
      time.sleep(1)

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("name, access, overview, price, status, image, output", [
      PageData.getTestData("OrganizationBundleData", "testcase4")
    ])
    def test_edit_bundle(self, email, password, name, access, overview, price, status, image, output):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      self.delay()

      organizationPage.click_organization_panel_button()
      self.delay()

      organizationPage.click_sidebar_child_button("Bundles Courses")
      self.delay()
    
      editbutton = organizationPage.get_elms_a_classes("para-color font-14 font-medium d-flex align-items-center")[0]
      organizationPage.scrollTo(editbutton)
      time.sleep(0.5)
      editbutton.click()
      self.delay()
      
      # INPUT
      self.createBundle(organizationPage, name, access, overview, price, status, image, output, "Update & Next")
      self.delay()
      organizationPage.click_done_bundle()
      time.sleep(0.5)
      newname = organizationPage.getHeaderCardBundle().get_attribute("innerHTML")
      assert newname == name


      time.sleep(1)
        