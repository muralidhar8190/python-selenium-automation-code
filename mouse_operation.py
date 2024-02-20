# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# action = ActionChains(driver)
# blogs = driver.find_element(By.ID, "blogsmenu")
# action.move_to_element(blogs).perform()
# time.sleep(3)

#Hovering:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# action = ActionChains(driver)
# blogs = driver.find_element(By.ID, "blogsmenu")
# action.move_to_element(blogs).perform()
#
# sub_blogs = driver.find_element(By.XPATH, "//a/span[text()='Selenium143']")
# action.move_to_element(sub_blogs).perform()
# time.sleep(3)
# driver.quit()

#Mouse left click:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# actions = ActionChains(driver)
# selenium143 = driver.find_element(By.ID, "link1")
# actions.move_to_element(selenium143).perform()
# time.sleep(3)
# driver.quit()

#Drag_and_Drop_by_offset:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/p/page3.html")
# action = ActionChains(driver)
# ele_slide = driver.find_element(By.XPATH, "//a[@aria-labelledby='price-min-label']")
# action.drag_and_drop_by_offset(ele_slide, 100, 0).perform()  #(x-dir, y-dir)
# time.sleep(3)
# driver.quit()

#mouse right click:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/")
# actions = ActionChains(driver)
# search_box = driver.find_element(By.NAME, "search")
# actions.context_click(search_box).perform()
# time.sleep(3)
# driver.quit()

#Double click:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# action = ActionChains(driver)
# double_click_option = driver.find_element(By.ID, "testdoubleclick")
# action.double_click(double_click_option).perform()
# time.sleep(3)
# driver.quit()

#click_and_hold:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# action = ActionChains(driver)
# element1 = driver.find_element(By.ID, "box3")
# element2 = driver.find_element(By.ID, "box101")
# action.click_and_hold(element1).move_to_element(element2).release().perform()
# time.sleep(3)
# driver.quit()

#Drag_and_Drop:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# action = ActionChains(driver)
# element1 = driver.find_element(By.ID, "box3")
# element2 = driver.find_element(By.ID, "box101")
# action.drag_and_drop(element1, element2).perform()
# time.sleep(3)
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# driver.find_element(By.NAME, "email").send_keys("sai@gmail.com")
# driver.find_element(By.ID, "input-password").send_keys("12345")
# action = ActionChains(driver)
# action.send_keys(Keys.ENTER).perform()
# time.sleep(3)
# driver.quit()

#key_up() and key_down():
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")
# for link in links:
#     action = ActionChains(driver)
#     action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
# time.sleep(3)
# driver.quit()

#Arrow_Down and Arrow_up:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.makemytrip.com/")
# driver.find_element(By.ID, "fromCity").click()
# driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys('g')
# time.sleep(3)
# action = ActionChains(driver)
# action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
# time.sleep(3)
# driver.quit()

# #Resizing element:
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://jqueryui.com/resizable/")
# frame_one = driver.find_element(By.CLASS_NAME, "demo-frame")
# driver.switch_to.frame(frame_one)
# actions = ActionChains(driver)
# dd = driver.find_element(By.CSS_SELECTOR, "div.ui-icon-gripsmall-diagonal-se")
# actions.drag_and_drop_by_offset(dd, 25, 50).perform()
# time.sleep(3)
# driver.quit()

#JQuery Right click:

import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(5)
button = driver.find_element(By.XPATH, "//span[text()='right click me']")
action = ActionChains(driver)
action.context_click(button).perform()
quit_option = driver.find_element(By.XPATH, "//li/span[text()='Quit']")  #Quit option click cheysinam
action.click(quit_option).perform()
time.sleep(5)
driver.quit()

#ActionChains() using pause:
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
driver.find_element(By.ID, "input-firstname").send_keys("sai")
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).pause(3).send_keys("Murali").pause(3).send_keys(Keys.TAB).send_keys("sai@gmail.com").pause(2).send_keys(Keys.TAB).send_keys("1234567899").pause(2).send_keys(Keys.TAB).send_keys("12345").pause(2).send_keys(Keys.TAB).pause(2).send_keys("12345").send_keys(Keys.TAB).pause(2).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).pause(3).send_keys(Keys.ENTER).perform()
time.sleep(6)
driver.quit()