
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
        PageData.getTestData("LoginData", "testcase4")
    ])
    @pytest.mark.parametrize("review,row, rating ", [
        PageData.getTestData("Review", "testcase1")
    ])
    def test_review(self, setup,email, password, rating, review, row):
        landingPage = LandingPage(self.driver)
        time.sleep(2)
        landingPage.doLogin(email, password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        studentPage.doReview(row,rating,review)
        time.sleep(1)
        assert studentPage.getReviewsToastMessage() == "Review Created Successful."