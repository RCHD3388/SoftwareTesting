
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.admin_related.AdminPage import AdminPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from pageObjects.organization_related.OrganizationPage import OrganizationPage
from utilities.BaseClass import BaseClass
import os
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.admin_related.ManageAdminPage import ManageAdminPage
class TestAdminOrganization(BaseClass):
    

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("first, last, email_org, password_org, title, phone, address, postal, facebook, twitter, linkedin, pinterest, country, gender, state, city, area, about,msg", [
      PageData.getTestData("OrganizationData", "orgcase1")
    ])

    def test_organization_from_admin(self, email, password, first, last, email_org, password_org, title, phone, address, postal, facebook, twitter, linkedin, pinterest, country, gender, state, city, area, about,msg):
    
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)

      landingPage.doLogin(email, password)
      adminpage.click_manage_organization()
      adminpage.click_add_organization()
      time.sleep(4)
      adminpage.enter_ins_field("First Name", first)
      adminpage.enter_ins_field("Last Name", last)
      adminpage.enter_ins_field("Email", email_org)
      adminpage.enter_ins_field("Password", str(password_org))
      adminpage.enter_ins_field("Professional Title", title)
      adminpage.enter_ins_field("Mobile Number", phone)
      adminpage.enter_ins_field("Address", address)
      adminpage.enter_ins_field("Postal Code", postal)
      adminpage.enter_ins_field("https://facebook.com", facebook)
      adminpage.enter_ins_field("https://twitter.com", twitter)
      adminpage.enter_ins_field("https://linkedin.com", linkedin)
      adminpage.enter_ins_field("https://pinterest.com", pinterest)
      time.sleep(0.5)
      adminpage.enter_ins_select_field("id", "country_id", country)
      time.sleep(0.5)
      adminpage.enter_ins_select_field("id", "gender", gender)
      adminpage.enter_ins_select_field("id", "state_id", state)
      adminpage.enter_ins_select_field("id", "city_id", city)
      adminpage.enter_ins_select_field("name", "area_code", area)
      adminpage.enter_ins_textarea("about_me", about)
     
      adminpage.click_ins_button("Save")
      organizationPage = OrganizationPage(self.driver)
      time.sleep(2) 
      assert organizationPage.getToastMessage() == msg
      time.sleep(2)

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("org_password", [
      PageData.getTestData("EditOrgData", "orgeditdata1")
    ])
    
    def test_edit_organization(self, email, password, org_password):
      waktu = 1
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      landingPage.doLogin(email, password)  
      instructorpage = InstructorPage(self.driver)
      time.sleep(waktu)
      instructorpage.click_button("Allow cookies")
      time.sleep(waktu)
      adminpage.click_manage_organization()
      time.sleep(waktu)
      adminpage.click_all_organizations()
      time.sleep(waktu)
      adminpage.click_edit_instructor()
      
      
      time.sleep(waktu)
      adminpage.enter_ins_field("Password",str(org_password))
   
      adminpage.click_ins_button("Save")
      
      time.sleep(30)
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    def test_delete_organization_from_admin(self, email, password):
      waktu = 1
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      manageadmin = ManageAdminPage(self.driver)
      landingPage.doLogin(email, password)
      instructorpage = InstructorPage(self.driver)
      time.sleep(waktu)
      instructorpage.click_button("Allow cookies")
      time.sleep(waktu)
      adminpage.click_manage_organization()
      time.sleep(waktu)
      adminpage.click_all_organizations()
      time.sleep(waktu)
      adminpage.click_delete_instructor()
      time.sleep(waktu)
      adminpage.click_confirm_delete()
      time.sleep(5)


    

