from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    manage_organization = (By.XPATH,"(//a[@class='has-arrow'])[4]")
    add_organization = (
        By.CSS_SELECTOR,"a[href='http://localhost:8000/admin/organizations/create']"
    )

    manage_instructor = (By.XPATH,"(//a[@class='has-arrow'])[3]")
    add_instructor = (
        By.CSS_SELECTOR,"a[href='http://localhost:8000/admin/instructor/create']"
    )
    
    def getInsFieldSelect(self, type, placeholder):
        return (By.XPATH, f"//select[@{type}='{placeholder}']")
    def getInsField(self, placeholder):
        return (By.XPATH, f"//input[@placeholder='{placeholder}']")
    def enter_ins_select_field(self, type, placeholder, value):
        select = Select(self.driver.find_element(*self.getInsFieldSelect(type, placeholder)))
        select.select_by_visible_text(value)
    def getInsButton(self, placeholder):
        return (By.XPATH, f"//button[normalize-space()='{placeholder}']")
    def getInsTextarea(self, placeholder):
        return (By.XPATH, f"//textarea[@name='{placeholder}']")
    
    def click_manage_organization(self):
        self.driver.find_element(*self.manage_organization).click()
    def click_add_organization(self):
        self.driver.find_element(*self.add_organization).click()
    def enter_ins_field(self, placeholder, value):
        self.driver.find_element(*self.getInsField(placeholder)).send_keys(value)
    def enter_ins_textarea(self, placeholder, value):
        self.driver.find_element(*self.getInsTextarea(placeholder)).send_keys(value)
    def enter_ins_select_field(self, type, placeholder, value):
        select = Select(self.driver.find_element(*self.getInsFieldSelect(type, placeholder)))
        select.select_by_visible_text(value)
    def click_ins_button(self, placeholder):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.getInsButton(placeholder))).perform()
        self.driver.find_element(*self.getInsButton(placeholder)).click()

    def click_manage_instructor(self):
        self.driver.find_element(*self.manage_instructor).click()
    def click_add_instructor(self):
        self.driver.find_element(*self.add_instructor).click()
    
  
    


    



