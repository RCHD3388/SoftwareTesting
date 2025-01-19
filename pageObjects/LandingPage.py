from selenium.webdriver.common.by import By

class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    login_button = (By.XPATH, "//a[normalize-space()='Sign In']")

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()





