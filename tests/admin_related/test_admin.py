
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
    
   
    
    @pytest.mark.parametrize("password_instructor", [
      PageData.getTestData("InstructorEditData", "editinstructor1")
    ])
    def test_edit_instructor_from_admin(self, email, password, password_instructor):
      waktu = 1
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
      adminpage.click_edit_instructor()
      
      time.sleep(waktu)
      
      time.sleep(waktu)
      adminpage.enter_ins_field("Password", password_instructor)
      time.sleep(waktu)
      adminpage.click_ins_button("Save")
      time.sleep(5)
      
    def test_delete_instructor_from_admin(self, email, password):
      waktu = 1
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


    

