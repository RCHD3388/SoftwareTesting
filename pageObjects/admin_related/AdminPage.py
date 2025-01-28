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
    manage_student = (By.XPATH,"(//a[@class='has-arrow'])[5]")
    add_instructor = (
        By.CSS_SELECTOR,"a[href='http://localhost:8000/admin/instructor/create']"
    )
    manage_course = (By.XPATH,"(//a[@class='has-arrow'])[1]")

    close_cookie_button = (By.CLASS_NAME,"btn-close front-close-btn")
    
    review_pending = (By.CSS_SELECTOR,"a[href='http://localhost:8000/admin/course/review-pending']")
    all_instructors = (By.XPATH,"//span[normalize-space()='All Instructors']")
    edit_instructor = (By.XPATH,"//tr[@class='removable-item odd']//img[@alt='edit']")
    delete_instructor = (By.XPATH,"//tr[@class='removable-item odd']//img[@alt='trash']")
    confirm_delete = (By.XPATH,"//button[normalize-space()='Yes, Delete It!']")
    all_organizations = (By.XPATH,"//span[normalize-space()='All Organizations']")
    manage_coupon = (By.XPATH,"//a[@class='has-arrow'])[7]")
    all_students = (By.XPATH,"//span[normalize-space()='All Student']")
    add_student = (By.XPATH,"//span[normalize-space()='Add Student']")
    
    def click_manage_student(self):
        return self.driver.find_element(*self.manage_student).click()
    def click_all_students(self):
        return self.driver.find_element(*self.all_students).click()
    def click_add_student(self):
        return self.driver.find_element(*self.add_student).click()
    
    
    def getElement(self,tag,type,content):
        return (By.XPATH, f"//{tag}[@{type}='{content}']")
    def click_delete_instructor(self):
        return self.driver.find_element(*self.delete_instructor).click()
    def clickElement(self,tag,type,content):
        return self.driver.find_element(*self.getElement(tag,type,content)).click()
    def click_confirm_delete(self):
        return self.driver.find_element(*self.confirm_delete).click()
    def click_close_cookie(self):
        return self.driver.find_element(*self.close_cookie_button).click()

    def click_all_instructors(self):
        return self.driver.find_element(*self.all_instructors).click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    def click_all_organizations(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.add_organization)).perform()
        return self.driver.find_element(*self.all_organizations).click()

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
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.manage_organization)).perform()
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

    def click_all_instructors(self):
        self.driver.find_element(*self.all_instructors).click()
    def click_manage_instructor(self):
        self.driver.find_element(*self.manage_instructor).click()
    def click_add_instructor(self):
        self.driver.find_element(*self.add_instructor).click()
    def click_manage_course(self):
        self.driver.find_element(*self.manage_course).click()
    def click_review_pending(self):
        self.driver.find_element(*self.review_pending).click()
    
    def getElemenet(self,tag,type,content):
        return (By.XPATH, f"//{tag}[{type}='{content}']")
    def click_element(self,tag,type,content):
        return self.driver.find_element(*self.getElement(tag,type,content)).click()
    
    def click_approve_button(self):
    # Check if the element exists
        elements = self.driver.find_elements(By.XPATH, "(//a[@title='Make as Active'][normalize-space()='Approve'])[1]")
        
        if elements:
            # If the element exists, click the first one
            elements[0].click()
            print("Approve button clicked.")
            return True
        else:
            # If the element does not exist
            print("Approve button does not exist.")
            return False
    def click_edit_instructor(self):
        self.driver.find_element(*self.edit_instructor).click()


    



