'''
Created on 19-Feb-2023

@author: Smitha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from setuptools.command import upload_docs
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://testautomationpractice.blogspot.com/")
fileup=driver.find_element(By.XPATH,"//input[@type='file']")

#search.text("//C:\Users\Smitha\Pictures\Camera Roll")
action=ActionChains(driver)
action.double_click(upload_docs).perform()
#action.drag_and_drop_by_offset(slide,150,0).perform()
action.click_and_hold(fileup).move_by_offset(150,0).perform()

