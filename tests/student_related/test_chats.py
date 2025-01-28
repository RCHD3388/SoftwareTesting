
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.student_related.StudentPageOther import StudentPage
from utilities.BaseClass import BaseClass

class TestChats(BaseClass):
    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase4")
    ])
    @pytest.mark.parametrize("content, username, course", [
        PageData.getTestData("Chats", "testcase1"),
        PageData.getTestData("Chats", "testcase2"),
    ])
    def test_chats(self, setup, email, password, content, username, course):
        landingPage = LandingPage(self.driver)
        landingPage.doLogin(email, password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        studentPage.goToChats(content, username, course)
        time.sleep(2)
        assert studentPage.getLatestChat() == content
        