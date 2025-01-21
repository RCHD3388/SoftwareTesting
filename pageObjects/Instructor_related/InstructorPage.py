from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
class InstructorPage:

    def __init__(self, driver):
        self.driver = driver

    def getInsField_insert(self, attr, placeholder, value):
        try:
            element = self.driver.find_element(By.XPATH, f"//input[@{attr}='{placeholder}']")
            element.send_keys(value)
            return element
        except Exception as e:
            print(f"Error finding or interacting with the input field: {e}")
            return None
    def getButton(self, type):
        return self.find_element(By.XPATH, f"//button[@type='{type}']")
    
    def open_instructor_panel(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Instructor Panel']").click()
    def open_upload_course(self):
        # Temukan elemen dengan XPath
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Live Class']")
        element2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Upload Course']")
        # Gulir halaman ke elemen dan klik menggunakan ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()  
        element2.click()
    
    def fill_course_input(self):
        element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Live Class']")
        course_subtitle = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Course subtitle in 1000 characters']")
    
        # Scroll ke elemen menggunakan ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    
        # Pilih opsi pada dropdown
        course_type = self.driver.find_element(By.XPATH, "//select[@id='course_type']")
        select = Select(course_type)
        select.select_by_visible_text("General")
    
        # Isi judul dan subtitle kursus
        self.getInsField_insert("placeholder", "Course subtitle in 1000 characters", "course subtitle")
        #pointname
        self.getInsField_insert("id", "name", "programming")
        #description 
        description = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Course description']")
        description.send_keys("ini adalah description  untuk course yang akan di upload")
        #meta title
      

        self.getInsField_insert("placeholder", "Meta Title", "programming")
        #meta description
        self.driver.find_element(By.XPATH, "//textarea[@id='exampleFormControlTextarea1']").send_keys("ini adalah meta description  untuk course yang akan di upload")
        #meta keywords
        self.getInsField_insert("placeholder", "Type meta keywords (comma separated)", "programming,OOP")
        #image
        file_path = os.path.abspath("TestData\\assets\\images\\istts.jpg")
        file_path =file_path.replace("\\", "\\\\")
        self.getInsField_insert("id", "og_image", file_path)
        #save and continue

    
        
        
        
        

   
  
    


    



