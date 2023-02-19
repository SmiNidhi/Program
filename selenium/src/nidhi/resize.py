'''
Created on 19-Feb-2023

@author: Smitha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from tkinter.constants import VERTICAL
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://testautomationpractice.blogspot.com/")
header=driver.find_element(By.XPATH,"//h3[@class='ui-widget-header']")
action=ActionChains(driver)
action.click_and_hold(header).move_by_offset(150,40).perform()
footer=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']",)
action.click_and_hold(footer).move_by_offset(150,50).perform()

#size=driver.find_element(By.XPATH,"//h3[@class='ui-widget-header']")