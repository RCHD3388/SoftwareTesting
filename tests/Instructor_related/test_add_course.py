
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
from pageObjects.Instructor_related.InstructorPage import InstructorPage
class TestOrganizationIns(BaseClass):
    

   

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    
   
    
    def test_instructor_from_admin(self, email, password):
      landingPage = LandingPage(self.driver)
      instructorPage = InstructorPage(self.driver)
      landingPage.doLogin(email, password)
      time.sleep(2)
      instructorPage.open_instructor_panel()
      instructorPage.open_upload_course()
      time.sleep(2)



    

