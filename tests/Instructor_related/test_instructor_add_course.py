import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from pageObjects.intructor_related.InstructorAddCoursePage import InstructorAddCoursePage
from utilities.BaseClass import BaseClass

import os

class TestInstructorAddCourse(BaseClass):
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration", [
      PageData.getTestData("AddCourseData", "test1"),
      PageData.getTestData("AddCourseData", "test2"),
    ])
    def test_instrucutor_add_course(self, email, password, course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration):
      landingPage = LandingPage(self.driver)
      # instructorPage = InstructorPage(self.driver)
      instructorAddCoursePage = InstructorAddCoursePage(self.driver)
      # login
      landingPage.doLogin(email, password)
      time.sleep(0.5)

      # add course
      instructorAddCoursePage.add_course(course_type, course_title, course_subtitle, key_point, course_desc, meta_title, meta_desc, meta_key, course_image, category, subcategory, tags, request_course_status, drip_content, access_duration, learner_accessibility, course_price, old_course_price, language, difficulty_level, course_thumbnail, intro_youtube_id, section_title, lesson_youtube_id, learning_visibility, lesson_duration)
      
      time.sleep(2)