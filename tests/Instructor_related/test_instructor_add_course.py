import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from utilities.BaseClass import BaseClass

import os

class TestInstructorAddCourse(BaseClass):
    
    def createInstructor(self, instructorPage: InstructorPage,
    #  image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output
    ):
      image_path = os.path.abspath("TestData\\assets\\images\\avocatto.jpg")
      image_path = image_path.replace("\\", "\\\\")
      
      def delay(t=0.3):
        time.sleep(t)

      # isi input course type
      instructorPage.enter_select_field_scroll("id", "course_type","General")
      delay()

      # isi input course title
      instructorPage.enter_field("placeholder","Type your course title", "Course1")
      delay()

      # isi input course subtitle
      instructorPage.enter_textarea("placeholder", "Course subtitle in 1000 characters", "hehehe")
      delay()

      # isi input course key points
      instructorPage.enter_field_scroll("id","name", "Machine Learning")
      delay()

      # isi input course description
      instructorPage.enter_textarea("placeholder", "Course description", "bisa ini mudah kok")
      delay()

      # isi input meta title
      instructorPage.enter_field_scroll("placeholder","Meta Title", "Trending")
      delay()

      # isi input meta description
      instructorPage.enter_textarea("id", "exampleFormControlTextarea1", "Ini Lagi Trend")
      delay()

      # isi input meta keywords
      instructorPage.enter_field_scroll("placeholder","Type meta keywords (comma separated)", "Machine Learning")
      delay()

      # isi input course image
      instructorPage.enter_field_scroll("id", "og_image", image_path)
      delay()

      # tekan buttton continue
      instructorPage.click_button_scroll("Save and continue")
      delay()

      # ======================== PAGE 2 ========================
      # CATEGORY & TAGS

      # isi select category
      instructorPage.enter_select_field_scroll("id", "category_id", "IT & Software")
      delay()

      # isi select sub category
      instructorPage.enter_select_field("id", "subcategory_id", "IT Certifications")
      delay()

      # isi tags
      instructorPage.enter_select_field_scroll("name", "tag[]", "IT")
      delay()

      # Learners Accesibility And Others

      # isi select request course
      instructorPage.enter_select_field_scroll("name", "status", "Publish")
      delay()

      # isi select drip content
      instructorPage.enter_select_field("name", "drip_content", "Available sequentially")
      delay()

      # isi input course access duration (in days)
      instructorPage.enter_field("name", "access_period", "30")
      delay()

      # isi select learner accessibility
      learner_accessibility = "Paid"
      instructorPage.enter_select_field_scroll("name", "learner_accessibility", learner_accessibility)
      delay()

      # if choose paid
      if learner_accessibility == "Paid" or learner_accessibility == "paid":
        # isi input course price
        instructorPage.enter_field("placeholder", "price", "50")
        delay()

        # isi input old course price
        instructorPage.enter_field("placeholder", "Old Price", "25")
        delay()

      # isi select language
      instructorPage.enter_select_field_scroll("id", "course_language_id", "English")
      delay()

      # isi select difficulty level
      instructorPage.enter_select_field_scroll("id", "difficulty_level_id", "Medium")
      delay()

      # isi select course thumbnail
      instructorPage.enter_field_scroll("id", "image", image_path)
      delay()

      # pilih upload video introduction
      instructorPage.click_radio_button_scroll("id", "youtube_check") 
      delay()

      # isi input video introduction
      instructorPage.enter_field_scroll("id", "youtube_video_id", "IpFX2vq8HKw")
      delay()

      # tekan buttton continue
      instructorPage.click_button("Save and continue")
      delay()

      # ======================== PAGE 3 ========================
      # isi section title
      instructorPage.enter_field_scroll("placeholder", "Introduction", "Introduction")
      delay()

      # find button
      
      btn_continue = instructorPage.find_button("Save and continue")
      delay()
      instructorPage.scrollTo(btn_continue)

      # tekan buttton continue
      instructorPage.click_button_scroll("Save and continue")
      delay()

      # ======================== PAGE 4 ========================

      #assert message 
      actual_message = instructorPage.getToastMessage()
      expected_message = "Created successful."
      assert actual_message == "Created successful.", f"Expected: {expected_message}, but got: {actual_message}"
      #SCROLL MENU
      instructorPage.scroll_to_menu("Live Class")

      # find button
      btn_upload = instructorPage.click_element("a","class","common-upload-lesson-btn font-13 font-medium")
   
      delay()

      #assert message


      # pilih youtube link
      instructorPage.click_radio_button_scroll("id", "lectureTypeYoutube")
      delay()

      # isi input youtube link
      instructorPage.enter_field("id", "youtube_url_path", "IpFX2vq8HKw")
      delay()

      # isi input lesson title
      instructorPage.enter_field("placeholder", "First steps", "Introduction aaa")
      delay()

      # isi select learning visibility
      instructorPage.enter_select_field("name", "lecture_type", "Show")
      delay()

      # isi input lesson duration
      instructorPage.enter_field_scroll("name", "youtube_file_duration", "03:41")
      delay() 

      # tekan button save
      instructorPage.click_button("Save")
      delay()

      # tekan button save and continue
      instructorPage.scroll_to_menu("Chat")
      delay()
      instructorPage.click_save_final()
      

      # ======================== PAGE terakhir ========================

      # isi input other instructor
      # instructorPage.enter_select_field_scroll("id", "instructor-id", "Ade")

      # # tekan button save and continue
      # instructorPage.click_button_scroll("Save and continue")
      delay()
      btn_save_terakhir = instructorPage.click_element("button","type","submit")
      delay()
      instructorPage.scroll_to_menu("Chat")
      delay()
      btn_submit_review = instructorPage.click_element("a","type","button")
      delay()
      
      delay()
      instructorPage.verify_waiting_toreview()
      delay()

      time.sleep(10)
      # assert organizationPage.getToastMessage() == output

    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    # @pytest.mark.parametrize("image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output", [
    #   PageData.getTestData("OrganizationInstructorData", "testcase6"),
    #   # PageData.getTestData("OrganizationInstructorData", "testcase2"),
    #   # PageData.getTestData("OrganizationInstructorData", "testcase3"),
    #   # PageData.getTestData("OrganizationInstructorData", "testcase4"),
    #   # PageData.getTestData("OrganizationInstructorData", "testcase5"),
    # ])
    def test_instrucutor_add_course(self, email, password
      # , image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output
      ):
      landingPage = LandingPage(self.driver)
      instructorPage = InstructorPage(self.driver)
      # login
      landingPage.doLogin(email, password)
      time.sleep(0.5)

      # klik instructor panel
      instructorPage.click_instruction_panel_button()
      time.sleep(0.5)

      # tutup pop up cookie
      # instructorPage.click_button_pop_up("aria-label", "Close")
      instructorPage.click_button("Allow cookies")
      time.sleep(0.5)

      # klik menu upload course
      instructorPage.click_menu_side_bar("Upload Course")
      time.sleep(0.5)

      # instructorPage.enter_select_field("course_type", "Course Type","General")

      # FIELD
      self.createInstructor(
        instructorPage,
          # image, first_name, last_name, ins_email, ins_password, prof_title, area, mobile, country, state, city, address, postal, gender, facebook, twitter, linkedin, pinterest, about, output
         )
      
      time.sleep(2)