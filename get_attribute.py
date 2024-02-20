# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# x = driver.find_element(By.ID, "ta1").get_attribute("cols")
# print("attribute_value: ", x)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
y = driver.find_element(By.XPATH, "(//input[@title='search'])[2]").get_attribute("value")
print("label_name: ",y)
driver.quit()
