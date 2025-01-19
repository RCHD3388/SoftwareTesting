from selenium.webdriver.common.by import By

class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    login_button = (By.XPATH, "//a[normalize-space()='Sign In']")
    login_username = (By.XPATH, "//input[@placeholder='Type your email or phone number']")
    login_password = (By.XPATH, "//input[@placeholder='*********']")
    login_submit_button = (By.XPATH, "//button[normalize-space()='Sign In']")

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def enter_username(self, username):
        self.driver.find_element(*self.login_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.login_password).send_keys(password)

    def click_login_submit_button(self):
        self.driver.find_element(*self.login_submit_button).click()
    




