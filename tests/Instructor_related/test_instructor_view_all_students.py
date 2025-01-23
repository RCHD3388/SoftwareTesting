import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from utilities.BaseClass import BaseClass

import os

class TestInstructorViewStudents(BaseClass):
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("student_name, course_name", [
      PageData.getTestData("InstructorStudentData", "test1"),
      PageData.getTestData("InstructorStudentData", "test2")
    ])
    def test_instrucutor_view_students(self, email, password, student_name, course_name):
      landingPage = LandingPage(self.driver)
      instructorPage = InstructorPage(self.driver)
      log = self.getLogger()
      log.info(student_name)

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
      delay(1)

      # klik menu all students
      instructorPage.click_menu_side_bar("All Students")
      delay()

      # ======================== PAGE ALL STUDENTS ========================
      # scroll ke bawah
      instructorPage.scrollToXY(0, 50)
      delay(1)

      # tekan button "View" yang nama studentnya sesuai dengan yang diinginkan
      instructorPage.click_button_view_student(student_name,course_name)
      delay(1)

      # assert nama student
      expected_name = student_name
      assert instructorPage.get_student_info("span","class","user_name") == expected_name
      delay(1)

      # assert course name
      expected_course = course_name
      assert instructorPage.get_student_info("div","class","all-student-info-value col-sm-6 col-md-6 col-lg-8 course_name") == expected_course
      delay(3)

      # close modal
      instructorPage.click_button_pop_up("class",'btn-close')
      delay(1)

      # logout
      landingPage.doLogout()
      delay(1)

      
