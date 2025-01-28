from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.PageData import PageData
from pageObjects.LandingPage import LandingPage
from pageObjects.admin_related.ManageAdminPage import ManageAdminPage
from pageObjects.admin_related.AdminPage import AdminPage
from utilities.BaseClass import BaseClass
import os
from selenium.webdriver.common.action_chains import ActionChains

class TestAddAdmin(BaseClass):

    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("nama, email_admin, area, phone, address, role, password_admin", [
        PageData.getTestData("AdminData", "testcaseadmin1")
    ])
    def test_add_admin(self, nama, email, area, phone, address, role, password, email_admin, password_admin):
        waktu=2
        landingPage = LandingPage(self.driver)
        manageAdminPage = ManageAdminPage(self.driver)
        adminPage = AdminPage(self.driver)
        landingPage.doLogin(email, password)
        time.sleep(waktu)
        manageAdminPage.create_super_admin(nama,  role, area, email_admin, password_admin, address, phone)
