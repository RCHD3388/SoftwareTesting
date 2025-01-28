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


class TestSkenarioStudentEnrollFreeCourse(BaseClass):
    @pytest.mark.parametrize("email, password, email1, password1, email2, password2", [
      PageData.getTestData("SkenarioInstructorStudentData", "testcase1")
    ])
    @pytest.mark.parametrize("course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration", [
      PageData.getTestData("AddCourseData", "test1"),
    #   PageData.getTestData("AddCourseData", "test2"),
    #   PageData.getTestData("AddCourseData", "test3"),
    ])
    def test_enroll_free_course(self, email, password, email1, password1, email2, password2, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration):
      landingPage = LandingPage(self.driver)
      instructorAddCoursePage = InstructorAddCoursePage(self.driver)
      # login
      landingPage.doLogin(email1, password1)
      time.sleep(0.5)

      # add course
      instructorAddCoursePage.add_course(course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration)
      
      time.sleep(2)
      landingPage.doLogout()

      adminpage = AdminPage(self.driver)

      #login as admin
      landingPage.doLogin(email2, password2)
      adminpage.click_manage_course()
      time.sleep(2)
      adminpage.click_review_pending()
      time.sleep(2)
      adminpage.click_approve_button()
      time.sleep(2)
      studentPage = StudentPage(self.driver)
      studentPage.click_profile_dropdown()
      landingPage.click_button_logout()

      #login as student
      landingPage.doLogin(email, password)
      time.sleep(2)
      ActionChains(self.driver).move_to_element(studentPage.move_to_course_dropdown()).perform()
      time.sleep(2)
      studentPage.click_menu("All Courses")
      time.sleep(2)
    #   studentPage.click_close_cookies_permission()
    #   time.sleep(0.5)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Personal Development"))).perform()
      studentPage.click_insert_button("IT & Software")
      time.sleep(0.5)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Business"))).perform()
      studentPage.click_checkbox_field("exampleRadiosSubCategory20")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Rating"))).perform()
      studentPage.click_checkbox_field("exampleRadiosDifficulty1")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Duration"))).perform()
      studentPage.click_checkbox_field("exampleRadiosAccessibility32")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.Duration_filter)).perform()
      # studentPage.click_checkbox_field("exampleRadiosDuration37")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Business"))).perform()
      studentPage.click_menu("Python Intro")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getMenuh6("This Course Includes"))).perform()
      # studentPage.click_menu("Go to Course")
      studentPage.click_button_enroll()
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.profile_img)).perform()
      time.sleep(2)
      studentPage.click_menu("My Learning")
      time.sleep(2)
      actual_message = studentPage.getMenuElement("Python Intro").text
      assert "Python Intro" == actual_message