from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()      #ChromeOptions will remove this error: Failed to read descriptor from node connection
chrome_browser = webdriver.Chrome() 
chrome_browser.maximize_window()        
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.title
show_message_button= chrome_browser.find_element(By.CSS_SELECTOR,'.btn')
# print(show_message_button.get_attribute('innerHTML'))

user_button2= chrome_browser.find_element(By.CSS_SELECTOR,'#get-input > .btn')   #to grap all buttons under the form get-input; # stands for id
print(user_button2)

# assert 'Show Message' in chrome_browser.page_source         #page_source is the entire html of the website

user_message = chrome_browser.find_element(By.ID,'user-message')
user_message.clear()                                    #to clear any previously entered msgs
user_message.send_keys('Prerak Panwar')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID,'display')

assert 'Prerak Panwar' in output_message.text           #OR output_message.get_attribute('innerHTML')

chrome_browser.quit()      #OR .close() or maybe 2 times .close()