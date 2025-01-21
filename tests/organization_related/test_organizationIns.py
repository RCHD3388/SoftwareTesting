
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

class TestOrganizationIns(BaseClass):
    def createInstructor(self, organizationPage, image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output):
      file_path = os.path.abspath(image)
      wait_time = 0.2
      file_path =file_path.replace("\\", "\\\\")
      time.sleep(wait_time)
      organizationPage.enter_ins_img_field(file_path)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("First Name", first_name)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Last Name", last_name)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Email", ins_email)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Password", ins_password)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Professional Title", prof_title)
      time.sleep(wait_time)
      organizationPage.enter_ins_select_field("name", "area_code", area)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Phone Number", mobile)
      time.sleep(wait_time)
      organizationPage.enter_ins_select_field("id", "country_id", country)
      time.sleep(wait_time)
      organizationPage.enter_ins_select_field("id", "state_id", state)
      time.sleep(wait_time)
      organizationPage.enter_ins_select_field("id", "city_id", city)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Address", address)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("Postal Code", postal)
      time.sleep(wait_time)
      organizationPage.enter_ins_select_field("id", "gender", gender)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("https://facebook.com", facebook)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("https://twitter.com", twitter)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("https://linkedin.com", linkedin)
      time.sleep(wait_time)
      organizationPage.enter_ins_field("https://pinterest.com", pinterest)
      time.sleep(wait_time)
      organizationPage.enter_ins_textarea("about_me", about)
      time.sleep(wait_time)

      organizationPage.click_ins_button("Save")
      time.sleep(wait_time)


      assert organizationPage.getToastMessage() == output
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase2")
    ])
    @pytest.mark.parametrize("image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output", [
      PageData.getTestData("OrganizationInstructorData", "testcase1"),
      PageData.getTestData("OrganizationInstructorData", "testcase2"),
      PageData.getTestData("OrganizationInstructorData", "testcase3"),
      PageData.getTestData("OrganizationInstructorData", "testcase4"),
      PageData.getTestData("OrganizationInstructorData", "testcase5"),
    ])
    def test_organization_add_instructor(self, email, password
      , image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output):
      landingPage = LandingPage(self.driver)
      organizationPage = OrganizationPage(self.driver)

      landingPage.doLogin(email, password)
      time.sleep(0.5)

      organizationPage.click_organization_panel_button()
      time.sleep(0.5)

      organizationPage.click_sidebar_head_button("2")
      time.sleep(0.5)
      organizationPage.click_sidebar_child_button("Add Instructor")
      time.sleep(0.5)

      # FIELD
      self.createInstructor(organizationPage, image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output)
      
      time.sleep(2) 
    
    




    

