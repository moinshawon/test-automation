# all the attributes by which we grab the element

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    LOGIN_BTN = (By.ID, "ctl00_leftColumn_ctl00_btnLogin")
    DROP_DOWN_STD = (By.XPATH,"//a[text()='Student']")
    GRADE_SHEET_BTN = (By.XPATH,"//a[text()='Student Grade Sheet']")
    GRADE_SHEET_PRINT = (By.ID,"print-button")
    DRP_ADVISING_ELEMENT = (By.XPATH,"//a[text()='Advising']")
    SEAT_STATUS_BTN = (By.XPATH,"//a[text()='Seat Status']")
    ADVISING_YEAR_ELEMENT = (By.ID,"academiaYear")
    SESSION_ELEMENT = (By.ID,"academiaSession")
    SEARCH_BTN = (By.ID, "search-button")
    
class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""
    pass