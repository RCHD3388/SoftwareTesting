from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    # LOGIN
    login_button = (By.XPATH, "//a[normalize-space()='Sign In']")
    login_username = (By.XPATH, "//input[@placeholder='Type your email or phone number']")
    login_password = (By.XPATH, "//input[@placeholder='*********']")
    login_submit_button = (By.XPATH, "//button[normalize-space()='Sign In']")

    # REGISTER
    register_button = (By.XPATH, "//a[normalize-space()='Create an Account']")
    register_code = (By.XPATH, "//select[@name='area_code']")
    register_submit_button = (By.XPATH, "//button[normalize-space()='Sign Up']")
    register_toast_message = (By.XPATH, "//div[@class='toast-message']")

    def scrollTo(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    def getElementGeneral(self,tag,type,content):
        return (By.XPATH, f"//{tag}[@{type}='{content}']")
    
    def getRegisterField(self, placeholder):
        return (By.XPATH, f"//input[@id='{placeholder}']")
    
    def getChildSidebarButton(self, placeholder):
        return (By.XPATH, f"//a[normalize-space()='{placeholder}']")

    # LOGIN
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def enter_username(self, username):
        self.driver.find_element(*self.login_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.login_password).send_keys(password)

    def click_login_submit_button(self):
        self.driver.find_element(*self.login_submit_button).click()
    
    # REGISTER
    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def enter_code(self, code):
        select = Select(self.driver.find_element(*self.register_code))
        select.select_by_visible_text(code)

    def enter_register_field(self, placeholder, value):
        self.driver.find_element(*self.getRegisterField(placeholder)).send_keys(value)

    def click_register_submit_button(self):
        self.driver.find_element(*self.register_submit_button).click()

    def getRegisterToastMessage(self):
        return self.driver.find_element(*self.register_toast_message).text
    
    #  LOGOUT
    def click_button_profile(self):
        self.driver.find_element(*self.getElementGeneral("img","alt","user")).click()
        time.sleep(1)

    def click_button_logout(self):
        elemen = self.driver.find_element(*self.getChildSidebarButton("Logout"))
        self.scrollTo(elemen)
        elemen.click()
        time.sleep(1)

    def doLogin(self, username, password): 
      time.sleep(2)    

      # click go to login page
      self.click_login_button()
      time.sleep(0.5)

      # enter username
      self.enter_username(username)
      time.sleep(0.5)
      # enter password
      self.enter_password(password)
      time.sleep(0.5)
      # click login button
      self.click_login_submit_button()

    def doLogout(self):
        # tekan button profile
        self.click_button_profile()

        # cari menu my wallet
        menu_my_wallet = self.driver.find_element(*self.getChildSidebarButton("My Wallet"))

        # scroll ke menu my wallet
        self.scrollTo(menu_my_wallet)

        # tekan button logout
        self.click_button_logout()



