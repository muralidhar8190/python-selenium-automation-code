# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.LINK_TEXT, "Open a popup window").click()
# page_text = driver.find_element(By.XPATH, "//div[@class='example']/h3").text
# print(page_text)
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# #current window ki loki veyli pakkaga next, ah application ah element ayeina findout cheyali.
# app_current_window = driver.current_window_handle
# driver.find_element(By.ID, "selenium143").click()
# child_window_jump = driver.window_handles  #Multiple windows cmd
# for w in child_window_jump:
#     driver.switch_to.window(w)
#     if driver.title.__eq__("Selenium143 "):
#         driver.find_element(By.LINK_TEXT, "What is Selenium?").click()
#         time.sleep(3)
#         driver.close()
#         break
#
# driver.switch_to.window(app_current_window)  #parent window switch ayeinam.
# driver.find_element(By.ID, "ta1").send_keys("Muralidhar")
# driver.close()

#New window:
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# page_one_title = driver.title
# print(page_one_title)
# #switch.to_window('window') antey only new window open avuthadi, ah window lo get() method use cheysi new application link pass chestham. elaga
# driver.switch_to.new_window('window')  #Empty new window open avuthadi anthey.
# driver.get("https://selenium143.blogspot.com/")  #Empty window lo ee application open avuthadi.
# page_two_title = driver.title
# print(page_two_title)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.CLASS_NAME, "dropbtn").click()
# wait = WebDriverWait(driver, timeout=30, poll_frequency=5, ignored_exceptions=[NoSuchElementException])
# flipkart_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Flipkart")))
# flipkart_option.click()
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.CLASS_NAME, "dropbtn").click()
# wait = WebDriverWait(driver, 10)
# flipkart_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Flipkart")))
# flipkart_option.click()
# driver.quit()






# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.CLASS_NAME, "dropbtn").click()
#
# wait = WebDriverWait(driver, 30)
# flipkart_options = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Flipkart")))
# flipkart_options.click()
# driver.quit()
#until class anduku chestham antey element path ni direct ga ekada pass cheyavachu until use cheysi. By default ga driver.find_element(By.LINK_TEXT, "fLIPKART") elaga estham kada, adey manam explicit wait lo manaku kavalisna element path ekada esthey chalu direct ah element ni findout chesthadi.

#presence_of_element_located():
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# wait = WebDriverWait(driver, 10)
# hidden_button = wait.until(expected_conditions.presence_of_element_located((By.ID, "hbutton")))
# hidden_button_label = hidden_button.get_attribute("value")
# print(hidden_button_label)
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.XPATH, "//button[text()='Check this']").click()
# wait = WebDriverWait(driver, 15)
# checkbox_tick = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'dte')))
# checkbox_tick.click()
# time.sleep(3)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.find_element(By.XPATH, "//button[text()='Start']").click()
#
# wait = WebDriverWait(driver, 30)
# progress_section = wait.until(expected_conditions.invisibility_of_element_located((By.ID, "loading")))
# heading_text = driver.find_element(By.XPATH, "//div[@id='finish']/h4").text
# print(heading_text)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.find_element(By.ID, "alert1").click()
# x = WebDriverWait(driver, 5)
# x.until(expected_conditions.alert_is_present())
# al = driver.switch_to.alert
# print(al.text)
# al.accept()  #okay button click avuthadi.
# driver.quit()

#Dynamic Xpath:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
for i in range(1, 6):
    xpath_text = "(//div[@id='LinkList1']//a)["+str(i)+"]" #Dynamic xpath
    driver.find_element(By.XPATH, xpath_text).click()
    driver.back()
    time.sleep(2)
driver.quit()

