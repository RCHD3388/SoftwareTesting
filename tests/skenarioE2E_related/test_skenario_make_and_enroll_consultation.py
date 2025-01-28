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
from pageObjects.intructor_related.InstructorPage import InstructorPage
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.student_related.StudentPage import StudentPage

class TestSkenarioUploadCourse(BaseClass):
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("consultation_privacy, consultation_type, consultation_area,consultation_fee, consultation_old_fee, offline_status_message, start_time, end_time", [
      PageData.getTestData("InstructorConsultationData", "test3")
    ])
    def test_instrucutor_set_consultation(self, email, password, consultation_privacy, consultation_type, consultation_area,consultation_fee, consultation_old_fee, offline_status_message, start_time: str, end_time: str):
      landingPage = LandingPage(self.driver)
      instructorPage = InstructorPage(self.driver)

      # delay
      def delay(t=0.3):
        time.sleep(t)

      # login
      landingPage.doLogin(email, password)
      time.sleep(0.5)

      # klik instructor panel
      instructorPage.click_instruction_panel_button()
      delay()

      # tutup pop up cookie
      # instructorPage.click_button_pop_up("aria-label", "Close")
      instructorPage.click_button("Allow cookies")
      delay()

        # scroll ke bawah
      instructorPage.scrollToXY(0, 80)
      delay(3)

        # klik menu chat
      instructorPage.click_menu_consultation("Consultation")
      delay(3)

      # instructorPage.scrollToXY(0, 80)
      # delay(3)

      #  klik menu dashboard consultation
      instructorPage.click_dashboard_consultation()
      delay()

      # ======================== PAGE CONSULTATION ========================
      # scroll ke bawah
      instructorPage.scrollToXY(0, 40)
      delay(1)
    
      # radio button private consultation
      is_consultation_private = consultation_privacy

      if is_consultation_private == "Yes":
        instructorPage.click_radio_button_scroll("id", "inlineCheckbox1")
      elif is_consultation_private == "No":
        instructorPage.click_radio_button_scroll("id", "inlineCheckbox2")

      delay()

      # radio button consultation type
      # consultation_type = "Both"
      if consultation_type == "In Person":
        instructorPage.click_radio_button("id", "inlineCheckbox3")
      elif consultation_type == "Online":
        instructorPage.click_radio_button("id", "inlineCheckbox4")
      else:
        instructorPage.click_radio_button("id", "inlineCheckbox5")

       
      # radio button consultation area
      # consultation_area = "All Over The World"

      if consultation_type != "Online" and consultation_area == "All Over The World":
        instructorPage.click_radio_button("id", "consultancyArea2")
      elif consultation_type != "Online":
        instructorPage.click_radio_button("id", "consultancyArea1")

      delay()

      # isi input consultation fee
      instructorPage.enter_field("id", "hourlyRate", consultation_fee)
      delay()

      # isi input consultation old fee
      instructorPage.enter_field_scroll("id", "hourlyOldRate", consultation_old_fee)
      delay()

      # tekan button offline status
      instructorPage.click_offline_status("id", "offlineStatus")
      delay(2)
      
      # isi input offline status
      instructorPage.enter_textarea_scroll("id", "offlineMessageText", offline_status_message)
      delay()

      # tekan button save
      instructorPage.click_button_save_consultation("last()")
      delay()

      #assert message 
      actual_message = instructorPage.getToastMessage()
      delay()
      # expected_message = "Updated Successfully"
      # assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

      # =================== PAGE ADD CONSULTATION SCHEDULE ===================
      # scroll ke bawah
      instructorPage.scrollToXY(0, 130)
      delay(1)

      # tekan add slot pada hari sabtu
      instructorPage.click_button_pop_up("class","theme-btn theme-button1 default-hover-btn saturdayAddSlot")
      delay(1)

      # pastikan start time adalah string
      start_time_str = str(start_time)
      # isi start time
      instructorPage.enter_field("name", "starTimes[]", start_time_str)
      delay()

      # pastikan start time adalah string
      end_time_str = str(end_time)
      # isi end time
      instructorPage.enter_field("name", "endTimes[]", end_time_str)
      delay()

      # tekan button save slot baru
      instructorPage.click_save_slot_consultation()
      delay()

      #assert message 
      actual_message = instructorPage.getToastMessage()
      delay()
      # expected_message = "Slot Added successfully"
      # assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

      # ubah status slot menjadi available
      if instructorPage.get_button_consultation_day_status_text() == "Off day":
        # scroll ke bawah
        instructorPage.scrollToXY(0, 160)
        delay(1)

        instructorPage.click_button_consultation_day_status()
        delay()

        actual_message = instructorPage.getToastMessage()
        delay()
        # expected_message = "Status Change Successfully"
        # assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

      # scroll ke bawah
      instructorPage.scrollToXY(0, 130)
      delay(1)

      # lihat detail slot
      instructorPage.click_button_pop_up("class","theme-btn theme-button1 green-theme-btn default-hover-btn saturdayViewSlot viewSlot")
      delay(5)

      instructorPage.click_button_close_consultation_view_slot()
      delay(1)
      
      # logout
      landingPage.doLogout()
      
      time.sleep(2)

      # ===================== student buy consultation =======================
      landingPage = LandingPage(self.driver)
      email = "studenttest@gmail.com"
      landingPage.doLogin(email, password)
      studentPage = StudentPage(self.driver)

      ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.profile_img)).perform()
      time.sleep(2)

      studentPage.click_menu("My Consultation")
      delay()

      studentPage.click_menu("Browse More Consultation")
      delay()

      studentPage.scrollToXY(0, 70);
      delay()

      studentPage.click_insert_button("Book Schedule")
      delay(1)

      studentPage.enter_insert_field("datepicker","1")
      time.sleep(2)

      studentPage.click_date_picker_button()
      time.sleep(2)

      studentPage.click_menu("1")
      time.sleep(5)

      studentPage.click_label("In Person")
      delay()

      studentPage.click_label("10:08 AM - 12:08 PM")
      delay()

      studentPage.click_insert_button("Make Payment")
      delay()

      studentPage.scrollToXY(0,80)
      delay(10)

      studentPage.click_insert_field_name("proceed_to_checkout")
      delay()

      try:
        studentPage.click_arial_label("Close").click()
        time.sleep(2)
      except:
        time.sleep(2)
      time.sleep(5)
      studentPage.scrollToXY(0,50)
      time.sleep(5)
      try:
        # Cari elemen dengan name="country_id"
        hidden_element = studentPage.get_hidden_element()

        # Pastikan elemen ditemukan
        assert hidden_element is not None
        print("test")

        # Periksa apakah elemen adalah hidden
        assert hidden_element.get_attribute("type") == "hidden"
        time.sleep(2)
      except Exception as e:
        studentPage.enter_insert_field("address", "AlamatTest")
        studentPage.click_select_field("country_id")
        delay()
        studentPage.combo_box_select("country_id", "2").click()
        delay()
        studentPage.click_select_field("state_id")
        delay()
        studentPage.combo_box_select("state_id", 2).click()
        delay()
        studentPage.click_select_field("state_id")
        delay()
        studentPage.combo_box_select("state_id", 2).click()
        delay()
        studentPage.enter_insert_field("postal_code", "032949234")
        delay()
      finally:
        ActionChains(self.driver).move_to_element(self.driver.find_element(*studentPage.get_span_normalize_space("Instamojo"))).perform()
        time.sleep(2)

        studentPage.click_checkbox_field("paypalPayment")

        delay()

        studentPage.click_pay_paypal()

        time.sleep(2)

        studentPage.enter_insert_field("email", "sb-vsrrv29812931@personal.example.com")

        delay()

        studentPage.click_button_byid("btnNext")
        delay()

        studentPage.enter_insert_field("password", "*XUe5$Z1")
        delay()

        studentPage.click_button_byid("btnLogin")
        delay()

        studentPage.click_button_byid("payment-submit-btn")
        time.sleep(10)
        