from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from TestData.PageData import PageData
from pageObjects.AdminPage import AdminPage
from pageObjects.student_related.StudentPageOther import StudentPage
from utilities.BaseClass import BaseClass
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
class TestSkenarioChatting(BaseClass):
    @pytest.mark.parametrize("student_email, student_password",[
        (PageData.student_email, PageData.student_password)
    ])
    @pytest.mark.parametrize("content, username, course", [
        PageData.getTestData("Chats", "testcase4")
    ])
    @pytest.mark.parametrize("instructor_email, instructor_password", [
        PageData.getTestData("LoginData", "testcase3")   
    ])
    @pytest.mark.parametrize("receiver_name, course_name, message", [
      PageData.getTestData("InstructorChatData", "test1"),
    ])
    def test_skenario_chatting(self, setup, student_email, student_password, content, username, course, instructor_email, instructor_password, receiver_name, course_name, message):
        landingPage = LandingPage(self.driver)
        landingPage.doLogin(student_email, student_password)
        time.sleep(2)
        studentPage = StudentPage(self.driver)
        studentPage.goToChats(content, username, course)
        time.sleep(2)
        studentPage.doLogout()
        landingPage.doLogin(instructor_email, instructor_password)
        time.sleep(2)
        instructorPage = InstructorPage(self.driver)

        log = self.getLogger()

        # delay
        def delay(t=0.3):
            time.sleep(t)

        # login
        landingPage.doLogin(email, password)
        delay()
    

        # klik instructor panel
        instructorPage.click_instruction_panel_button()
        delay()

        # tutup pop up cookie
        # instructorPage.click_button_pop_up("aria-label", "Close")
        instructorPage.click_button("Allow cookies")
        delay()

        # scroll ke bawah
        instructorPage.scrollToXY(0, 80)
        delay(1)

        # klik menu chat
        instructorPage.click_menu_side_bar("Chat")
        delay()

        # ======================== PAGE CHAT ========================
        # scroll ke bawah
        instructorPage.scrollToXY(0, 60)
        delay(1)

        # pilih tujuan chat
        instructorPage.click_chat_name(receiver_name, course_name)
        delay(1)

        # isi chat
        instructorPage.enter_field("id", "chat-message", message)
        delay()

        # tekan button send
        instructorPage.click_button("send")
        delay(3)

        # assert message yang dikirim apakah sesuai
        expected_msg = message
        actual_msg = instructorPage.get_chat_message_text("sender")
        log.info(f"Actual message: {actual_msg}")
        