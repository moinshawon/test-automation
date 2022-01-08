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

driver.get('https://www.airbnb.com/')

try:
    # -- clicking in France, Paris !! 🇫🇷
    
    paris = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='_1byskwn']//div[contains(text(),'Paris')]//parent::div[@class='_1hsn6c7']//parent::a[@class]"))
    )
    paris.click()

    # -- now click Dijon and go to next page: Dijon
    
    dijon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Dijon 262 km']"))
    ) 
    # search for the text in the page. wait 10 sec until find that
    # it has to be clickable text/button. usually 'a' tag has this.
    # now find the text again and go to next page
    dijon.click()
    time.sleep(2)
    
    # -- click login button
    
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@class='_t26s9ye' and @action='/login']//input[@class='_1r6oup6']"))
    ) 
    login.click()
    
    # -- now fill up and enter phone number
    
    phone = driver.find_element_by_xpath("//input[@id='phoneNumber']") # find HTML tag input and attribute name = s
    phone.clear()   # clear the input box first
    phone.send_keys("12345")  # fill the search box 'test'
    # phone.send_keys(Keys.RETURN) # hit enter
    
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='_utuv3hg']"))
    ) 
    time.sleep(2) # just to check what is going on the web page 
    button.click()
    time.sleep(2)
    
#     select = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//parent::select[@id='children']//option[@value='5']"))
#     ) 
#     select.click()
    
    # -- going back and forward
    
    driver.back() # go back
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.forward()
    driver.forward()
    
except: # if the text did not find then, pass it
    pass