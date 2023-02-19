from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
#driver.find_element(By.XPATH,".//a[@class='gb_p' and @aria-label='Gmail (opens a new tab)']").click()
#driver.find_element(By.XPATH,"//button[@aria-label='No thanks']").click()
driver.switch_to.frame("callout")
driver.find_element(By.XPATH,"//button[@aria-label='No thanks']").click()
time.sleep(5)
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,".//a[@class='gb_p' and @aria-label='Gmail (opens a new tab)']").click()
