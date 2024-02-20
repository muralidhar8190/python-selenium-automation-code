# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# url_one = driver.current_url
# print("Url link: ", url_one)
# driver.find_element(By.LINK_TEXT, "testwisely").click()
# url_two = driver.current_url
#
#print("Url link: ", url_two)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Open a popup window").click()
time.sleep(3)
driver.close()