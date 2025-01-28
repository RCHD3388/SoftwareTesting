from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
class StudentPage:
    def __init__(self, driver):
        self.driver = driver
        self.become_instructor_nav = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[3]/a")
        self.become_instructor_button = (By.XPATH, "/html/body/div[2]/section[1]/div/div[2]/div/button")#ABSOUlute masihan
        self.first_name_input_become_instructor = (By.XPATH, "//*[@id='first_name']")
        self.instructor_type_input_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[2]/div/select")
        self.last_name_input_become_instructor = (By.XPATH, "//*[@id='last_name']")
        self.phone_number_input_become_instructor = (By.XPATH, "//*[@id='phone_number']")
        self.address_input_become_instructor = (By.XPATH, "//*[@id='address']")
        self.cv_input_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[7]/div/div/input")
        self.bio_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[8]/div/textarea")
        self.submit_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[2]/button")
        self.profile = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[7]/a/img")
        self.logout_button = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[7]/div/ul[3]/li[2]/a")
        self.professional_title_become_instructor = (By.XPATH, "//*[@id='becomeAnInstructor']/div/div/form/div[1]/div[3]/div/select")
        #forum page
        self.forum_category_logo = (By.XPATH, "//*[@id='logo']")
        self.forum_category_title = (By.XPATH, "//*[@id='title']")
        self.forum_category_subtitle = (By.XPATH, "//*[@id='subtitle']")
        self.forum_category_status = (By.XPATH, "//*[@id='status']")
        self.forum_button = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[2]/a")
        self.ask_question_button = (By.XPATH, "//a[@class='theme-button1']")
        self.submit_question_button = (By.XPATH, "//button[normalize-space()='Publish Question']")
        self.topic_title_input = (By.XPATH, "//input[@placeholder='Enter your topic title']")
        self.category_input = (By.XPATH, "//select[@id='inputState']")
        self.question_input = (By.XPATH, "//div[@role='textbox']//p")
        self.forum_toast = (By.XPATH, "//*[@id='toast-container']/div/div[2]")
        #blogs page
        self.pages_dropdown = (By.XPATH, "//*[@id='pagesDropdown']")
        self.blogs_button = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[1]/ul/li[1]/a")
        self.blogs_dropdown = (By.XPATH, "//a[contains(@class,'dropdown-item')][normalize-space()='Blogs']")
        self.blog = "//h3[@class='card-title blog-title']//a[contains(text(),'{}')]"  # Dynamic xpath with placeholder for title
        self.blog_reply_input = (By.XPATH, "//*[@id='cus_comment']")
        self.blog_reply_submit = (By.XPATH, "//button[normalize-space()='Submit Now']")
        self.blog_reply_toast_message = (By.CLASS_NAME, 'toast')
        #chats
        self.chats_button = (By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[7]/div/ul[1]/li[3]/a")
        self.chat_xpath = "//span[contains(@class, 'user-name') and contains(text(), '{}')]/following-sibling::span[contains(@class, 'course-title')]//span[@class='title' and contains(text(), '{}')]"
        self.chat_reply_input = (By.XPATH, "//*[@id='chat-message']")
        self.chat_reply_submit = (By.XPATH, "//*[@id='chat-send']/span")
        self.latest_chat = (By.XPATH, "//*[@id='messages-container']/div[1]/h6")
        #discussions
        self.my_learning_button = (By.XPATH, "//a[normalize-space()='My Learning']")
        self.course_view_button = "//tbody/tr[{}]/td[7]/a[1]"  # Dynamic xpath with placeholder for row number
        self.discussions_button = (By.XPATH, "//*[@id='Discussion-tab']")
        self.discussions_create_button = (By.XPATH, "//*[@id='Discussion']/div/div/div/div[1]/div[2]/div[1]/button")
        self.discussions_content_input = (By.XPATH, "//*[@id='mytextarea']")
        self.discussions_submit_button = (By.XPATH, "//*[@id='Discussion']/div/div/div/div[1]/div[2]/div[2]/form/button")
        self.discussions_final_content = '//*[@id="Discussion"]/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/p/text()'        
        # //*[@id="Discussion"]/div/div/div/div[{}]/div/div/div[1]/div[2]/div[1]/p
        #reviews
        self.reviews_button = (By.XPATH, "//*[@id='Review-tab']")
        self.reviews_write_button = (By.XPATH, "//button[normalize-space()='Write a review']")
        self.reviews_feedback_input = (By.XPATH, "//*[@id='exampleFormControlTextarea1']")
        self.reviews_submit_button = (By.XPATH, "//*[@id='writeReviewModal']/div/div/div[3]/button[2]")
        self.reviews_star_template = "//*[@id='writeReviewModal']/div/div/div[2]/form/div[1]/div/div/label[{}]"
        self.reviews_toast_message = (By.XPATH, "//*[@id='toast-container']/div/div[2]")
    #become instructor  
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
    
    #profile
    def getProfile(self):
        return self.driver.find_element(*self.profile)
    
    def getLogoutButton(self):
        return self.driver.find_element(*self.logout_button)
    #forum
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
        
    def getProfessionalTitleBecomeInstructor(self):
        return self.driver.find_element(*self.professional_title_become_instructor)
    def getForumToastMessage(self):
        return self.driver.find_element(*self.forum_toast).text
    #blogs
    def getBlogsDropdown(self):
        return self.driver.find_element(*self.pages_dropdown)
    
    def getBlogsButton(self):
        return self.driver.find_element(*self.blogs_button)
    
    def getBlog(self, title):
        blog_xpath = self.blog.format(title)  # Format the xpath with the provided title
        return self.driver.find_element(By.XPATH, blog_xpath)
    
    def getBlogReplyInput(self):
        return self.driver.find_element(*self.blog_reply_input)
    
    def getBlogReplySubmit(self):
        return self.driver.find_element(*self.blog_reply_submit)
    
    def getBlogReplyToastMessage(self):
        return self.driver.find_element(*self.blog_reply_toast_message).text
    
    #chats  
    def getChatReplyInput(self):
        return self.driver.find_element(*self.chat_reply_input)
    
    def getChatReplySubmit(self):
        return self.driver.find_element(*self.chat_reply_submit)
    
    def getChatsButton(self):
        return self.driver.find_element(*self.chats_button)
    
    def getChat(self, sender, course_name):
        return (By.XPATH, f"//span[contains(@class,'user-name') and contains(text(), '{sender}')]/following-sibling::span[contains(@class, 'course-title')]//span[@class='title' and contains(text(), '{course_name}')]")
    def getLatestChat(self):
        return self.driver.find_element(*self.latest_chat).text
        
    #discussions
    def getMyLearningButton(self):
        return self.driver.find_element(*self.my_learning_button)
    
    def getCourseViewButton(self, row=1):
        course_xpath = (By.XPATH, self.course_view_button.format(row))
        return self.driver.find_element(*course_xpath)
    
    def getDiscussionsButton(self):
        return self.driver.find_element(*self.discussions_button)
    
    def getDiscussionsCreateButton(self):
        return self.driver.find_element(*self.discussions_create_button)
    
    def getDiscussionsContentInput(self):
        return self.driver.find_element(*self.discussions_content_input)
    
    def getDiscussionsSubmitButton(self):
        return self.driver.find_element(*self.discussions_submit_button)
    
    def getDiscussionsFinalContent(self, index):
        wait = WebDriverWait(self.driver, 10)
        discussions_button = wait.until(EC.presence_of_element_located(self.discussions_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", discussions_button)
        time.sleep(2)
        discussions_button = wait.until(EC.element_to_be_clickable(self.discussions_button))
        discussions_button.click()
        time.sleep(2)
        discussions_final_content_xpath = '//*[@id="Discussion"]/div/div/div/div[2]/div/div/div[{}]/div[2]/div[1]/p'.format(index)

        try:
            print(f"Looking for element with XPath: {discussions_final_content_xpath}")
            wait.until(EC.presence_of_element_located((By.XPATH, discussions_final_content_xpath)))
            discussions_element = self.driver.find_element(By.XPATH, discussions_final_content_xpath)
            
            # Check if the element is displayed
            if discussions_element.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", discussions_element)
                return discussions_element.text
            else:
                print(f"Element found but not displayed: {discussions_final_content_xpath}")
                return None
        except TimeoutException:
            print(f"Element not found for index {index}: {discussions_final_content_xpath}")
            return None
    
    #reviews
    def getReviewsButton(self):
        return self.driver.find_element(*self.reviews_button)
    
    def getReviewsWriteButton(self):
        return self.driver.find_element(*self.reviews_write_button)
    
    def getReviewsFeedbackInput(self):
        return self.driver.find_element(*self.reviews_feedback_input)
    
    def getReviewsSubmitButton(self):
        return self.driver.find_element(*self.reviews_submit_button)
    
    def getReviewsToastMessage(self):
        return self.driver.find_element(*self.reviews_toast_message).text
    
    def getReviewsStar(self, rating=4):
        """
        Get the star rating element for the specified rating (1-5)
        :param rating: Rating value between 1 and 5
        :return: WebElement for the specified star rating
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        star_locator = (By.XPATH, self.reviews_star_template.format(rating))
        return self.driver.find_element(*star_locator)
    
    def doLogout(self):
        # Wait for the toast notification to disappear
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, 'toast'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.profile)
        )
        self.getProfile().click()
        time.sleep(2)
        self.getLogoutButton().click()
        

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
        time.sleep(2)

    def goToBlogs(self,content,title):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.pages_dropdown)).click(self.driver.find_element(*self.blogs_button)).perform()
        time.sleep(2)
        
        # Wait for blog to be present and scroll to it
        wait = WebDriverWait(self.driver, 10)
        blog_element = wait.until(EC.presence_of_element_located((By.XPATH, self.blog.format(title))))
        
        # Scroll the blog into view
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", blog_element)
        time.sleep(2)  # Wait for scroll to complete

        # Wait for element to be clickable after scroll
        blog_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.blog.format(title))))
        blog_element.click()
        time.sleep(2)  # Wait for page to load after click
        
        # Wait for reply input to be present and scroll to it
        reply_input = wait.until(EC.presence_of_element_located(self.blog_reply_input))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", reply_input)
        time.sleep(2)
        
        # Wait for input to be clickable and enter text
        reply_input = wait.until(EC.element_to_be_clickable(self.blog_reply_input))
        reply_input.clear()
        reply_input.send_keys(content)
        
        # Wait for submit button and scroll if needed
        submit_button = wait.until(EC.presence_of_element_located(self.blog_reply_submit))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(2)
        
        # Try to click using JavaScript if normal click fails
        try:
            submit_button = wait.until(EC.element_to_be_clickable(self.blog_reply_submit))
            submit_button.click()
        except:
            # Fallback to JavaScript click
            self.driver.execute_script("arguments[0].click();", submit_button)
        
        time.sleep(2)
        
    def goToChats(self, content, username="hehe", course="Intro"):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.profile)).click(self.driver.find_element(*self.chats_button)).perform()
        time.sleep(2)

        # Use the parameterized getChat method
        chat_element = self.driver.find_element(*self.getChat(username, course))
        chat_element.click()
        time.sleep(3)  # Wait for chat to load

        # Initialize WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        
        # Function to scroll and find element
        def scroll_to_element():
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)  # Wait for page to load
                
                try:
                    chat_input = self.driver.find_element(*self.chat_reply_input)
                    return chat_input
                except:
                    # Calculate new scroll height
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        raise Exception("Chat input not found after scrolling to bottom")
                    last_height = new_height
        
        try:
            # First try to find element without scrolling
            chat_input = wait.until(EC.presence_of_element_located(self.chat_reply_input))
        except:
            # If not found, scroll until found
            chat_input = scroll_to_element()
            
        chat_input.send_keys(content)

        # Wait for the submit button to be clickable
        submit_button = wait.until(EC.element_to_be_clickable(self.chat_reply_submit))
        submit_button.click()
    
    def goToDiscussions(self, content, row=1):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.profile)).click(self.driver.find_element(*self.my_learning_button)).perform()
        time.sleep(2)
        
        # Wait and scroll for course view button
        wait = WebDriverWait(self.driver, 10)
        course_button = wait.until(EC.presence_of_element_located((By.XPATH, self.course_view_button.format(row))))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", course_button)
        time.sleep(2)
        course_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.course_view_button.format(row))))
        course_button.click()
        time.sleep(2)
        
        # Wait and scroll for discussions button
        discussions_button = wait.until(EC.presence_of_element_located(self.discussions_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", discussions_button)
        time.sleep(2)
        discussions_button = wait.until(EC.element_to_be_clickable(self.discussions_button))
        discussions_button.click()
        time.sleep(2)
        
        # Wait and scroll for create button
        create_button = wait.until(EC.presence_of_element_located(self.discussions_create_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", create_button)
        time.sleep(2)
        create_button = wait.until(EC.element_to_be_clickable(self.discussions_create_button))
        create_button.click()
        
        # Wait and scroll for content input
        content_input = wait.until(EC.presence_of_element_located(self.discussions_content_input))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", content_input)
        time.sleep(2)
        content_input = wait.until(EC.element_to_be_clickable(self.discussions_content_input))
        content_input.clear()
        content_input.send_keys(content)
        
        # Wait and scroll for submit button
        submit_button = wait.until(EC.presence_of_element_located(self.discussions_submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(2)
        submit_button = wait.until(EC.element_to_be_clickable(self.discussions_submit_button))
        submit_button.click()
        
        time.sleep(2)
    def scrollToXY(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, window.innerHeight * {y} /100);")

    def goToChats(self, content, username="hehe", course="Intro"):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.profile)).click(self.driver.find_element(*self.chats_button)).perform()
        time.sleep(2)

        # Use the parameterized getChat method
        chat_element = self.driver.find_element(*self.getChat(username, course))
        chat_element.click()
        time.sleep(3)  # Wait for chat to load

        # Initialize WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        
        try:
            # First try to find element without scrolling
            chat_input = wait.until(EC.presence_of_element_located(self.chat_reply_input))
        except:
            # If not found, scroll by specified amount
            self.scrollToXY(0, 60)
            time.sleep(1)  # Wait for scroll to complete
            chat_input = wait.until(EC.presence_of_element_located(self.chat_reply_input))
            
        chat_input.send_keys(content)

        try:
            # Try to find and click submit button
            submit_button = wait.until(EC.element_to_be_clickable(self.chat_reply_submit))
            submit_button.click()
        except:
            # If not clickable, scroll again and retry
            self.scrollToXY(0, 60)
            time.sleep(1)
            submit_button = wait.until(EC.element_to_be_clickable(self.chat_reply_submit))
            submit_button.click()
        
    def doReview(self, row,star,feedback="test"):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.profile)).click(self.driver.find_element(*self.my_learning_button)).perform()
        time.sleep(2)
        
        # Wait and scroll for course view button
        wait = WebDriverWait(self.driver, 10)
        course_button = wait.until(EC.presence_of_element_located((By.XPATH, self.course_view_button.format(row))))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", course_button)
        time.sleep(2)
        course_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.course_view_button.format(row))))
        course_button.click()
        time.sleep(2)
        
        # Wait and scroll for reviews button
        reviews_button = wait.until(EC.presence_of_element_located(self.reviews_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", reviews_button)
        time.sleep(2)
        reviews_button = wait.until(EC.element_to_be_clickable(self.reviews_button))
        reviews_button.click()
        time.sleep(2)
        
        # Wait and scroll for write review button
        write_review_button = wait.until(EC.presence_of_element_located(self.reviews_write_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", write_review_button)
        time.sleep(2)
        write_review_button = wait.until(EC.element_to_be_clickable(self.reviews_write_button))
        write_review_button.click()
        time.sleep(2)
        
        # Wait and scroll for rating input
        self.getReviewsStar(star).click()
        time.sleep(2)
        
        # Wait for feedback input field and clear any existing text
        feedback_input = wait.until(EC.presence_of_element_located(self.reviews_feedback_input))
        feedback_input.clear()  # Clear any existing text
        feedback_input.send_keys(feedback)  # Type the new feedback
        time.sleep(1)  # Short pause to ensure text is entered
        
        # Wait and scroll for submit button
        submit_button = wait.until(EC.presence_of_element_located(self.reviews_submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_button)
        time.sleep(2)
        submit_button = wait.until(EC.element_to_be_clickable(self.reviews_submit_button))
        submit_button.click()
        time.sleep(2)
        
