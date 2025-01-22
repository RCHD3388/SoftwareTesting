
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.StudentPage import StudentPage
from utilities.BaseClass import BaseClass


class TestDiscussion(BaseClass):
    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase3")
    ])
    
    def test_discussion(self, setup, email, password):
        landingPage = LandingPage(self.driver)
        landingPage.doLogin(email, password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        studentPage.goToDiscussions("test", 1)
        time.sleep(2)
        studentPage.doLogout()
        time.sleep(2)