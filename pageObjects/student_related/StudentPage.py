from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class StudentPage:

    def __init__(self, driver):
        self.driver = driver

    become_instructor = (By.XPATH, "//a[normalize-space()='Become an Instructor']")
    become_instructor_toast_message = (By.XPATH, "(//button[@class='theme-btn theme-button1 theme-button3 mr-30'][normalize-space()='Become an Instructor'])[1]")
    become_instructor_toast_message_locator = (By.XPATH, "(//*[name()='polyline'])[1]")
    add_insert_cv = (By.XPATH, "//input[@name='cv_file']")
    input_bio = (By.XPATH, "//textarea[@placeholder='About your self']")
    input_bio2 = (By.XPATH, "/html/body/div[3]/div/div/form/div[1]/div[8]/div/textarea")
    course_dropdown = (By.XPATH, "//a[@id='librariesDropdown']")
    all_course = (By.XPATH, "//a[normalize-space()='All Courses']")
    close_cookies_permission = (By.XPATH, "/html/body/div[3]/button")
    Duration_filter = (By.XPATH, "//input[@id='exampleRadiosDuration37']")

    shopping_cart_button = (By.XPATH, "//a[@aria-current='page']//*[name()='svg']")
    course_thumbnail = (By.XPATH, "(//div[@class='course-img-wrap overflow-hidden'])[2]")

    button_enroll = (By.XPATH, "//span[@class='msgInfoChange']")
    profile_img = (By.XPATH, "//img[@alt='user']")
    profile_dropdown = (By.XPATH, "//a[@id='dropdownUser']//img[@alt='icon']")

    country_select = (By.XPATH, "//*[@id='country_id']/option[2]")
    pay_paypal = (By.XPATH, "//div[@class='regular-btn']//button[@type='submit']")

    def click_profile_dropdown(self):
        self.driver.find_element(*self.profile_dropdown).click()

    # scroll to x and y
    def scrollToXY(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, window.innerHeight * {y} /100);")

    def get_arial_label(self, placeholder):
        return (By.XPATH, f"//button[@aria-label='{placeholder}']")
    def get_hidden_element(self):
        return (By.NAME, "country_id")

    def combo_box_select (self, placeholder, index):
        return (By.XPATH, f"//*[@id='{placeholder}']/option[{index}]")
    
    def click_combo_box_select (self, placeholder, index):
        self.driver.find_element(*self.combo_box_select(placeholder,index)).click()

    def click_pay_paypal (self):
        self.driver.find_element(*self.pay_paypal).click()

    def click_combo_box_select (self, placeholder, index):
        self.driver.find_element(*self.combo_box_select(placeholder, index)).click()

    def get_span_normalize_space(self, placeholder):
        return (By.XPATH, f"//span[normalize-space()='{placeholder}']")
        
    def getInsertField(self, placeholder):
        return (By.XPATH, f"//input[@id='{placeholder}']")

    def getInsertFieldName(self, placeholder):
        return (By.XPATH, f"//input[@name='{placeholder}']")

    def getCheckBoxField(self, placeholder):
        return (By.XPATH, f"//input[@id='{placeholder}']")

    def getSelectField(self, placeholder):
        return (By.XPATH, f"//select[@id='{placeholder}']")
    
    def getMenu(self, placeholder):
        return(By.XPATH, f"//a[normalize-space()='{placeholder}']")
    
    def getMenuElement(self, placeholder):
        return self.driver.find_element(*self.getMenu(placeholder))
    
    def get_label(self, placeholder):
        return(By.XPATH, f"//label[normalize-space()='{placeholder}']")

    def getMenuh6(self, placeholder):
        return(By.XPATH, f"//h6[normalize-space()='{placeholder}']")

    def get_button_byid(self, placeholder):
        return (By.XPATH, f"//button[@id='{placeholder}']")

    def click_button_byid(self, placeholder):
        self.driver.find_element(*self.get_button_byid(placeholder)).click()

    def click_insert_field_name(self, placeholder):
        self.driver.find_element(*self.getInsertFieldName(placeholder)).click()

    def click_button_enroll(self):
        self.driver.find_element(*self.button_enroll).click()

    def click_shopping_cart_button(self):
        self.driver.find_element(*self.shopping_cart_button).click()
    def getInsertTextarea(self, value):
        self.driver.find_element(*self.input_bio2).send_keys(value)

    def click_checkbox_field(self, placeholder):
        self.driver.find_element(*self.getCheckBoxField(placeholder)).click()

    def click_close_cookies_permission(self):
        self.driver.find_element(*self.close_cookies_permission).click()
    
    def getInsertButton (self, placeholder):
        return (By.XPATH, f"//button[normalize-space()='{placeholder}']")

    def click_menu(self, placeholder):
        self.driver.find_element(*self.getMenu(placeholder)).click()

    def click_menu_h6(self, placeholder):
        self.driver.find_element(*self.getMenuh6(placeholder)).click()

    def click_become_instructor(self):
        self.driver.find_element(*self.become_instructor).click()

    def click_become_instructor_toast_message(self):
        self.driver.find_element(*self.become_instructor_toast_message).click()
    
    def enter_insert_field(self, placeholder, value):
        self.driver.find_element(*self.getInsertField(placeholder)).send_keys(value)

    # def enter_insert_textarea(self, placeholder, value):
    #     self.driver.find_element(*self.getInsertTextarea(placeholder)).send_keys(value)

    def enter_insert_cv(self, value):
        self.driver.find_element(*self.add_insert_cv).send_keys(value)

    def click_insert_button(self, placeholder):
        self.driver.find_element(*self.getInsertButton(placeholder)).click()

    def move_to_course_dropdown(self):
        return self.driver.find_element(*self.course_dropdown)

    def click_select_field(self, placeholder):
        self.driver.find_element(*self.getSelectField(placeholder)).click()

    def click_label(self, placeholder):
        self.driver.find_element(*self.get_label(placeholder)).click()

    def click_arial_label(self, placeholder):
        self.driver.find_element(*self.get_arial_label(placeholder)).click()