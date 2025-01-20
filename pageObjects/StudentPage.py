from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class StudentPage:
    def __init__(self, driver):
        self.driver = driver
        self.become_instructor_nav = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[3]/a")
        self.become_instructor_button = (By.XPATH, "/html/body/div[2]/section[1]/div/div[2]/div/button")
        self.first_name_input_become_instructor = (By.XPATH, "//*[@id='first_name']")
        self.instructor_type_input_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[2]/div/select")
        self.last_name_input_become_instructor = (By.XPATH, "//*[@id='last_name']")
        self.phone_number_input_become_instructor = (By.XPATH, "//*[@id='phone_number']")
        self.address_input_become_instructor = (By.XPATH, "//*[@id='address']")
        self.cv_input_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[7]/div/div/input")
        self.bio_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[8]/div/textarea")
        self.submit_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[2]/button")
        self.profile = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[2]/a")
        self.logout_button = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[7]/div/ul[3]/li[2]/a")
        self.professional_title_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[3]/div/select")
        self.forum_button = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[2]/a")
        self.ask_question_button = (By.XPATH, "//a[@class='theme-button1']")
        self.submit_question_button = (By.XPATH, "//button[@type='submit']")
        self.topic_title_input = (By.XPATH, "//input[@placeholder='Enter your topic title']")
        self.category_input = (By.XPATH, "//select[@id='inputState']")
        self.question_input = (By.XPATH, "//div[@role='textbox']//p")
        #forum page
        self.forum_category_title = (By.XPATH, "//*[@id='title']")
        self.forum_category_subtitle = (By.XPATH, "//*[@id='subtitle']")
        self.forum_category_status = (By.XPATH, "//*[@id='status']")

    def getBecomeInstructorButton(self):
        return self.driver.find_element(*self.become_instructor_button)
    
    def getBecomeInstructorNav(self):
        return self.driver.find_element(*self.become_instructor_nav)
    
    def getFirstNameInputBecomeInstructor(self):
        return self.driver.find_element(*self.first_name_input_become_instructor)

    def getInstructorTypeInputBecomeInstructor(self):
        return self.driver.find_element(*self.instructor_type_input_become_instructor)
    
    def getCvInputBecomeInstructor(self):
        return self.driver.find_element(*self.cv_input_become_instructor)
    
    def getLastNameInputBecomeInstructor(self):
        return self.driver.find_element(*self.last_name_input_become_instructor)
    
    def getPhoneNumberInputBecomeInstructor(self):
        return self.driver.find_element(*self.phone_number_input_become_instructor)
    
    def getAddressInputBecomeInstructor(self):
        return self.driver.find_element(*self.address_input_become_instructor)
    
    def cvUpload(self, path):
        self.driver.find_element(*self.cv_input_become_instructor).send_keys(path)
        
    def getBioBecomeInstructor(self):
        return self.driver.find_element(*self.bio_become_instructor)
    
    def getSubmitBecomeInstructor(self):
        return self.driver.find_element(*self.submit_become_instructor)
    
    def getProfile(self):
        return self.driver.find_element(*self.profile)
    
    def getLogoutButton(self):
        return self.driver.find_element(*self.logout_button)
    
    def getForumButton(self):
        return self.driver.find_element(*self.forum_button)
    
    def getAskQuestionButton(self):
        return self.driver.find_element(*self.ask_question_button)
    
    def getSubmitQuestionButton(self):
        return self.driver.find_element(*self.submit_question_button)
    
    def getTopicTitleInput(self):
        return self.driver.find_element(*self.topic_title_input)
    
    def getCategoryInput(self):
        return self.driver.find_element(*self.category_input)
    
    def getQuestionInput(self):
        return self.driver.find_element(*self.question_input)

    def doLogout(self):
        profile_element = self.getProfile()
        actions = ActionChains(self.driver)
        actions.move_to_element(profile_element).perform() 
        logout_button = self.getLogoutButton()
        logout_button.click()
        
    def getProfessionalTitleBecomeInstructor(self):
        return self.driver.find_element(*self.professional_title_become_instructor)

    def doRequestInstructor(self, first_name, last_name, phone_number, address, cv, bio, title):
        self.getBecomeInstructorNav().click()
        self.getBecomeInstructorButton().click()
        self.getFirstNameInputBecomeInstructor().send_keys(first_name)
        self.getInstructorTypeInputBecomeInstructor().click()
        self.getLastNameInputBecomeInstructor().send_keys(last_name)
        self.getPhoneNumberInputBecomeInstructor().send_keys(phone_number)
        self.getAddressInputBecomeInstructor().send_keys(address)
        self.cvUpload(cv)
        self.getProfessionalTitleBecomeInstructor().send_keys(title)
        self.getBioBecomeInstructor().send_keys(bio)
        self.getSubmitBecomeInstructor().click()
    
    def doCreateForumQuestion(self, topic_title, category, question):
        self.getForumButton().click()
        self.getAskQuestionButton().click()
        self.getTopicTitleInput().send_keys(topic_title)
        self.getCategoryInput().send_keys(category)
        self.getQuestionInput().send_keys(question)
        self.getSubmitQuestionButton().click()