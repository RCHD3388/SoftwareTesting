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


class TestSkenarioStudentEnrollPaidCourse(BaseClass):
    @pytest.mark.parametrize("email, password, email1, password1, email2, password2", [
      PageData.getTestData("SkenarioInstructorStudentData", "testcase1")
    ])
    @pytest.mark.parametrize("course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration", [
    #   PageData.getTestData("AddCourseData", "test1"),
      PageData.getTestData("AddCourseData", "test2"),
    #   PageData.getTestData("AddCourseData", "test3"),
    ])
    def test_enroll_paid_course(self, email, password, email1, password1, email2, password2, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration):
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
      time.sleep(0.5)
      studentPage.click_menu("All Courses")
      time.sleep(0.5)
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
      studentPage.click_checkbox_field("exampleRadiosAccessibility33")
      # studentPage.click_checkbox_field("exampleRadiosAccessibility33")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Business"))).perform()
      time.sleep(2)
      studentPage.click_menu("Python Intermediate")
      time.sleep(2)
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getMenuh6("This Course Includes"))).perform()
      # studentPage.click_menu("Go to Course")
      studentPage.click_button_enroll()
      time.sleep(2)

      studentPage.click_shopping_cart_button()
      time.sleep(2)

      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertFieldName("cancel_order"))).perform()
      time.sleep(2)

      studentPage.click_insert_field_name("proceed_to_checkout")
      time.sleep(2)

      try:
        studentPage.click_arial_label("Close")
        time.sleep(2)
      except:
        time.sleep(2)
      
      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertField("phone_number"))).perform()
      try:
        # Cari elemen dengan name="country_id"
        hidden_element = self.driver.find_element(*studentPage.get_hidden_element())

        # Pastikan elemen ditemukan
        assert hidden_element is not None
        print("test")

        # Periksa apakah elemen adalah hidden
        assert hidden_element.get_attribute("type") == "hidden"
        time.sleep(2)
      except Exception as e:
        studentPage.enter_insert_field("address", "AlamatTest")
        studentPage.click_select_field("country_id")
        time.sleep(2)
        studentPage.click_combo_box_select("country_id", 2)
        time.sleep(2)
        studentPage.click_select_field("state_id")
        time.sleep(2)
        studentPage.click_combo_box_select("state_id", 2)
        time.sleep(2)
        studentPage.click_select_field("state_id")
        time.sleep(2)
        studentPage.click_combo_box_select("state_id", 2)
        time.sleep(2)
        studentPage.enter_insert_field("postal_code", "032949234")
        time.sleep(2)
      finally:
        ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.get_span_normalize_space("Instamojo"))).perform()
        time.sleep(2)

        studentPage.click_checkbox_field("paypalPayment")

        time.sleep(2)

        studentPage.click_pay_paypal()

        time.sleep(2)

        studentPage.enter_insert_field("email", "sb-vsrrv29812931@personal.example.com")

        time.sleep(2)

        studentPage.click_button_byid("btnNext")
        time.sleep(2)

        studentPage.enter_insert_field("password", "*XUe5$Z1")
        time.sleep(2)

        studentPage.click_button_byid("btnLogin")
        time.sleep(5)

        studentPage.click_button_byid("payment-submit-btn")
        time.sleep(5)