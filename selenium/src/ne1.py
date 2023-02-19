from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
#driver.find_element(By.XPATH,"//*[@id='gb']/div/div[1]/div/div[1]/a").click()
#driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").click()
driver.find_element(By.XPATH,"//a[text()='clothes']").click()
driver.find_element(By.XPATH,"//[@id='contentGrid_578260']/div/div[1]/div/div/div/a").click()

#driver.find_element(By.XPATH,"//a[text()='Gmail']").click()