
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
    
    
    
    def test_approve_course(self, email, password):
      timer =2
      landingPage = LandingPage(self.driver)
      adminpage = AdminPage(self.driver)
      
      landingPage.doLogin(email, password)
      adminpage.click_manage_course()
      time.sleep(timer)
      adminpage.click_review_pending()
      time.sleep(timer)
      adminpage.click_approve_button()
      time.sleep(timer)
      time.sleep(2)
    




    

