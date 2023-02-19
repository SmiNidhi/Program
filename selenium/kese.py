from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
#driver.get("https://www.google.com")
#time.sleep(5)
driver.maximize_window()
driver.get("https://www.flipkart.com")
time.sleep(5)
search=driver.find_element(By.XPATH,"//input[@class='_3704LK']")
search.click()
search.send_keys("laptops")
