from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class SkenarioPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    profile = (By.XPATH, "//a[@id='dropdownUser']//img[@alt='icon']")
    change_button = (By.XPATH, "//a[@class='dropdown-item']//span[contains(text(),'Change Password')]")
    newpassword = "yv6w3be7wb1"
    logout_buton = (By.XPATH, "//ul[@class='dropdown-menu show']//li[3]//a[1]")
    submit_update = (By.XPATH, "//input[@name='update']")
    toast_message = (By.XPATH, "//div[@class='toast-message']")

    def scrollTo(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        time.sleep(0.2) 

    def fillinput(self, placeholder, value):
        element = self.driver.find_element(By.XPATH, f"//input[@id='{placeholder}']")
        self.driver.execute_script("arguments[0].value = arguments[1]", element, value)

    def click_profile(self):
        element = self.driver.find_element(*self.profile)
        self.scrollTo(element)
        time.sleep(0.5)
        element.click()

    def click_changepassword(self):
        element = self.driver.find_element(*self.change_button)
        self.scrollTo(element)
        time.sleep(0.5)
        element.click()

    def click_updatepassword(self):
        element = self.driver.find_element(*self.submit_update)
        self.scrollTo(element)
        time.sleep(0.5)
        element.click()

    def click_logout(self):
        element = self.driver.find_element(*self.logout_buton)
        self.scrollTo(element)
        time.sleep(0.5)
        element.click()

    def getToastMessage(self):
        return self.driver.find_element(*self.toast_message).text

        
    
  
    


    



