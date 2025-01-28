import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.intructor_related.InstructorPage import InstructorPage
from utilities.BaseClass import BaseClass

import os

class TestInstructorReplyDiscussionChat(BaseClass):
    
    @pytest.mark.parametrize("email, password", [
      PageData.getTestData("LoginData", "testcase3")
    ])
    @pytest.mark.parametrize("message, receiver_name", [
      PageData.getTestData("InstructorDiscussionReplyData", "test1"),
      PageData.getTestData("InstructorDiscussionReplyData", "test2")
    ])
    def test_instructor_reply_discussion(self,email, password, message, receiver_name):
        landingPage = LandingPage(self.driver)
        instructorPage = InstructorPage(self.driver)

        log = self.getLogger()
        log.info(f"Receiver name {receiver_name}")

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
        instructorPage.click_menu_side_bar("Discussion")
        delay()

        # ======================== PAGE CHAT ========================
        # scroll ke bawah
        instructorPage.scrollToXY(0, 60)
        delay(1)

        # isi chat
        instructorPage.enter_discussion_chat_reply("name","commentReply",message)
        delay()

        # tekan button reply
        instructorPage.click_reply_button("span","class","default-hover-btn")
        delay(1)

        # assert reply chat sukses
        expected_message = "Replied successful."
        actual_message = instructorPage.getToastMessage()
        delay()
        assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"
        
        delay(2)