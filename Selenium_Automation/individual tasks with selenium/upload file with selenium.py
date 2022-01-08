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
driver.get('https://app.geckoform.com/public/?fbclid=IwAR0q9X73dE9xKIcvmBGhRjs_aUbVETJ1fdMnpsUOlNnt7u8b8P-g_qo5DPA#/modern/21FO00r2prn8tm00jet92j9ljt')
# driver.maximize_window()
driver.switch_to.frame
try:

    booked_before = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='chosen-container chosen-container-single']"))
    )
    booked_before.click()

    time.sleep(2)
    
#     selecting_no = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID,"field10633-option-3"))
#     )

#     selecting_no.click()

    selecting_no = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Have you already booked a sponsorship interview?: Search list']"))
    )
    selecting_no.click()
    selecting_no.clear()          # clear the input box first
    selecting_no.send_keys("No") # use your email
    selecting_no.send_keys(Keys.RETURN) # hit enter
    
    
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"form_4133"))
    )
    first_name.click()    
    first_name.clear()          # clear the input box first
    first_name.send_keys("jaja") # use your first name    
    
    
    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Last Name']"))
    )
    last_name.click()
    last_name.clear()
    last_name.send_keys("jaja") # use your last name
    

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"form_4134"))
    )
    email.click()    
    email.clear()          # clear the input box first
    email.send_keys("jaja@gmail.com") # use your email    
    
    
    std_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"form_4145"))
    )
    std_id.click()    
    std_id.clear()          # clear the input box first
    std_id.send_keys("16301023") # use your student id    
    
    
    phone_num = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"form_4138"))
    )
    phone_num.click()    
    phone_num.clear()          # clear the input box first
    phone_num.send_keys("5555") # use your phone number    
    

    drop_flag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='flag-dropdown']"))
    )
    drop_flag.click()
    
    
    choose_flag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//li[@data-country-code='bd']"))
    )
    choose_flag.click()
    time.sleep(1)
    
    
    drop_nationality = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//ul[@id='field4144_list']//parent::div[@class='chosen-drop']//parent::div[@class='chosen-container chosen-container-single']"))
    )
    drop_nationality.click()
    
    
    choose_nationality = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Please confirm your nationality: Search list']"))
    )
    choose_nationality.click()
    choose_nationality.clear()          # clear the input box first
    choose_nationality.send_keys("Bangladesh") # use your email
    choose_nationality.send_keys(Keys.RETURN) # hit enter
    
    
    upload_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Upload your video file here']"))
    )
    upload_btn.click()
    
    
    choose_file = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"inputfile_9982"))
    )
    choose_file.send_keys("C://Users/Moinul Islam Shawon/Downloads/TestCaseTemplate.xls") # give your own local file
    time.sleep(1)
    
    
    upload_file = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"file-upload_9982"))
    )
    upload_file.click()


    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"form-submit"))
    )
    
#     submit_button.click()

    
except: # if the text did not find then, pass it
    pass