from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://amzn.to/412lwrP")
image=driver.find_element(By.ID,"imgTagWrapperId")
#image=driver.find_element(By.ID,"//div[@id='imgTagWrapperId']")
#click_me=driver.find_element(By.XPATH,"//img[@id='landingImage']")
action=ActionChains(driver)
action.double_click(image).perform()
action.move_to_element(image).perform()