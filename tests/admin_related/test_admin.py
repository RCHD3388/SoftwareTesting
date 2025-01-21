
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.admin_related.AdminPage import AdminPage
from pageObjects.organization_related.OrganizationPage import OrganizationPage
from utilities.BaseClass import BaseClass
import os
from selenium.webdriver.common.action_chains import ActionChains

class TestOrganizationIns(BaseClass):
    

   

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    
    # def test_organization_from_admin(self, email, password):
    
    #   landingPage = LandingPage(self.driver)
    #   adminpage = AdminPage(self.driver)

    #   landingPage.doLogin(email, password)
    #   adminpage.click_manage_organization()
    #   adminpage.click_add_organization()
    #   time.sleep(4)
    #   adminpage.enter_ins_field("First Name", "new Organization")
    #   adminpage.enter_ins_field("Last Name", "new Organization")
    #   adminpage.enter_ins_field("Email", "organizationtest@gmail.com")
    #   adminpage.enter_ins_field("Password", "123456")
    #   adminpage.enter_ins_field("Professional Title", "Software Engineer")
    #   adminpage.enter_ins_field("Mobile Number", "1232349")
    #   adminpage.enter_ins_field("Address", "Los Altos, California(CA), 94024")
    #   adminpage.enter_ins_field("Postal Code", "94024")
    #   adminpage.enter_ins_field("https://facebook.com", "https://www.facebook.com/random")
    #   adminpage.enter_ins_field("https://twitter.com", "https://twitter.com/istts_sby")
    #   adminpage.enter_ins_field("https://linkedin.com", "https://id.linkedin.com/in/ryu-alvino-296953290")
    #   adminpage.enter_ins_field("https://pinterest.com", "https://www.pinterest.com/gutapresley/ferdinand/")
    #   time.sleep(0.5)
    #   adminpage.enter_ins_select_field("id", "country_id", "United States")
    #   time.sleep(0.5)
    #   adminpage.enter_ins_select_field("id", "gender", "Male")
    #   adminpage.enter_ins_select_field("id", "state_id", "California")
    #   adminpage.enter_ins_select_field("id", "city_id", "Acton")
    #   adminpage.enter_ins_select_field("name", "area_code", "BD(+88)")
    #   adminpage.enter_ins_textarea("about_me", "New Instructor here")
     
    #   adminpage.click_ins_button("Save")
      
    #   time.sleep(2)
    
    def test_instructor_from_admin(self, email, password):
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      
      landingPage.doLogin(email, password)
      adminpage.click_manage_instructor()
      adminpage.click_add_instructor()
      time.sleep(4)
      adminpage.enter_ins_field("First Name", "new Instructor")
      adminpage.enter_ins_field("Last Name", "new Instructor")
      adminpage.enter_ins_field("Email", "instructortest@gmail.com")
      adminpage.enter_ins_field("Password", "123456")
      adminpage.enter_ins_field("Professional Title", "Software Engineer")
      adminpage.enter_ins_field("Phone Number", "6969696")
      adminpage.enter_ins_field("Address", "Los Altos, California(CA), 94024")
      adminpage.enter_ins_field("Postal Code", "94024")
      adminpage.enter_ins_field("https://facebook.com", "https://www.facebook.com/random")
      adminpage.enter_ins_field("https://twitter.com", "https://twitter.com/istts_sby")
      adminpage.enter_ins_field("https://linkedin.com", "https://id.linkedin.com/in/ryu-alvino-296953290")
      adminpage.enter_ins_field("https://pinterest.com", "https://www.pinterest.com/gutapresley/ferdinand/")
      time.sleep(0.5)
      adminpage.enter_ins_select_field("id", "country_id", "United States")
      time.sleep(0.5)
      adminpage.enter_ins_select_field("id", "gender", "Male")
      adminpage.enter_ins_select_field("id", "state_id", "California")
      adminpage.enter_ins_select_field("id", "city_id", "Acton")
      adminpage.enter_ins_select_field("name", "area_code", "BD(+88)")
      adminpage.enter_ins_textarea("about_me", "New Instructor here")
     
      adminpage.click_ins_button("Save")
      
      time.sleep(2)
    




    

