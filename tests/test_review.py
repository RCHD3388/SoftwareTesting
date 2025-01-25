
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.StudentPage import StudentPage
from utilities.BaseClass import BaseClass

class TestReviews(BaseClass):
    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("rating, review, row", [
        PageData.getTestData("Review", "testcase1")
    ])
    def test_review(self, setup,email, password, rating, review, row):
        landingPage = LandingPage(self.driver)
        time.sleep(2)
        landingPage.doLogin(email, password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        studentPage.doReview(row,rating,review)
        time.sleep(2)
        studentPage.doLogout()
        time.sleep(2)