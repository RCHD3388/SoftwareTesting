import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from utilities.BaseClass import BaseClass

import os

class TestInstructorSetConsultation(BaseClass):
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("consultation_privacy, consultation_type, consultation_area,consultation_fee, consultation_old_fee, offline_status_message, start_time, end_time", [
      PageData.getTestData("InstructorConsultationData", "test1")
      # PageData.getTestData("InstructorConsultationData", "test2")
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
      instructorPage.scrollToXY(0, 60)
      delay(3)

        # klik menu chat
      instructorPage.click_menu_consultation("Consultation")
      delay()

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
      expected_message = "Updated Successfully"
      assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

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
      expected_message = "Slot Added successfully"
      assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

      # ubah status slot menjadi available
      if instructorPage.get_button_consultation_day_status_text() == "Off day":
        # scroll ke bawah
        instructorPage.scrollToXY(0, 130)
        delay(1)

        instructorPage.click_button_consultation_day_status()
        delay()

        actual_message = instructorPage.getToastMessage()
        delay()
        expected_message = "Status Change Successfully"
        assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

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