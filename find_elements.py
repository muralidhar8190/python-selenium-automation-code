# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# elements = driver.find_elements(By.XPATH, "//select[@id='multiselect1']/option")
# for option in elements:
#     print(option.text)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/index.php?route=product/search&search=HP")
# links = driver.find_elements(By.XPATH, "//a")
# print(len(links))
# for link in links:
#     print(link.get_attribute("href"))
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.get_attribute("href"))
driver.quit()