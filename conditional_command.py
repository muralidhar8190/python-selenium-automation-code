# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# if driver.find_element(By.ID, "ta1").is_displayed():
#     print("Element is displayed on the page.")
# else:
#     print("Not Displayed.")

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//span[text()='My Account']").click()
# driver.find_element(By.LINK_TEXT, "Login").click()
# driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("sai@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")
# driver.find_element(By.XPATH, "//input[@value='Login']").click()
# time.sleep(5)
# if driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed():
#     print("User got logged in sucessfully.")
# else:
#     print("Not Login")
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# if driver.find_element(By.ID, "hbutton").is_displayed():
#     print("Displayed")
# else:
#     print("Not Displayed")
# driver.quit()

import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# if driver.find_element(By.ID, "but1").is_enabled():
#     print("Enabled State")
# else:
#     print("Not Enable State")
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# if driver.find_element(By.ID, "checkbox1").is_selected():
#     print("Selected State")
# else:
#     print("Not Selected State")
# driver.quit()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# if driver.find_element(By.ID, "checkbox2").is_selected():
#     print("Selected State")
# else:
#     print("Not Selected State")
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
if driver.find_element(By.XPATH, "//input[@value='Bike']").is_selected():
    print("Selected State")
else:
    print("Not Selected State")
driver.quit()

#This is conditional statement