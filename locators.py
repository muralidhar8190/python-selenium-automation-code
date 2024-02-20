import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
title_of_web_page_one = driver.title
print("Title Name: ",title_of_web_page_one)
time.sleep(5)
driver.find_element(By.LINK_TEXT,"onlytestingblog").click()
title_of_web_page_two = driver.title
print("Title Name: ",title_of_web_page_two)
driver.quit()




