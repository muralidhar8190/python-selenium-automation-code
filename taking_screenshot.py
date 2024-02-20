# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# driver.save_screenshot("Login.png")  #Direct ga project level lo store avuthadi image elaga esthey.
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# driver.get_screenshot_as_file("D:\\Python Practises\\Login_three.png")  #Ah location lo kavali antey ah location lo save chesukovachu.
# driver.quit()

#Retrieving the tag name.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# element_tag = driver.find_element(By.ID, "pah").tag_name
# print("Tag Name: ",element_tag)
# driver.quit()

#Finding the size of element.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/")
# driver.maximize_window()
# search_box_size = driver.find_element(By.NAME, "search").size
# print("Size of the element width and height: ",search_box_size)
# print(search_box_size.get("height: "))
# print(search_box_size.get("width: "))
# driver.quit()

#finding the element location.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/")
# search_box_loc = driver.find_element(By.NAME, "search").rect
# print("Location of the element x and y: ",search_box_loc)
# print(search_box_loc.get("height"))
# print(search_box_loc.get("width"))
# print(search_box_loc.get("x"))
# print(search_box_loc.get("y"))
# driver.quit()

#Finding the page load execution.
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(3)
driver.get("https://selenium143.blogspot.com/")
driver.quit()