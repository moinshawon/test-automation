from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\Program Files (x86)\chromedriver.exe'


driver = webdriver.Chrome(PATH)
driver.get('https://usis.bracu.ac.bd/academia/')

try:
    
# --------- give you valid usis email & password ---------
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"username"))
    )
    email_input.click()
    email_input.clear()          # clear the input box first
    email_input.send_keys("sadique.tahmid.7@gmail.com") # use your email
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"password"))
    )
    password_input.click()
    password_input.clear()                  
    password_input.send_keys("MetalGear13")  # use your password
    password_input.send_keys(Keys.RETURN)    # hit enter
    time.sleep(2)
    
# --------- go to the student section then grade sheet and download it ---------
    
    drp_std_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[text()='Student']"))
    )
    drp_std_element.click() 
    time.sleep(1)
    
    # go to grade sheet page
    grade_sheet = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[text()='Student Grade Sheet']"))
    )
    # as it is a dynamic page we need to select by JS
    driver.execute_script("arguments[0].click()", grade_sheet)
    # driver.execute_script("arguments[0].style.display = 'none';", grade_sheet)
    
    # find the print button from grade sheet page
    grade_sheet_print = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"print-button"))
    )  
    grade_sheet_print.click()
    time.sleep(1)
    
    
# --------- go to advising page and click seat status. Find a course ---------
# ------------------ by selecting year and session --------------

    # advising page element
    drp_advising_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[text()='Advising']"))
    ) 
    drp_advising_element.click()
    time.sleep(1)
    
    # going to seat status page
    seat_status = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[text()='Seat Status']"))
    )
    driver.execute_script("arguments[0].click()", seat_status)
    time.sleep(1)
    
    # grabing the Adving year box
    advising_year_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"academiaYear"))
    )
    # using 'Select' class from selenium for drop down menu
    # the HTML tag of the web page also select class
    # here, creating an object of it then we can work with it's methods
    advising_year_drop_down = Select(advising_year_element)
    
    # select the desire acedamic year
    advising_year_drop_down.select_by_visible_text("2021")
    
    # select by index: 2021 is in index number 2
    #advising_year_drop_down.select_by_index("2")
    
    # option always contains value attribute
    #advising_year_drop_down.select_by_value("279286")
    time.sleep(1)
    
    
    # same way selecting session from drop down menu
    session_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"academiaSession"))
    )
    session_drop_down = Select(session_element)
    session_drop_down.select_by_visible_text("Summer 2021")
    time.sleep(1)
    
    # find HTML tag input and any attribute (name preffered) 
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "queryCourseStatus"))
    ) 
    search_box.clear()  
    search_box.send_keys("cse422")
    
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search-button"))
    ) 
    time.sleep(20)   # coz BracU USIS is soOOOoo slow !!!!!!!!
    for i in range(300):
        search_button.click()
    
except: # if the text did not find then, pass it
    pass