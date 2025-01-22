
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.StudentPage import StudentPage
from utilities.BaseClass import BaseClass

class TestBlogs(BaseClass):

    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("content, title", [
        PageData.getTestData("BlogReply", "testcase1")
    ])
    def test_blogs(self, setup, email, password,content,title):
        landingPage = LandingPage(self.driver)
        landingPage.doLogin(email, password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        time.sleep(2)
        studentPage.goToBlogs(content,title)
        time.sleep(2)