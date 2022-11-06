from selenium import webdriver

chrome_browser = webdriver.Chrome()     #instantiate;OR path: webdriver.Chrome(r'D:\PYTHON\VScode\Automation_Testing\chromedriver')
# print(chrome_browser)
chrome_browser.maximize_window()        #just to maximize the window
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy' in chrome_browser.title
button_text = chrome_browser.find_element_by_class_name('btn btn-default')
print(button_text.get_attribute('innerHTML'))
