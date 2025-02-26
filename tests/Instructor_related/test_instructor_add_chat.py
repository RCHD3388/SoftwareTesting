import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from utilities.BaseClass import BaseClass

import os

class TestInstructorAddChat(BaseClass):
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("receiver_name, course_name, message", [
      PageData.getTestData("InstructorChatData", "test1"),
      PageData.getTestData("InstructorChatData", "test2")
    ])
    def test_instructor_add_chat(self,email, password, receiver_name, course_name, message):
        landingPage = LandingPage(self.driver)
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

        assert expected_msg == actual_msg
        
        delay(2)