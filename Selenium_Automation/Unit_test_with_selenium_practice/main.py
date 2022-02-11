# write the tests we will perform
import unittest
from unittest.main import main
from selenium import webdriver
import page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


PATH = 'C:\Program Files (x86)\chromedriver.exe'

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.python.org/')


    def test_search_in_python_org(self): # if it starts with 'test_', it will automatically run 
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""
        
        main_page = page.MainPage(self.driver) # create obj of MainPage class from page.py file
        assert main_page.is_title_matches(), "python.org title doesn't match." # right side is true then it pass
        main_page.search_text_element = "pycon" # send "pycon" to SearchTextElement() in page.py, then set value to BasePageElement in element.py
        main_page.click_go_button() # go to page.py, then locators.py 
        search_results_page = page.SearchResultsPage(self.driver) # send the value to the element.py file
        assert search_results_page.is_results_found(), "No results found." # Verifies that the results page has that sentence
        
        
    def test_my_example(self): # the program will run, how many test_**** i write
        main_page = page.MainPage(self.driver) # create obj of MainPage() class from page.py file
        assert main_page.is_title_matches(), "python.org title doesn't match." # right side is true then it pass
        main_page.search_text_element = "pycon" 
        main_page.click_go_button() # go to page.py, then locators.py
        main_page.go_to_next_page() # go to the next link from that page
        search_results_page = page.SearchResultsPage(self.driver) # create obj of SearchResultsPage() class from page.py 
        assert search_results_page.my_own_result_found(), "PSF PyCon Trademark Usage Policys" # fail here
        
    def tearDown(self): # close the website
        pass

if __name__ == "__main__": # 
    unittest.main() # run all the unit test that we defined