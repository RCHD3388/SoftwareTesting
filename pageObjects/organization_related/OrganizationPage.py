from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class OrganizationPage:

    def __init__(self, driver):
        self.driver = driver

    organization_panel_button = (By.XPATH, "//a[normalize-space()='Organization Panel']")
    panel = (By.XPATH, "//a[normalize-space()='Organization Panel']")
    toast_message = (By.XPATH, "//div[@class='toast-message']")
    
    # SIDEAR
    def getHeadSidebarButton(self, placeholder):
        return (By.XPATH, f"//li[{placeholder}]//span[1]")
    def getChildSidebarButton(self, placeholder):
        return (By.XPATH, f"//a[normalize-space()='{placeholder}']")
    
    # INSTRUCTOR
    add_ins_img = (By.XPATH, "//input[@id='image']")
    def getInsField(self, placeholder):
        return (By.XPATH, f"//input[@placeholder='{placeholder}']")
    def getInsTextarea(self, placeholder):
        return (By.XPATH, f"//textarea[@name='{placeholder}']")
    def getInsFieldSelect(self, type, placeholder):
        return (By.XPATH, f"//select[@{type}='{placeholder}']")
    def getInsButton(self, placeholder):
        return (By.XPATH, f"//button[normalize-space()='{placeholder}']")


    def click_organization_panel_button(self):
        self.driver.find_element(*self.organization_panel_button).click()

    def click_panel(self):
        self.driver.find_element(*self.panel).click()

    def click_sidebar_head_button(self, placeholder):
        self.driver.find_element(*self.getHeadSidebarButton(placeholder)).click()

    def click_sidebar_child_button(self, placeholder):
        self.driver.find_element(*self.getChildSidebarButton(placeholder)).click()

    # INSTRUCTOR
    def enter_ins_img_field(self, value):
        self.driver.find_element(*self.add_ins_img).send_keys(value)
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

    # TOAST MESSAGE
    def getToastMessage(self):
        return self.driver.find_element(*self.toast_message).text
    
    
  
    


    



