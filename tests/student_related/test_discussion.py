from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.student_related.StudentPageOther import StudentPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait


class TestDiscussion(BaseClass):
    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase4")
    ])
    @pytest.mark.parametrize("content, row, index", [
        PageData.getTestData("Discussion", "testcase1")
    ])
    
    def test_discussion(self, setup, email, password, content,row,index):
        landingPage = LandingPage(self.driver)
        landingPage.doLogin(email, password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        studentPage.goToDiscussions(content, row)
        time.sleep(3)
        studentPage.getDiscussionsFinalContent(index)
        
        assert studentPage.getDiscussionsFinalContent(index) == content