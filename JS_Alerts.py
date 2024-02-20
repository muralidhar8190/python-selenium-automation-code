# Information Alert
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
# info_alert = driver.switch_to.alert
# print(info_alert.text)
# # info_alert.accept()
# info_alert.dismiss()
# driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()
# time.sleep(3)
# driver.quit()

# Confirmation Alert:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# time.sleep(3)
# conf_alert = driver.switch_to.alert
# print(conf_alert.text)
# conf_alert.accept()
# driver.quit()

#Prompt Alert:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# prompt_alert = driver.switch_to.alert
# print(prompt_alert.text)
# time.sleep(2)
# prompt_alert.send_keys("Sai Muralidhar..!")
# prompt_alert.accept()
# prompt_alert.dismiss()
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--disable-notification")
# driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
# driver.get("https://www.homedepot.com/")
# time.sleep(3)
# driver.quit()

#Handling the cookies dialog box.
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.opera.com/?utm_source=bing&utm_medium=pa&utm_campaign=Worldwide%20-%20Brand%20-%20EN&msclkid=e51b06b4b36e14f44e3b630cddeb6ac8&utm_term=Opera&utm_content=Branded%20-%20Exact")
# time.sleep(3)
# driver.find_element(By.XPATH, "//span[contains(text(), 'Accept cookies')]").click()
# time.sleep(3)
# driver.quit()

#Finding lightbox .

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/index.php?route=product/product&product_id=47&search=HP")
# time.sleep(3)
# driver.find_element(By.XPATH, "(//a[@title='HP LP3065'])[1]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()
# driver.quit()

#Default page load:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://selenium143.blogspot.com/")
# driver.find_element(By.LINK_TEXT, "What is Selenium?").click()
# driver.quit()

#Dropdown Field:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# drop_down_field = driver.find_element(By.ID, "drop1")
# x = Select(drop_down_field)
# x.select_by_visible_text("doc 3")
# time.sleep(3)
# x.select_by_index(2)
# time.sleep(3)
# x.select_by_value("mno")
# time.sleep(3)
# dropdown_option = x.options
# for y in dropdown_option:
#     print(y.text)

#Dropdown field:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# drop_down_field = driver.find_element(By.ID, "drop1")
# x = Select(drop_down_field)
# x.select_by_visible_text("doc 3")
# print(x.first_selected_option.text)
# driver.quit()

#Multiple selection box list:
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# drop_down_field = driver.find_element(By.ID, "multiselect1")
# x = Select(drop_down_field)
#This is selected options in list box.
# x.select_by_visible_text("Swift")
# x.select_by_value("audix")
# x.select_by_index(0)
# time.sleep(3)

#Deselect the options in list box.
# x.deselect_by_visible_text("Swift")
# x.deselect_by_value("audix")
# x.deselect_by_index(0)
#      (or)
#x.deselect_all()  #all deselect avuthadi.
# time.sleep(3)

# # is_multiple command:
# if x.is_multiple:
#     print("Multiple selection filed box")
# else:
#     print("Only one option select box")

#option command:
# option = x.options
# for y in option:
#     print(y.text)


#first_selected_option:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# drop_down_field = driver.find_element(By.ID, "multiselect1")
# x = Select(drop_down_field)
#
# x.select_by_visible_text("Audi")
# x.select_by_index(0)
# print(x.first_selected_option.text)
#
# multple_opt = x.all_selected_options
# for a in multple_opt:
#     print(a.text)

#Boostrap dropdown:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://getboostrap.com/docs/4.0/components/dropdowns/")
# driver.find_element(By.ID, "dropdownMenuButton").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[@id='dropdownMenuButton']/following-sibling::div/a[1]").click()
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
# driver.find_element(By.ID, "justAnInputBox").click()
# driver.find_element(By.XPATH, "(//span[contains(text(), 'choice 1  ')])[1]").click()
# driver.find_element(By.XPATH, "(//span[contains(text(), 'choice 5')])[1]").click()
# driver.find_element(By.XPATH, "(//span[contains(text(), 'choice 2 1')])[1]").click()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# male_radio_option = driver.find_element(By.ID, "radio1")
# #condition em antey radio check ayei untey pass, leydu click avaleydu antey click() echi select chestham male box ni
# if male_radio_option.is_selected():
#     pass
# else:
#     male_radio_option.click()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# orange_checkbox_option = driver.find_element(By.ID, "checkbox1")
# #Already tickmark unna box meda click chesthey deselect avuthadi.
# if orange_checkbox_option.is_selected():
#     orange_checkbox_option.click()
# else:
#     pass
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# blue_checkbox_option = driver.find_element(By.ID, "checkbox2")
# #Blue checkbox tickmark leydu antey tickmark paduthdi, else tickmark leydu antey tickmark paduthadi.
# if blue_checkbox_option.is_selected():
#     pass
# else:
#     blue_checkbox_option.click()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# text_area_field_one = driver.find_element(By.ID, "ta1")
# text_area_field_one.send_keys("My name is sai..!")
# driver.find_element(By.LINK_TEXT, "compendiumdev").click()
# driver.back()
# time.sleep(3)
# text_area_field_one.clear()
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/iframe")
# # driver.switch_to.frame("mce_0_ifr")  #id="mce_0_ifr"
# driver.find_element(By.XPATH, "//body[@id='tinymce']/p").clear()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://docs.oracle.com/javase/8/docs/api/")
# driver.switch_to.frame("classFrame")
# driver.find_element(By.LINK_TEXT, "Description").click()
# time.sleep(3)


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://blogpendingtasks.blogspot.com/p/switchtoframeusingwebelement.html")
# #first iframe ni findout cheysi oka variable store cheysi, inside iframe lo ki veyli element ni findout cheysinam.
# iframe_element = driver.find_element(By.XPATH, "//iframe[@title='arunmotoori']")
# driver.switch_to.frame(iframe_element)
# driver.find_element(By.LINK_TEXT, "Home").click()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/iframe")
# time.sleep(3)
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//body[@id='tinymce']/p").clear()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://letcode.in/frame")
#Parent Frame ki Jump ayeina.
# driver.switch_to.frame("firstFr")
# driver.find_element(By.NAME, "fname").send_keys("Sai...")
# driver.find_element(By.NAME, "lname").send_keys("Murali")
#Child Frame ki jump ayeina next.
# child_frame = driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")
# driver.switch_to.frame(child_frame) #Ekada inside frame lo ki vacha
# driver.find_element(By.NAME, "email").send_keys("sai@gmail.com")
# time.sleep(3)
#clear email id data
# driver.find_element(By.NAME, "email").clear()
#direct child to parent frame ki jump avuthadi. clear firstname and lastname element data.
# driver.switch_to.parent_frame()
# driver.find_element(By.NAME, "fname").clear()
# driver.find_element(By.NAME, "lname").clear()
# time.sleep(3)
#Direct jump to main page level using "default_content" cmd
# driver.switch_to.default_content()
# page_heading = driver.find_element(By.XPATH, "//div[@class='container']/h1").text
# print(page_heading)  #print main level heading
# driver.quit()

#Parent child sibling:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/nested_frames")
# driver.switch_to.frame("frame-top")  #name="frameset-middle"
# driver.switch_to.frame("frame-left")  #name="frame-left"
# left_text = driver.find_element(By.XPATH, "//body").text
# print(left_text)
# time.sleep(3)

#parent frame ki jump ayei, again child frame ki jump avutham.
# driver.switch_to.parent_frame()
# driver.switch_to.frame("frame-middle") #name="frame-middle"
# middle_text = driver.find_element(By.XPATH, "//div[@id='content']").text
# print(middle_text)
# time.sleep(3)

#again parent frame ki vachi, second child frame ki jump avutham.
# driver.switch_to.parent_frame()
# driver.switch_to.frame("frame-right")
# right_text = driver.find_element(By.XPATH, "//body").text
# print(right_text)
# time.sleep(3)

#again main page level frame ki vachi, bottom parent frame ki jump avutham.
# driver.switch_to.default_content()
# driver.switch_to.frame("frame-bottom")
# bottom_text = driver.find_element(By.XPATH, "//body").text
# print(bottom_text)


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)
driver.quit()
