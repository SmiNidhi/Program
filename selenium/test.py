#Selenium code to Lunch the browser using URL : 
from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\Users\Smitha\Downloads\chromedriver_win32\\chromedriver.exe");
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.google.com");
webdriver.find_element_by_name('q').send_keys("selenium tutorial" )
