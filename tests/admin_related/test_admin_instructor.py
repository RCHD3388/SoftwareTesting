
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
class TestAdmin(BaseClass):
    

   

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    
    @pytest.mark.parametrize("fn, ln, email_instructor, password_insturctor, title, postal_code, pn, address, area_code, country, state, city, gender, facebook, twitter, linkedin, pinterest, about, msg", [
      PageData.getTestData("AdminInstructorIns", "instructordata6")
    ])
    def test_insert_instructor_from_admin(self, email, password, fn, ln, email_instructor, password_insturctor, title, postal_code, pn, address, area_code, country, state, city, gender, facebook, twitter, linkedin, pinterest, about, msg):
      waktu = 1
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      manageadmin = ManageAdminPage(self.driver)
      landingPage.doLogin(email, password)
      instructorpage = InstructorPage(self.driver)
      organizationPage = OrganizationPage(self.driver)
      time.sleep(waktu)
      instructorpage.click_button("Allow cookies")
      time.sleep(waktu)
      adminpage.click_manage_instructor()
      time.sleep(waktu)
      adminpage.click_add_instructor()
      time.sleep(waktu)
      adminpage.enter_ins_field("First Name", fn)
      time.sleep(waktu)
      adminpage.enter_ins_field("Last Name", ln)
      time.sleep(waktu)
      adminpage.enter_ins_field("Email", email_instructor)
      time.sleep(waktu)
      adminpage.enter_ins_field("Password", password_insturctor)
      time.sleep(waktu)
      adminpage.enter_ins_field("Professional Title", title)
      time.sleep(waktu)
      organizationPage.enter_ins_select_field("name", "area_code", area_code)
      time.sleep(waktu)
      adminpage.enter_ins_field("Phone Number", pn)
      time.sleep(waktu)
      adminpage.enter_ins_field("Address", address)
      time.sleep(waktu)
      organizationPage.enter_ins_field("Postal Code", postal_code)
      time.sleep(waktu)
      organizationPage.enter_ins_select_field("id", "country_id", country)
      time.sleep(waktu)
      organizationPage.enter_ins_select_field("id", "state_id", state)
      time.sleep(waktu)
      organizationPage.enter_ins_select_field("id", "city_id", city)
      time.sleep(waktu)
      organizationPage.enter_ins_select_field("id", "gender", gender)
      time.sleep(waktu)
      organizationPage.enter_ins_field("https://facebook.com", facebook)
      time.sleep(waktu)
      organizationPage.enter_ins_field("https://twitter.com", twitter)
      time.sleep(waktu)
      organizationPage.enter_ins_field("https://linkedin.com", linkedin)
      time.sleep(waktu)
      organizationPage.enter_ins_field("https://pinterest.com", pinterest)
      time.sleep(waktu)
      organizationPage.enter_ins_textarea("about_me", about, "name")
      time.sleep(waktu)
      adminpage.click_ins_button("Save")
      time.sleep(5)

      assert organizationPage.getToastMessage() == msg
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("password_instructor,msg", [
      PageData.getTestData("InstructorEditData", "editinstructor1")
    ])
    def test_edit_instructor_from_admin(self, email, password, password_instructor, msg):
      waktu = 2
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      landingPage.doLogin(email, password)
      instructorpage = InstructorPage(self.driver)
      time.sleep(waktu)
      instructorpage.click_button("Allow cookies")
      time.sleep(waktu)
      adminpage.click_manage_instructor()
      time.sleep(waktu)
      adminpage.click_all_instructors()
      time.sleep(waktu)
      adminpage.click_edit_instructor()
      
      
      time.sleep(waktu)
      adminpage.enter_ins_field("Password", str(password_instructor))
      time.sleep(waktu)
      adminpage.click_ins_button("Save")

      organizationPage = OrganizationPage(self.driver)
      assert organizationPage.getToastMessage() == msg
      time.sleep(5)
      
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    def test_delete_instructor_from_admin(self, email, password):
      waktu = 5
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      manageadmin = ManageAdminPage(self.driver)
      landingPage.doLogin(email, password)
      instructorpage = InstructorPage(self.driver)
      time.sleep(waktu)
      instructorpage.click_button("Allow cookies")
      time.sleep(waktu)
      adminpage.click_manage_instructor()
      time.sleep(waktu)
      adminpage.click_all_instructors()
      time.sleep(waktu)
      adminpage.click_delete_instructor()
      time.sleep(waktu)
      adminpage.click_confirm_delete()
      time.sleep(5)


    

