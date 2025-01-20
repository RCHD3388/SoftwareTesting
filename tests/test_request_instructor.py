
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.AdminPage import AdminPage
from pageObjects.StudentPage import StudentPage
from utilities.BaseClass import BaseClass
from tests.test_login import TestLogin

class TestRequestInstructor(BaseClass):

    def test_request_instructor(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        studentPage = StudentPage(self.driver)
        adminPage = AdminPage(self.driver)
        TestLogin(self.driver).test_login(
            self.email, self.password
        )
        studentPage.doRequestInstructor(
            PageData.firstName, PageData.lastName, PageData.phoneNumber,
            PageData.address, PageData.cv, PageData.bio
        )
        adminPage.getPendingInstructor().click()
        adminPage.getInstructorComboBox().click()
        select = Select(adminPage.getInstructorComboBox())
        select.select_by_visible_text(PageData.firstName + " " + PageData.lastName)
        adminPage.getPendingInstructorApproveButton().click()
        
        
        