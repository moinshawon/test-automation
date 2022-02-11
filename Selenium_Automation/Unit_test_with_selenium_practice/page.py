# all the kinds of test will be deploped here

from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.support.ui import Select
import time

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'q'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver # contructor assigning


class MainPage(BasePage): # inherite from BasePage coz I dont want to innitial driver every time
    """Home page action methods come here. I.e. Python.org"""
    search_text_element = SearchTextElement() # Discriptor: Declares a variable that will contain the retrieved text
    
    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title # return true or false

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
    
    def go_to_next_page(self):
        next_page_click = self.driver.find_element(*MainPageLocators.NEXT_PAGE) # unpack
        next_page_click.click() # click the first link from the page


class SearchResultsPage(BasePage): # inherite from BasePage coz I dont want to innitial driver every time
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
    
    def my_own_result_found(self):
        return "PSF PyCon Trademark Usage Policys" in self.driver.page_source # fail here

