from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.student_related import StudentPageOther
from pageObjects.student_related.StudentPage import StudentPage
from utilities.BaseClass import BaseClass
import os
from selenium.webdriver.common.action_chains import ActionChains


class TestStudent(BaseClass):
    
    # @pytest.mark.parametrize("email, password", [
    #   PageData.getTestData("LoginData", "testcase4")
    # ])

    # @pytest.mark.parametrize("pdf, professional_title, address, bio", [
    #   PageData.getTestData("StudentData", "testcase1")
    # ])
    # def test_become_an_instructor(self, email, password, pdf, professional_title, address, bio):
    #   landingPage = LandingPage(self.driver)
    #   landingPage.doLogin(email, password)
    #   studentPage = StudentPage(self.driver)

    #   studentPage.click_become_instructor()
    #   time.sleep(0.5)

    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.become_instructor_toast_message_locator)).perform()
    #   time.sleep(2)
    
    #   studentPage.click_become_instructor_toast_message()
    #   time.sleep(0.5)

    #   studentPage.enter_insert_field("professional_title", professional_title)
    #   time.sleep(2)

    #   studentPage.enter_insert_field("address", address)
    #   time.sleep(2)

    #   file_path = os.path.abspath(pdf)
    #   file_path =file_path.replace("\\", "\\\\")
    #   time.sleep(0.5)
    #   studentPage.enter_insert_cv(file_path)
    #   time.sleep(0.5)

    #   # ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.input_bio)).perform()
    #   # time.sleep(2)

    #   studentPage.scrollToXY(0,30)
    #   time.sleep(1)

    #   studentPage.getInsertTextarea(bio)
    #   time.sleep(0.5)

    #   studentPage.click_insert_button("Submit")
    #   time.sleep(2)

    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase4")
    ])
    def test_enroll_free_course(self, email, password):
      landingPage = LandingPage(self.driver)
      landingPage.doLogin(email, password)
      studentPage = StudentPage(self.driver)
      ActionChains(self.driver).move_to_element(studentPage.move_to_course_dropdown()).perform()
      time.sleep(0.5)
      studentPage.click_menu("All Courses")
      time.sleep(0.5)
      studentPage.click_close_cookies_permission()
      time.sleep(0.5)
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
      actual_message = studentPage.getMenuElement("SDP").text
      assert "SDP" == actual_message




    # @pytest.mark.parametrize("email, password", [
    #   PageData.getTestData("LoginData", "testcase4")
    # ])
    # def test_enroll_paid_course(self, email, password):
    #   landingPage = LandingPage(self.driver)
    #   landingPage.doLogin(email, password)
    #   studentPage = StudentPage(self.driver)
    #   ActionChains(self.driver).move_to_element(studentPage.move_to_course_dropdown()).perform()
    #   time.sleep(0.5)
    #   studentPage.click_menu("All Courses")
    #   time.sleep(0.5)
    #   studentPage.click_close_cookies_permission()
    #   time.sleep(0.5)
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Personal Development"))).perform()
    #   studentPage.click_insert_button("IT & Software")
    #   time.sleep(0.5)
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Business"))).perform()
    #   studentPage.click_checkbox_field("exampleRadiosSubCategory20")
    #   time.sleep(2)
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Rating"))).perform()
    #   studentPage.click_checkbox_field("exampleRadiosDifficulty1")
    #   time.sleep(2)
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Duration"))).perform()
    #   studentPage.click_checkbox_field("exampleRadiosAccessibility33")
    #   # studentPage.click_checkbox_field("exampleRadiosAccessibility33")
    #   time.sleep(2)
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertButton("Business"))).perform()
    #   time.sleep(2)
    #   studentPage.click_menu("Python Intermediate")
    #   time.sleep(2)
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getMenuh6("This Course Includes"))).perform()
    #   # studentPage.click_menu("Go to Course")
    #   studentPage.click_button_enroll()
    #   time.sleep(2)

    #   studentPage.click_shopping_cart_button()
    #   time.sleep(2)

    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertFieldName("cancel_order"))).perform()
    #   time.sleep(2)

    #   studentPage.click_insert_field_name("proceed_to_checkout")
    #   time.sleep(2)

    #   try:
    #     studentPage.click_arial_label("Close")
    #     time.sleep(2)
    #   except:
    #     time.sleep(2)
      
    #   ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.getInsertField("phone_number"))).perform()
    #   try:
    #     # Cari elemen dengan name="country_id"
    #     hidden_element = self.driver.find_element(*studentPage.get_hidden_element())

    #     # Pastikan elemen ditemukan
    #     assert hidden_element is not None
    #     print("test")

    #     # Periksa apakah elemen adalah hidden
    #     assert hidden_element.get_attribute("type") == "hidden"
    #     time.sleep(2)
    #   except Exception as e:
    #     studentPage.enter_insert_field("address", "AlamatTest")
    #     studentPage.click_select_field("country_id")
    #     time.sleep(2)
    #     studentPage.combo_box_select("country_id", 2).click()
    #     time.sleep(2)
    #     studentPage.click_select_field("state_id")
    #     time.sleep(2)
    #     studentPage.combo_box_select("state_id", 2).click()
    #     time.sleep(2)
    #     studentPage.click_select_field("state_id")
    #     time.sleep(2)
    #     studentPage.combo_box_select("state_id", 2).click()
    #     time.sleep(2)
    #     studentPage.enter_insert_field("postal_code", "032949234")
    #     time.sleep(2)
    #   finally:
    #     ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.get_span_normalize_space("Instamojo"))).perform()
    #     time.sleep(2)

    #     studentPage.click_checkbox_field("paypalPayment")

    #     time.sleep(2)

    #     studentPage.click_pay_paypal()

    #     time.sleep(2)

    #     studentPage.enter_insert_field("email", "sb-vsrrv29812931@personal.example.com")

    #     time.sleep(2)

    #     studentPage.click_button_byid("btnNext")
    #     time.sleep(2)

    #     studentPage.enter_insert_field("password", "*XUe5$Z1")
    #     time.sleep(2)

    #     studentPage.click_button_byid("btnLogin")
    #     time.sleep(2)

    #     studentPage.click_button_byid("payment-submit-btn")
    #     time.sleep(10)

    # @pytest.mark.parametrize("email, password", [
    # PageData.getTestData("LoginData", "testcase4")
    # ])
    # def test_buy_consultation(self, email, password):
    #     landingPage = LandingPage(self.driver)
    #     landingPage.doLogin(email, password)
    #     studentPage = StudentPage(self.driver)

    #     ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.profile_img)).perform()
    #     time.sleep(2)

    #     studentPage.click_menu("My Consultation")
    #     time.sleep(2)

    #     studentPage.click_menu("Browse More Consultation")
    #     time.sleep(2)

    #     studentPage.scrollToXY(0, 70);
    #     time.sleep(2)

    #     studentPage.click_insert_button("Book Schedule")
    #     time.sleep(2)

    #     studentPage.enter_insert_field("datepicker","25")
    #     time.sleep(2)

    #     studentPage.click_menu("25")
    #     time.sleep(5)

    #     studentPage.click_label("In Person")
    #     time.sleep(2)

    #     studentPage.click_label("10:08 AM - 12:08 AM")
    #     time.sleep(2)

    #     studentPage.click_insert_button("Make Payment")
    #     time.sleep(2)

    #     studentPage.scrollToXY(0,50)
    #     time.sleep(2)

    #     studentPage.click_insert_field_name("proceed_to_checkout")
    #     time.sleep(2)

    #     try:
    #       studentPage.click_arial_label("Close").click()
    #       time.sleep(2)
    #     except:
    #       time.sleep(2)
    #     time.sleep(5)
    #     studentPage.scrollToXY(0,50)
    #     time.sleep(5)
    #     try:
    #       # Cari elemen dengan name="country_id"
    #       hidden_element = studentPage.get_hidden_element()

    #       # Pastikan elemen ditemukan
    #       assert hidden_element is not None
    #       print("test")

    #       # Periksa apakah elemen adalah hidden
    #       assert hidden_element.get_attribute("type") == "hidden"
    #       time.sleep(2)
    #     except Exception as e:
    #       studentPage.enter_insert_field("address", "AlamatTest")
    #       studentPage.click_select_field("country_id")
    #       time.sleep(2)
    #       studentPage.combo_box_select("country_id", "2").click()
    #       time.sleep(2)
    #       studentPage.click_select_field("state_id")
    #       time.sleep(2)
    #       studentPage.combo_box_select("state_id", 2).click()
    #       time.sleep(2)
    #       studentPage.click_select_field("state_id")
    #       time.sleep(2)
    #       studentPage.combo_box_select("state_id", 2).click()
    #       time.sleep(2)
    #       studentPage.enter_insert_field("postal_code", "032949234")
    #       time.sleep(2)
    #     finally:
    #       ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.get_span_normalize_space("Instamojo"))).perform()
    #       time.sleep(2)

    #       studentPage.click_checkbox_field("paypalPayment")

    #       time.sleep(2)

    #       studentPage.click_pay_paypal()

    #       time.sleep(2)

    #       studentPage.enter_insert_field("email", "sb-vsrrv29812931@personal.example.com")

    #       time.sleep(2)

    #       studentPage.click_button_byid("btnNext")
    #       time.sleep(2)

    #       studentPage.enter_insert_field("password", "*XUe5$Z1")
    #       time.sleep(2)

    #       studentPage.click_button_byid("btnLogin")
    #       time.sleep(2)

    #       studentPage.click_button_byid("payment-submit-btn")
    #       time.sleep(10)







