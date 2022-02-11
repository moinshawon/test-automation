# all the kinds of test will be deploped here

from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.support.ui import Select
import time


class SearchEmailInput(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'username'
    
class SearchPasswordInput(BasePageElement):
    locator = 'password'

class SearchBoxField(BasePageElement):
    locator = 'queryCourseStatus'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver # contructor assigning


class MainPage(BasePage): # inherite from BasePage coz I dont want to innitial driver every time
    """Home page action methods come here. I.e. Python.org"""
    # search_text_element = SearchTextElement() 
    search_email_input = SearchEmailInput() # Discriptor: Declares a variable that will contain the retrieved text
    search_password_input = SearchPasswordInput()
    search_box_field = SearchBoxField()

    def click_login_btn(self):
        login_btn = self.driver.find_element(*MainPageLocators.LOGIN_BTN) # unpack
        login_btn.click() # click the first link from the page
        
    def click_std_drp_down(self):
        self.driver.implicitly_wait(5) # wait 5 sec before doing next task
        drp_down_std = self.driver.find_element(*MainPageLocators.DROP_DOWN_STD) # unpack
        drp_down_std.click() # click the first link from the page

    def click_grade_sheet_btn(self):
        self.driver.implicitly_wait(5)
        grade_sheet_btn = self.driver.find_element(*MainPageLocators.GRADE_SHEET_BTN) # unpack
        grade_sheet_btn.click() # click the first link from the page
        #self.driver.execute_script("arguments[0].click()", grade_sheet_btn)  # it will also work
        
    def click_grade_sheet_print(self):
        self.driver.implicitly_wait(5)
        grade_sheet_print = self.driver.find_element(*MainPageLocators.GRADE_SHEET_PRINT) # unpack
        grade_sheet_print.click() # click the first link from the page
        
    def click_advising_drp_down(self):
        self.driver.implicitly_wait(5)
        advising_drp_down = self.driver.find_element(*MainPageLocators.DRP_ADVISING_ELEMENT) # unpack
        advising_drp_down.click() # click the first link from the page
        
    def click_seat_status_btn(self):
        self.driver.implicitly_wait(5)
        seat_status_btn = self.driver.find_element(*MainPageLocators.SEAT_STATUS_BTN) # unpack
        seat_status_btn.click() # click the first link from the page
        #self.driver.execute_script("arguments[0].click()", seat_status_btn) # it will also work
        
    def click_advising_year_select(self):
        self.driver.implicitly_wait(5)
        advising_year_element = self.driver.find_element(*MainPageLocators.ADVISING_YEAR_ELEMENT) # unpack
        advising_year_drp_down = Select(advising_year_element)
        advising_year_drp_down.select_by_visible_text("2021")
        
    def click_session_select(self):
        self.driver.implicitly_wait(5)
        session_element = self.driver.find_element(*MainPageLocators.SESSION_ELEMENT) # unpack
        session_drp_down = Select(session_element)
        session_drp_down.select_by_visible_text("Summer 2021")

    def click_search_btn(self):
        self.driver.implicitly_wait(5)
        search_btn = self.driver.find_element(*MainPageLocators.SEARCH_BTN) # unpack
        time.sleep(30)
        for i in range(300): # using for loop bcz the website takes time
            search_btn.click()

class SearchResultsPage(BasePage): # inherite from BasePage coz I dont want to innitial driver every time
    """Search results page action methods come here"""

    def find_cse470_text(self):
        return "CSE470" in self.driver.page_source  
