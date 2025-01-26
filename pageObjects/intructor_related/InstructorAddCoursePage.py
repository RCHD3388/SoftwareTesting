from re import S
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
from pageObjects.intructor_related.InstructorPage import InstructorPage

class InstructorAddCoursePage():
    def __init__(self, driver):
        self.driver = driver

    def createInstructor(self, instructorPage: InstructorPage, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration: str
    ):
      image_path = os.path.abspath(course_image)
      image_path = image_path.replace("\\", "\\\\")

      thumbnail_path = os.path.abspath(course_thumbnail)
      thumbnail_path = thumbnail_path.replace("\\", "\\\\")
      
      def delay(t=0.3):
        time.sleep(t)

      # isi input course type
      instructorPage.enter_select_field_scroll("id", "course_type",course_type)
      delay()

      # isi input course title
      instructorPage.enter_field("placeholder","Type your course title", course_title)
      delay()

      # isi input course subtitle
      instructorPage.enter_textarea("placeholder", "Course subtitle in 1000 characters", course_subtitle)
      delay()

      # isi input course key points
      instructorPage.enter_field_scroll("id","name", key_point)
      delay()

      # isi input course description
      instructorPage.enter_textarea("placeholder", "Course description", course_desc)
      delay()

      # isi input meta title
      instructorPage.enter_field_scroll("placeholder","Meta Title", meta_title)
      delay()

      # isi input meta description
      instructorPage.enter_textarea("id", "exampleFormControlTextarea1", meta_desc)
      delay()

      # isi input meta keywords
      instructorPage.enter_field_scroll("placeholder","Type meta keywords (comma separated)", meta_key)
      delay()

      # isi input course image
      instructorPage.enter_field_scroll("id", "og_image", image_path)
      delay(0.5)

      # tekan buttton continue
      instructorPage.click_button_scroll("Save and continue")
      delay()

      # ======================== PAGE 2 ========================
      # CATEGORY & TAGS

      # isi select category
      instructorPage.enter_select_field_scroll("id", "category_id", category)
      delay()

      # isi select sub category
      instructorPage.enter_select_field("id", "subcategory_id", subcategory)
      delay()

      # isi tags
      instructorPage.enter_select_field_scroll("name", "tag[]", tags)
      delay()

      # Learners Accesibility And Others

      # isi select request course
      instructorPage.enter_select_field_scroll("name", "status", request_course_status)
      delay()

      # isi select drip content
      instructorPage.enter_select_field("name", "drip_content", drip_content)
      delay()

      # isi input course access duration (in days)
      instructorPage.enter_field("name", "access_period", access_duration)
      delay()

      # isi select learner accessibility
    #   learner_accessibility = "Paid"
      instructorPage.enter_select_field_scroll("name", "learner_accessibility", learner_accessibility)
      delay()

      # if choose paid
      if learner_accessibility == "Paid" or learner_accessibility == "paid":
        # isi input course price
        instructorPage.enter_field("placeholder", "price", course_price)
        delay()

        # isi input old course price
        instructorPage.enter_field("placeholder", "Old Price", old_course_price)
        delay()

      # isi select language
      instructorPage.enter_select_field_scroll("id", "course_language_id", language)
      delay()

      # isi select difficulty level
      instructorPage.enter_select_field_scroll("id", "difficulty_level_id", difficulty_level)
      delay()

      # isi select course thumbnail
      instructorPage.enter_field_scroll("id", "image", thumbnail_path)
      delay(0.5)

      # pilih upload video introduction
      instructorPage.click_radio_button_scroll("id", "youtube_check") 
      delay()

      # isi input video introduction
      instructorPage.enter_field_scroll("id", "youtube_video_id", intro_youtube_id)
      delay()

      # tekan buttton continue
      instructorPage.click_button_scroll("Save and continue")
      delay()

      # ======================== PAGE 3 ========================
      # isi section title
      instructorPage.enter_field_scroll("placeholder", "Introduction", section_title)
      delay()

      # find button
      instructorPage.scroll_to_menu("Live Class")
      delay()

      # tekan buttton continue
      instructorPage.click_button_scroll("Save and continue")
      delay()

      # ======================== PAGE 4 ========================

      #assert message 
      actual_message = instructorPage.getToastMessage()
      delay()
      expected_message = "Created successful."
      assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"
      #SCROLL MENU

      instructorPage.scrollToXY(0, 50)
      delay(1)

      # click btn upload lesson
      instructorPage.click_menu_side_bar("Upload lesson")
      delay(1)

      #assert message

      #  =================== PAGE BARU LANJUTAN ===================
      # scroll ke bawah
      instructorPage.scrollToXY(0, 50)
      delay(1)

      # pilih youtube link
      instructorPage.click_radio_button_scroll("id", "lectureTypeYoutube")
      delay()

      # isi input youtube link
      instructorPage.enter_field("id", "youtube_url_path", lesson_youtube_id)
      delay()

      # isi input lesson title
      instructorPage.enter_field("placeholder", "First steps", section_title)
      delay()

      # isi select learning visibility
      instructorPage.enter_select_field("name", "lecture_type", learning_visibility)
      delay()

      # pastikan lesson duration adalah string
      hasil = str(lesson_duration)

      # isi input lesson duration
      instructorPage.enter_field_scroll("name", "youtube_file_duration", hasil)
      delay() 

      # tekan button save
      instructorPage.click_button("Save")
      delay()

      # tekan button save and continue
      instructorPage.scrollToXY(0, 70)
      delay()

      # scroll ke upload lesson btn
      instructorPage.scroll_to_menu("Upload lesson")
      delay()

      instructorPage.click_save_final()
      delay()
      

      # ======================== PAGE terakhir ========================

      # scroll ke bawah
      instructorPage.scrollToXY(0, 50)
      delay(1)

      # tekan button save and continue
      instructorPage.click_button_scroll("Save and continue")
      delay()

      # ========================= SAVE AND FINISH =========================
      # scroll ke bawah
      instructorPage.scrollToXY(0, 50)
      delay(1)

      instructorPage.click_menu_side_bar("Submit for review")
      delay()
      
      # assert message
      instructorPage.verify_waiting_toreview()
      delay()
      # assert organizationPage.getToastMessage() == output


    def add_course(self, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration):
      instructorPage = InstructorPage(self.driver)
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

      # FIELD
      self.createInstructor(
        instructorPage, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration
        )
      
      time.sleep(2)