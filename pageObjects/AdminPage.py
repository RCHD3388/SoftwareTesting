from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.instructorComboBox = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/a")
        self.pendingInstructor = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[1]/a")
        self.pendingInstructorApproveButton = (By.XPATH, "//*[@id='customers-table']/tbody/tr/td[7]/div/a[1]")
        self.profile = (By.XPATH, "//*[@id='dropdownUser']")
        self.logoutButton = (By.XPATH, "/html/body/div[3]/header/div/div/div/div/div[2]/ul/li[3]/ul/li[3]/a/span")
        #forum nav
        self.forum_button = (By.XPATH, "//*[@id='sidebar-menu']/li[25]/a")
        self.forum_category = (By.XPATH, "//*[@id='sidebar-menu']/li[25]/ul/li/a/span")
        self.add_category = (By.XPATH, "//button[normalize-space()='Add Forum Category']")
        #forum page
        self.forum_category_title = (By.XPATH, "//*[@id='title']")
        self.forum_category_subtitle = (By.XPATH, "//*[@id='subtitle']")
        self.forum_category_status = (By.XPATH, "//*[@id='status']")
        self.forum_category_image = (By.XPATH, "//*[@id='logo']")
        self.forum_category_submit = (By.XPATH, "//*[@id='add-todo-modal']/div/div/form/div/div[5]/button")

    def getInstructorComboBox(self):
        return self.driver.find_element(*self.instructorComboBox)

    def getPendingInstructor(self):
        return self.driver.find_element(*self.pendingInstructor)
    
    def getPendingInstructorApproveButton(self):
        return self.driver.find_element(*self.pendingInstructorApproveButton)
    
    def doApproveInstructor(self):
        self.getInstructorComboBox().click()
        self.getPendingInstructor().click()
        self.getPendingInstructorApproveButton().click()
    def getProfile(self):
        return self.driver.find_element(*self.profile)
    def getLogoutButton(self):
        return self.driver.find_element(*self.logoutButton)
    def doLogout(self):
        wait = WebDriverWait(self.driver, 10)
        profile = wait.until(EC.element_to_be_clickable(self.profile))
        profile.click()
        time.sleep(1)  # Wait for dropdown animation
        logout = wait.until(EC.element_to_be_clickable(self.logoutButton))
        logout.click()
        
    def getForumButton(self):
        return self.driver.find_element(*self.forum_button)

    def getForumCategory(self):
        return self.driver.find_element(*self.forum_category)

    def getAddCategoryButton(self):
        return self.driver.find_element(*self.add_category)

    def getForumCategoryTitle(self):
        return self.driver.find_element(*self.forum_category_title)

    def getForumCategorySubtitle(self):
        return self.driver.find_element(*self.forum_category_subtitle)

    def getForumCategoryStatus(self):
        return self.driver.find_element(*self.forum_category_status)

    def getForumCategoryImage(self):
        return self.driver.find_element(*self.forum_category_image)

    def getForumCategorySubmit(self):
        return self.driver.find_element(*self.forum_category_submit)
    
    def doInputForumCategory(self, title, subtitle, status):
        self.getForumCategoryTitle().send_keys(title)
        self.getForumCategorySubtitle().send_keys(subtitle)
        self.getForumCategoryStatus().send_keys(status)
    
        self.getForumCategorySubmit().click()