# all the attributes by which we grab the element

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit') # it is constant so, BLOCK LETTER !!
    NEXT_PAGE = (By.XPATH, "//a[text()='PSF PyCon Trademark Usage Policy']") # element of the first link

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""
    pass