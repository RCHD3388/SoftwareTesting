from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TestData.PageData import PageData
from pageObjects.AdminPage import AdminPage
from pageObjects.StudentPage import StudentPage
from utilities.BaseClass import BaseClass
from pageObjects.LandingPage import LandingPage


class TestForumDiscussion(BaseClass):
    @pytest.mark.parametrize("admin_email, admin_password", [
        PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("student_email, student_password", [
        PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("title, subtitle, status", [
        PageData.getTestData("ForumDiscussion", "testcase1")
    ])
    def test_forum_discussion(self, setup, admin_email, admin_password, student_email, student_password, title, subtitle, status):
        # Set up wait
        wait = WebDriverWait(self.driver, 10)
        
        # Login as admin
        landingPage = LandingPage(self.driver)
        landingPage.doLogin(admin_email, admin_password)
        time.sleep(2)
        
        # Initialize admin page
        adminPage = AdminPage(self.driver)
        
        # Click forum button using JavaScript
        forum_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sidebar-menu']/li[25]/a")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", forum_button)
        self.driver.execute_script("arguments[0].click();", forum_button)
        time.sleep(1)
        
        # Click forum category using JavaScript
        forum_category = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sidebar-menu']/li[25]/ul/li/a/span")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", forum_category)
        self.driver.execute_script("arguments[0].click();", forum_category)
        time.sleep(1)
        
        # Click add category button
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Forum Category']")))
        add_button.click()
        time.sleep(1)
        
        # Input forum category details
        adminPage.doInputForumCategory(title, subtitle, status)
        time.sleep(2)
        
        adminPage.doLogout()
        time.sleep(2)
        
        # Login as student
        studentPage = StudentPage(self.driver)
        landingPage.doLogin(student_email, student_password)
        
        studentPage.doCreateForumQuestion(title, subtitle, status)
        time.sleep(2)
        
        studentPage.doLogout()
        time.sleep(2)