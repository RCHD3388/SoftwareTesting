from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class StudentPage:
    def __init__(self, driver):
        self.driver = driver
        self.becomeInstructorNav = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[3]/a")
        self.becomeInstructorButton = (By.XPATH, "/html/body/div[2]/section[1]/div/div[2]/div/button")
        self.firstNameInputBecomeInstructor = (By.XPATH, "//*[@id='first_name']")
        self.instructorTypeInputBecomeInstructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[2]/div/select")
        self.lastNameInputBecomeInstructor = (By.XPATH, "//*[@id='last_name']")
        self.phoneNumberInputBecomeInstructor = (By.XPATH, "//*[@id='phone_number']")
        self.addressInputBecomeInstructor = (By.XPATH, "//*[@id='address']")
        self.cvInputBecomeInstructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[7]/div/div/input")
        self.bioBecomeInstructor = (By.XPATH, "//*[@id='beco    meAnInstructor']/div/div/form/div[1]/div[8]/div/textarea")
        self.submitBecomeInstructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[2]/button")
        self.profile = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[2]/a")
        self.logoutButton = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[7]/div/ul[3]/li[2]/a")
        self.professionalTitleBecomeInstructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[3]/div/select")
        self.forumButton = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[2]/a")
        self.askQuestionButton = (By.XPATH, "//a[@class='theme-button1']")
        self.submitQuestionButton = (By.XPATH, "//button[@type='submit']")
        self.topicTitleInput = (By.XPATH, "//*input[@placeholder='Enter your topic title']")
        self.categoryInput = (By.XPATH, "//*[@id='inputState']")
        self.questionInput = (By.XPATH, "//*div[@role='textbox']//p")
    def getBecomeInstructorButton(self):
        return self.driver.find_element(*self.becomeInstructorButton)
    
    def getBecomeInstructorNav(self):
        return self.driver.find_element(*self.becomeInstructorNav)
    
    def getFirstNameInputBecomeInstructor(self):
        return self.driver.find_element(*self.firstNameInputBecomeInstructor)
    def getInstructorTypeInputBecomeInstructor(self):
        return self.driver.find_element(*self.instructorTypeInputBecomeInstructor)
    
    def getcvInputBecomeInstructor(self):
        return self.driver.find_element(*self.cvInputBecomeInstructor)
    
    def getLastNameInputBecomeInstructor(self):
        return self.driver.find_element(*self.lastNameInputBecomeInstructor)
    
    def getPhoneNumberInputBecomeInstructor(self):
        return self.driver.find_element(*self.phoneNumberInputBecomeInstructor)
    
    def getAddressInputBecomeInstructor(self):
        return self.driver.find_element(*self.addressInputBecomeInstructor)
    
    def cvUpload(self, path):
        self.driver.find_element(*self.cvInputBecomeInstructor).send_keys(path)
        
    def getBioBecomeInstructor(self):
        return self.driver.find_element(*self.bioBecomeInstructor)
    
    def getSubmitBecomeInstructor(self):
        return self.driver.find_element(*self.submitBecomeInstructor)
    
    def getProfile(self):
        return self.driver.find_element(*self.profile)
    
    def getLogoutButton(self):
        return self.driver.find_element(*self.logoutButton)
    
    def getForumButton(self):
        return self.driver.find_element(*self.forumButton)
    
    def getAskQuestionButton(self):
        return self.driver.find_element(*self.askQuestionButton)
    
    def getSubmitQuestionButton(self):
        return self.driver.find_element(*self.submitQuestionButton)
    
    def getTopicTitleInput(self):
        return self.driver.find_element(*self.topicTitleInput)
    
    def getCategoryInput(self):
        return self.driver.find_element(*self.categoryInput)
    
    def getQuestionInput(self):
        return self.driver.find_element(*self.questionInput)


    def doLogout(self):
        profile_element = self.getProfile()  # Assuming this returns a WebElement for the profile
        actions = ActionChains(self.driver)  # Initialize ActionChains with the WebDriver instance
        actions.move_to_element(profile_element).perform() 

        logout_button = self.getLogoutButton()
        logout_button.click()
        
    def getProfessionalTitleBecomeInstructor(self):
        return self.driver.find_element(*self.professionalTitleBecomeInstructor)
    def doRequestInstructor(self, firstName, lastName, phoneNumber, address, cv, bio,title):
        self.getBecomeInstructorNav().click()
        self.getBecomeInstructorButton().click()
        self.getFirstNameInputBecomeInstructor().send_keys(firstName)
        self.getInstructorTypeInputBecomeInstructor().click()
        self.getLastNameInputBecomeInstructor().send_keys(lastName)
        self.getPhoneNumberInputBecomeInstructor().send_keys(phoneNumber)
        self.getAddressInputBecomeInstructor().send_keys(address)
        self.cvUpload(cv)
        self.getProfessionalTitleBecomeInstructor().send_keys(title)
        self.getBioBecomeInstructor().send_keys(bio)
        self.getSubmitBecomeInstructor().click()
        