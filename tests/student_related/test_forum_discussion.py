from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TestData.PageData import PageData
from pageObjects.student_related.StudentPageOther import StudentPage
from utilities.BaseClass import BaseClass
from pageObjects.LandingPage import LandingPage

class TestForumDiscussion:
    @pytest.mark.parametrize("student_email, student_password", [
        PageData.getTestData("LoginData", "testcase4")
    ])
    @pytest.mark.parametrize("title, subtitle, content", [
        PageData.getTestData("ForumDiscussion", "testcase1"),
        PageData.getTestData("ForumDiscussion", "testcase2")
    ])
    def test_forum_discussion(self, setup, student_email, student_password, title, subtitle, content):
        # Set up wait
        wait = WebDriverWait(self.driver, 10)
        landingPage = LandingPage(self.driver)
        # Login as student
        studentPage = StudentPage(self.driver)
        landingPage.doLogin(student_email, student_password)
        
        studentPage.doCreateForumQuestion(title, subtitle, content)
        time.sleep(2)
        
        assert studentPage.getForumToastMessage() == "Question created successfully."