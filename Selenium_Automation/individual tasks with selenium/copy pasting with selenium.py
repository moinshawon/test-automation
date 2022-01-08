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
driver.get('https://github.com/login') # go to the site


driver.implicitly_wait(3) # wait 3 sec before doing next task

head_line = driver.find_element_by_xpath("//label[@for='login_field']")
email_input = driver.find_element_by_xpath("//input[@id='login_field']")
password_input = driver.find_element_by_xpath("//input[@id='password']")

# -- copy element 'Username or email address' but address will be copied

copy_action = ActionChains(driver) # creating an instance of ActionChains
copy_action.move_to_element(head_line) # move to 'Username or email address'
copy_action.double_click() # for copy we need to double click
copy_action.key_down(Keys.CONTROL).send_keys('c') # press down + ctrl + copy 

# -- paste it to user input box and copy again

copy_action.move_to_element(email_input) # go to user input box
copy_action.click() # click it to write anything
copy_action.key_down(Keys.CONTROL).send_keys('v') # paste it
time.sleep(2)
copy_action.send_keys('a').send_keys('c') 
# copying all what just pasted there
# still holding 'down' so no need to mention key_down

# -- copy from the user input box and paste it to password input box

copy_action.move_to_element(password_input) # go to pass box
copy_action.click() 
time.sleep(2)
copy_action.key_down(Keys.CONTROL).send_keys('v') # press down: and paste
copy_action.perform() # execute all

sign_in_btn = driver.find_element_by_xpath("//input[@name='commit']")
sign_in_btn.click()
