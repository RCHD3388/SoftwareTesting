from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.SkenarioPasswordPage import SkenarioPasswordPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pageObjects.intructor_related.InstructorAddCoursePage import InstructorAddCoursePage
from pageObjects.admin_related.AdminPage import AdminPage

class TestSkenarioUploadCourse(BaseClass):

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration", [
      # PageData.getTestData("AddCourseData", "test1"),
      PageData.getTestData("AddCourseData", "test2"),
      # PageData.getTestData("AddCourseData", "test3"),
    ])
    def test_skenario1(self, email, password, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration):
      landingPage = LandingPage(self.driver)
      # instructorPage = InstructorPage(self.driver)
      instructorAddCoursePage = InstructorAddCoursePage(self.driver)
      # login
      landingPage.doLogin(email, password)
      time.sleep(0.5)

      # add course
      instructorAddCoursePage.add_course(course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration)
      
      time.sleep(2)

      # logout
      landingPage.doLogout()
      time.sleep(2)

      # ============= approve course =============

      # login as admin
      adminpage = AdminPage(self.driver)
      
      timer =0.5
      email = "admin@gmail.com"
      landingPage.doLogin(email, password)
      
      # go to manage course
      adminpage.click_manage_course()
      time.sleep(timer)

      # go to menu review pending
      adminpage.click_review_pending()
      time.sleep(timer)

      # approve course
      adminpage.click_approve_button()
      time.sleep(2)

      # logout
      landingPage.doLogoutAdmin()
      time.sleep(2)

    
      