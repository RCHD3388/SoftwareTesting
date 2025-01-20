from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class InstructorPage:

    def __init__(self, driver):
        self.driver = driver

    def open_instructor_panel(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Instructor Panel']").click()
    def open_upload_course(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Upload Course')]").click()
        
  
  
    


    



