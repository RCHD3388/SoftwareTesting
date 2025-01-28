
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.admin_related.AdminPage import AdminPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from pageObjects.admin_related.ManageAdminPage import ManageAdminPage
from utilities.BaseClass import BaseClass
import os
class TestAdminOrganization(BaseClass):
    

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("first, last, email_student, password_student, phone, address, postal, country, gender, state, city, area, about", [
      PageData.getTestData("AdminStudentData", "studentcase4")
    ])

    def test_student_from_admin(self, email, password, first, last, email_student, password_student, phone, address, postal, country, gender, state, city, area, about):
    
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      instructorpage = InstructorPage(self.driver)
      landingPage.doLogin(email, password)
      
      instructorpage.click_button("Allow cookies")

      adminpage.click_manage_student()
      adminpage.click_add_student()
      time.sleep(4)
      
      adminpage.enter_ins_field("First Name", first)
      adminpage.enter_ins_field("Last Name", last)
      adminpage.enter_ins_field("Email", email_student)
      adminpage.enter_ins_field("Password", str(password_student))
      adminpage.enter_ins_field("Phone number", phone)
      adminpage.enter_ins_field("Address", address)
      
      adminpage.enter_ins_field("Postal Code", postal)
      
      time.sleep(0.5)
      adminpage.enter_ins_select_field("id", "country_id", country)
      time.sleep(0.5)
      adminpage.enter_ins_select_field("id", "gender", gender)
      adminpage.enter_ins_select_field("id", "state_id", state)
      adminpage.enter_ins_select_field("id", "city_id", city)
      adminpage.enter_ins_select_field("name", "area_code", area)
      adminpage.enter_ins_textarea("about_me", about)
     
      adminpage.click_ins_button("Save")
      
      time.sleep(10)

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("student_password", [
      PageData.getTestData("EditStudentData", "studenteditdata1")
    ])
    
    def test_edit_student(self, email, password, student_password):
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
      adminpage.click_edit_instructor()
      
      
      time.sleep(waktu)
      adminpage.enter_ins_field("Password",str(student_password))
   
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


    

