from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.maximize_window()
#time.sleep(5)
driver.switch_to.frame("callout")
#search=driver.find_element(By.XPATH,"//button[//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[2]/a]").click()
singIn=driver.find_element(By.XPATH,"//a[@aria-label='Sign in']")
singIn.click()
driver.switch_to.window(driver.window_handles[1])
search=driver.find_element(By.XPATH,"//input[@type='email']")
#switch.input.type.add_text('email')
search.send_keys("smithachandrappa111@gmial.com")
time.sleep(5)
driver.switch_to.parent_frame()
search.text
#search=driver.find_element(By.XPATH,"//input@type='Email or phone']")

