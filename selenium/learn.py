from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#time.sleep(5)

singIn=driver.find_element(By.XPATH,"//button[@onclick='myFunction()']")
singIn.click()
time.sleep(2)
driver.switch_to.alert.accept()

print("you pressed me")
#singIn.click()
search=driver.find_element(By.XPATH,"you are pressed me")
#print("you pressed me")
#singIn.send_keys("alert").click()
#singIn.text
