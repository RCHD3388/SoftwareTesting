from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class ManageAdminPage:

    def __init__(self, driver):
        self.driver = driver

    
    manage_admin = (By.XPATH,"(//a[@class='has-arrow'])[15]")
    add_user = (By.XPATH,"//span[normalize-space()='Add User']")
    roles = (By.XPATH,"//span[normalize-space()='Roles']")
    
    close_cookie = (By.CLASS_NAME, "btn-close front-close-btn")
    element = (By.XPATH,"(//a[@class='has-arrow'])[21]")
    cookie_button = (By.XPATH,"//button[normalize-space()='Allow cookies']")

    toast_message = (By.XPATH, "//div[@class='toast-message']")

    save_btn = (By.XPATH,"//input[@name='save']")

    def getCheckBox(self, placeholder):
        return (By.XPATH, f"//input[@id='{placeholder}']")
    
    def checkBox(self, placeholder):
        return self.driver.find_element(*self.getCheckBox(placeholder)).click()

    def getElement(self,tag,type,content):
        return (By.XPATH, f"//{tag}[{type}='{content}']")
    def clickElement(self,tag,type,content):
        return self.driver.find_element(*self.getElement(tag,type,content)).click()
    def insert_input_field(self,tag,type,placeholder, value):
        self.driver.find_element(By.XPATH, f"//{tag}[@{type}='{placeholder}']").send_keys(value)
    def click_manage_admin(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.element)).perform()
        self.driver.find_element(*self.manage_admin).click()
    
    def getInsFieldSelect(self, type, placeholder):
        return (By.XPATH, f"//select[@{type}='{placeholder}']")

    def enter_ins_select_field(self, type, placeholder, value):
        select = Select(self.driver.find_element(*self.getInsFieldSelect(type, placeholder)))
        select.select_by_visible_text(value)
    def click_add_admin(self):
        self.driver.find_element(*self.add_user).click()
      
    def click_roles(self):
        self.driver.find_element(*self.roles).click()
    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()
    
    def click_save_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.save_btn)).perform()
        self.driver.find_element(*self.save_btn).click()
    
    def getToastMessage(self):
        wait = WebDriverWait(self.driver, 10)
        success_message_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='toast-message']"))  
        ) 
        return success_message_element.text

    def create_super_admin(self, username,  role,  area, email_admin, password_admin, address, phone):
        waktu = 2  # Define waktu variable
        self.click_cookie_button()
        self.click_manage_admin()
        time.sleep(waktu)
        self.click_add_admin()
        time.sleep(waktu)
        self.insert_input_field("input", "id", "name", username)
        time.sleep(waktu)
        self.enter_ins_select_field("name", "area_code", area)
        time.sleep(waktu)
        self.insert_input_field("input", "id", "email", email_admin)
        self.insert_input_field("input", "id", "password", password_admin)
        self.insert_input_field("textarea", "id", "address", address)
        self.enter_ins_select_field("id", "role_name", role)
        self.insert_input_field("input", "id", "phone_number", phone)
        time.sleep(waktu)
        self.click_save_button()
        time.sleep(waktu)
        actual_message = self.getToastMessage()
        expected_message = "User successfully created"
        assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"
        time.sleep(20)
    
    


    


    



