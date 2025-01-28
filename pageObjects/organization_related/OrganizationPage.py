from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class OrganizationPage:

    def __init__(self, driver):
        self.driver = driver

    organization_panel_button = (By.XPATH, "//a[normalize-space()='Organization Panel']")
    panel = (By.XPATH, "//a[normalize-space()='Organization Panel']")
    toast_message = (By.XPATH, "//div[@class='toast-message']")
    checkbox_add_bundle = (By.XPATH, "//*[@class='form-check-input addBundle ']")
    delete_bundle = (By.XPATH, "//*[@class='deleteItem para-color font-14 font-medium d-flex align-items-center']")
    viewnotice = (By.XPATH, "//tbody/tr[1]/td[3]/div[1]/a[2]")
    dashboard_consult = (By.XPATH, "//ul[@class='account-sub-menu']//a[contains(text(),'Dashboard')]")

    submitupdateConsultDash = (By.XPATH, "//div[@class='are-you-available-box mb-30']//button[@type='submit'][normalize-space()='Save']")

    def scrollTo(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        time.sleep(0.2) 

    def getByClass(self, placeholder):
        return (By.XPATH, f"//*[@class='{placeholder}']")

    # SIDEAR
    edit_ins_button = (By.XPATH, "//tbody/tr[1]/td[9]/a[1]/img[1]")
    edit_std_button = (By.XPATH, "//tbody/tr[1]/td[6]/a[1]/img[1]")
    def getHeadSidebarButton(self, placeholder):
        return (By.XPATH, f"//li[{placeholder}]//span[1]")
    def getChildSidebarButton(self, placeholder):
        return (By.XPATH, f"//a[normalize-space()='{placeholder}']")

    def getInputById(self, placeholder):
        return (By.XPATH, f"//input[@id='{placeholder}']")

    # INSTRUCTOR
    add_ins_img = (By.XPATH, "//input[@id='image']")
    def getInsField(self, placeholder):
        return (By.XPATH, f"//input[@placeholder='{placeholder}']")
    def getInsTextarea(self, type, placeholder):
        return (By.XPATH, f"//textarea[@{type}='{placeholder}']")
    def getInsFieldSelect(self, type, placeholder):
        return (By.XPATH, f"//select[@{type}='{placeholder}']")
    def getInsButton(self, placeholder):
        return (By.XPATH, f"//button[normalize-space()='{placeholder}']")


    def click_organization_panel_button(self):
        self.driver.find_element(*self.organization_panel_button).click()

    def click_panel(self):
        self.driver.find_element(*self.panel).click()

    def delay(self, t=0.5):
        time.sleep(t)
    # ====================================================================
    def click_sidebar_head_button(self, placeholder):
        self.scrollTo(self.driver.find_element(*self.getHeadSidebarButton(placeholder)))
        time.sleep(0.5)
        self.driver.find_element(*self.getHeadSidebarButton(placeholder)).click()

    def click_sidebar_child_button(self, placeholder):
        self.scrollTo(self.driver.find_element(*self.getChildSidebarButton(placeholder)))
        time.sleep(0.5)
        self.driver.find_element(*self.getChildSidebarButton(placeholder)).click()

    # INSTRUCTOR
    def enter_ins_img_field(self, value):
        self.scrollTo(self.driver.find_element(*self.add_ins_img))
        self.driver.find_element(*self.add_ins_img).send_keys(value)
    def enter_ins_field(self, placeholder, value):
        element = self.driver.find_element(*self.getInsField(placeholder))
        self.scrollTo(element)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
    def enter_ins_textarea(self, placeholder, value, type="name"):
        element=self.driver.find_element(*self.getInsTextarea(type, placeholder))
        self.scrollTo(element)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
    def enter_ins_select_field(self, type, placeholder, value):
        select = Select(self.driver.find_element(*self.getInsFieldSelect(type, placeholder)))
        self.scrollTo(self.driver.find_element(*self.getInsFieldSelect(type, placeholder)))
        select.select_by_visible_text(value)
    def click_ins_button(self, placeholder):
        self.scrollTo(self.driver.find_element(*self.getInsButton(placeholder)))
        time.sleep(0.5)
        self.driver.find_element(*self.getInsButton(placeholder)).click()
    def click_edit_ins_button(self):
        self.scrollTo(self.driver.find_element(*self.edit_ins_button))
        self.driver.find_element(*self.edit_ins_button).click()
    def click_edit_ins_status(self, value):
        select = Select(self.driver.find_element(*self.edit_ins_status))
        self.scrollTo(self.driver.find_element(*self.edit_ins_status))
        select.select_by_visible_text(value)

    # STUDENT
    def click_edit_std_button(self):
        self.scrollTo(self.driver.find_element(*self.edit_std_button))
        self.driver.find_element(*self.edit_std_button).click()
    def click_detail_insstd(self, email):
        email_td = self.driver.find_element(By.XPATH, f"//td[contains(text(), '{email}')]")
        self.scrollTo(email_td)
        # Dari td tersebut, naik ke parent tr dan cari td terakhir di dalam tr tersebut
        last_td_in_row = email_td.find_element(By.XPATH, "./../td[last()]")
        last_td_in_row.click()

    # BUNDLE COURSE
    def checked_all_coursebundle(self): 
        elements = self.driver.find_elements(*self.checkbox_add_bundle)
        for element in elements:
            self.scrollTo(element)
            self.driver.execute_script("arguments[0].checked = true;", element)
            self.delay()
    def click_done_bundle(self):
        xpath = (By.XPATH, "//a[normalize-space()='Done']")
        element = self.driver.find_element(*xpath)
        self.scrollTo(element)
        self.delay()
        element.click()
    def click_delete_bundle(self):
        element = self.driver.find_elements(*self.delete_bundle)[0]
        self.scrollTo(element)
        self.delay()
        element.click()

    def get_elms_a_classes(self, placeholder):
        return self.driver.find_elements(By.XPATH, f"//a[@class='{placeholder}']")
    def getHeaderCardBundle(self):
        element = self.driver.find_elements(By.XPATH, "//*[@class='card-title course-title']/a")[0]
        self.scrollTo(element)
        self.delay()
        return element

    # NOTICE
    def click_viewNotice(self):
        element = self.driver.find_element(*self.viewnotice)
        self.scrollTo(element)
        self.delay()
        element.click()
    def click_notice_button_bar(self, topic, index=3):
        topic_td = self.driver.find_element(By.XPATH, f"//td[contains(text(), '{topic}')]")
        # dapatkan tombol delete
        last_td_in_row = topic_td.find_element(By.XPATH, f"./../td[last()]/div[1]/a[{index}]")
        self.scrollTo(topic_td)
        self.delay()
        last_td_in_row.click()

    # consultation
    def click_dashboard_consult(self):
        element = self.driver.find_element(*self.dashboard_consult)
        self.scrollTo(element)
        self.delay()
        element.click()
    
    def get_inputdashboard(self, placeholder):
        element = self.driver.find_element(*self.getInputById(placeholder))
        self.scrollTo(element)
        self.delay()
        return element
    
    def get_textareadashboard(self):
        element = self.driver.find_element(By.XPATH, "//textarea[@id='offlineMessageText']")
        self.scrollTo(element)
        self.delay()
        return element
    
    def click_consultsubmit(self):
        element = self.driver.find_element(*self.submitupdateConsultDash)
        self.scrollTo(element)
        self.delay()
        element.click()

    
    # TOAST MESSAGE
    def getToastMessage(self):
        return self.driver.find_element(*self.toast_message).text

        
    
  
    


    



