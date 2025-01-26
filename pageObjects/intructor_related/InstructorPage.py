from re import S
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class InstructorPage():
    def __init__(self, driver):
        self.driver = driver

    instructor_panel_button = (By.XPATH, "//a[normalize-space()='Instructor Panel']")
    # panel = (By.XPATH, "//a[normalize-space()='Instructor Panel']")
    toast_message = (By.XPATH, "//div[@class='toast-message']")
    upload_lesson = (By.XPATH, "//a[@class='common-upload-lesson-btn font-13 font-medium']")

    def getUploadLessonButton(self):
        return
    
    # SIDEAR
    def getHeadSidebarButton(self, placeholder):
        return (By.XPATH, f"//li[{placeholder}]//span[1]")
    def getChildSidebarButton(self, placeholder):
        return (By.XPATH, f"//a[normalize-space()='{placeholder}']")
    
    # template for xpath
    add_img = (By.XPATH, "//input[@id='image']")
    def getInputTextField(self,type, placeholder):
        return (By.XPATH, f"//input[@{type}='{placeholder}']")
    def getInputTextareaField(self, type, placeholder):
        return (By.XPATH, f"//textarea[@{type}='{placeholder}']")
    def getSelectField(self, type, placeholder):
        return (By.XPATH, f"//select[@{type}='{placeholder}']")
    def getButton(self, placeholder):
        return (By.XPATH, f"//button[normalize-space()='{placeholder}']")
    def getGeneralButton(self, type, placeholder):
        return (By.XPATH, f"//button[@{type}='{placeholder}']")
    def getElementGeneral(self,tag,type,content):
        return (By.XPATH, f"//{tag}[@{type}='{content}']")
        
    def getToastMessage(self):
        wait = WebDriverWait(self.driver, 10)
        success_message_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='toast-message']"))  # Use appropriate locator
        ) 
        return success_message_element.text
    # buat scroll
    def scrollTo(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        # ActionChains(self.driver).move_to_element(element).perform()
    #click element
    def click_element(self,tag,type,content):
        self.scrollTo(self.driver.find_element(*self.getElementGeneral(tag,type,content)))
        return self.driver.find_element(*self.getElementGeneral(tag,type,content)).click()

    # function for instructor page

    # ============================= template =============================
    # img field
    def enter_img_field(self, value):
        self.driver.find_element(*self.add_img).send_keys(value)
    
    # input text field
    def enter_field(self, type, placeholder, value):
        self.driver.find_element(*self.getInputTextField(type,placeholder)).send_keys(value)

    # textarea field
    def enter_textarea(self, type, placeholder, value):
        self.driver.find_element(*self.getInputTextareaField(type, placeholder)).send_keys(value)

    # select field
    def enter_select_field(self, type, placeholder, value):
        select = Select(self.driver.find_element(*self.getSelectField(type, placeholder)))
        select.select_by_visible_text(value)
        
    def click_button(self, placeholder):
        self.driver.find_element(*self.getButton(placeholder)).click()

    # radio button
    def click_radio_button(self, type, placeholder):
        self.driver.find_element(*self.getInputTextField(type, placeholder)).click()

    # isi input with scroll 
    def enter_img_field_scroll(self, value):
        img_element = self.driver.find_element(*self.add_img)
        self.scrollTo(img_element)
        img_element.send_keys(value)

    def enter_field_scroll(self, type, placeholder, value):
        field_element = self.driver.find_element(*self.getInputTextField(type,placeholder))
        self.scrollTo(field_element)
        field_element.send_keys(value)

    def enter_textarea_scroll(self, type, placeholder, value):
        textareaElement = self.driver.find_element(*self.getInputTextareaField(type, placeholder))
        self.scrollTo(textareaElement)
        textareaElement.send_keys(value)

    def enter_select_field_scroll(self, type, placeholder, value):
        selectElement = self.driver.find_element(*self.getSelectField(type, placeholder))
        self.scrollTo(selectElement)
        select = Select(selectElement)
        select.select_by_visible_text(value)

    def click_radio_button_scroll(self, type, placeholder):
        radioElement = self.driver.find_element(*self.getInputTextField(type, placeholder))
        self.scrollTo(radioElement)
        radioElement.click()
        
    def click_button_scroll(self, placeholder):
        btnElement = self.driver.find_element(*self.getButton(placeholder))
        self.scrollTo(btnElement)
        btnElement.click()
  
   
    def click_save_final(self):
        return self.driver.find_element(By.XPATH, "//a[normalize-space()='Save and continue']").click() 

    # ============================= end template =============================

    def click_instruction_panel_button(self):
        self.driver.find_element(*self.instructor_panel_button).click()

    def click_button_pop_up(self,types,placeholder):
        self.driver.find_element(*self.getGeneralButton(types,placeholder)).click()

    def find_button(self, placeholder):
        return self.driver.find_element(*self.getButton(placeholder))

    def click_menu_side_bar(self, placeholder):
        self.driver.find_element(*self.getChildSidebarButton(placeholder)).click()

    def scroll_to_menu(self,placeholder):
        element = self.driver.find_element(*self.getChildSidebarButton(placeholder))
        self.scrollTo(element) 
        
    def verify_waiting_toreview(self):
        try:
            # Wait for the first element with the specific class
            first_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'course-tag badge publish-badge radius-3 font-14 font-medium position-absolute')]"))
            )
            
            # Verify the text of the element
            if first_element.text.strip() == "Waiting for Review":
                print("Element with text 'Waiting for Review' found.")
                return True
            else:
                print(f"Element found, but text is '{first_element.text.strip()}' instead of 'Waiting for Review'.")
                return False
        except Exception as e:
            print(f"Element not found: {e}")
            return False
    
    


    