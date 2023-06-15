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
        self.driver.get('https://usis.bracu.ac.bd/academia/')

    def test_usis(self):
        main_page = page.MainPage(self.driver)
        main_page.search_email_input = "sadique.tahmid.7@gmail.com"
        main_page.search_password_input = ""
        main_page.click_login_btn()
        main_page.click_std_drp_down()
        main_page.click_grade_sheet_btn()
        main_page.click_grade_sheet_print()
        main_page.click_advising_drp_down()
        main_page.click_seat_status_btn()
        main_page.click_advising_year_select()
        main_page.click_session_select()
        main_page.search_box_field = 'cse470'
        main_page.click_search_btn() # it will take 20 sec
        time.sleep(1)
        search_results_page = page.SearchResultsPage(self.driver) # create obj of SearchResultsPage() class from page.py 
        assert search_results_page.find_cse470_text(), "CSE470"
        
    def tearDown(self): # close the website
        pass

if __name__ == "__main__": # 
    unittest.main() # run all the unit test that we defined
