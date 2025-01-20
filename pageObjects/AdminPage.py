from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.instructorComboBox = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/a")
        self.pendingInstructor = (By.XPATH, "//*[@id='sidebar-menu']/li[4]/ul/li[1]/a")
        self.pendingInstructorApproveButton = (By.XPATH, "//*[@id='customers-table']/tbody/tr/td[7]/div/a[1]")

    def getInstructorComboBox(self):
        return self.driver.find_element(*self.instructorComboBox)

    def getPendingInstructor(self):
        return self.driver.find_element(*self.pendingInstructor)

    def getPendingInstructorApproveButton(self):
        return self.driver.find_element(*self.pendingInstructorApproveButton)

    def approvePendingInstructor(self):
        self.getInstructorComboBox().click()
        self.getPendingInstructor().click()
        self.getPendingInstructorApproveButton().click()
