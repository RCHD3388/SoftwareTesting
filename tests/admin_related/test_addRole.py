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

class TestAddRole(BaseClass):

    @pytest.mark.parametrize("email, password", [
        PageData.getTestData("LoginData", "testcase1")
    ])
    @pytest.mark.parametrize("nama_role, permission1, permission2, permission3, permission4, permission5", [
        PageData.getTestData("PermissionData", "testpermission3")
    ])
    def test_add_role(self, email, password, nama_role, permission1, permission2, permission3, permission4, permission5):
        waktu=2
        landingPage = LandingPage(self.driver)
        manageAdminPage = ManageAdminPage(self.driver)
        adminPage = AdminPage(self.driver)
        landingPage.doLogin(email, password)
        time.sleep(waktu)
        manageAdminPage.click_cookie_button()
        manageAdminPage.click_manage_admin()
        time.sleep(waktu)
        manageAdminPage.click_roles()
        time.sleep(waktu)
        manageAdminPage.clickElement("a", "normalize-space()", "Add Role")
        time.sleep(waktu)
        manageAdminPage.checkBox(permission1)
        time.sleep(waktu)
        manageAdminPage.checkBox(permission2)
        time.sleep(waktu)
        manageAdminPage.checkBox(permission3)
        time.sleep(waktu)
        manageAdminPage.checkBox(permission4)
        time.sleep(waktu)
        manageAdminPage.checkBox(permission5)
        time.sleep(waktu)
        manageAdminPage.insert_input_field("input", "id", "name", nama_role)
        time.sleep(waktu)
        manageAdminPage.click_save_button()
        time.sleep(waktu)