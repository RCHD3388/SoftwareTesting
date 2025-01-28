from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.student_related.StudentPage import StudentPage
from utilities.BaseClass import BaseClass
import os
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.intructor_related.InstructorAddCoursePage import InstructorAddCoursePage
from pageObjects.admin_related.AdminPage import AdminPage

class TestSkenarioBecameInstructor(BaseClass):
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase4")
    ])
    @pytest.mark.parametrize("pdf, professional_title, address, bio", [
      PageData.getTestData("StudentData", "testcase1")
    ])
    def test_became_instructor(self, email, password, pdf, professional_title, address, bio):
      landingPage = LandingPage(self.driver)
      landingPage.doLogin(email, password)
      studentPage = StudentPage(self.driver)

      studentPage.click_become_instructor()
      time.sleep(0.5)

      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.become_instructor_toast_message_locator)).perform()
      time.sleep(2)
    
      studentPage.click_become_instructor_toast_message()
      time.sleep(0.5)

      studentPage.enter_insert_field("professional_title", professional_title)
      time.sleep(2)

      studentPage.enter_insert_field("address", address)
      time.sleep(2)

      file_path = os.path.abspath(pdf)
      file_path =file_path.replace("\\", "\\\\")
      time.sleep(0.5)
      studentPage.enter_insert_cv(file_path)
      time.sleep(0.5)

      # ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.input_bio)).perform()
      # time.sleep(2)

      studentPage.scrollToXY(0,30)
      time.sleep(1)

      studentPage.getInsertTextarea(bio)
      time.sleep(0.5)

      studentPage.click_insert_button("Submit")
      time.sleep(2)
