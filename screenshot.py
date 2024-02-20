# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://tutorialsninja.com/demo/")
# driver.save_screenshot("HomePage.png")
# driver.find_element(By.XPATH, "//div[@id='search']//button").click()
# driver.save_screenshot("Searchbutton.png")
# driver.quit()

#ii. get_screenshot_as_file("imagename.png")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/")
# driver.get_screenshot_as_file("HomePage.png")
# driver.find_element(By.XPATH, "//div[@id='search']//button").click()
# driver.get_screenshot_as_file("Searchbutton.png")
# driver.quit()

#Sections screenshot:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# section_links = driver.find_element(By.ID, "LinkList1")
# section_links.screenshot("Links.png")  #Links okati screenshot testhadi.
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/")
# button_img = driver.find_element(By.XPATH, "//div[@id='search']//button")
# button_img.screenshot("SearchButton.png")
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# driver.execute_script("alert('This is sai..!')")
# time.sleep(10)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# # driver.get("https://omayo.blogspot.com/")
# web_page_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
# print(web_page_height)
# driver.quit()

#Headless Mode:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #ee three line new ga add cheyali.
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options = chrome_options)
# driver.maximize_window()
# driver.get("https://tutorialsninja.com/demo/")
# title = driver.title
# print(title)
# driver.quit()

#Full Page Screenshot:

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #step1:
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options = chrome_options)
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# #step2:
# width = 1920
# height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
# #step3:
# driver.set_window_size(width, height)
# page_body = driver.find_element(By.TAG_NAME, "body")
# page_body.screenshot("Full_page_image1.png")
# driver.quit()

#Maximized Browser:
# import time
# from selenium import webdriver
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=chrome_option)
# time.sleep(5)
# driver.quit()

#Full Screen Mode:
import time
from selenium import webdriver
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--kiosk")
driver = webdriver.Chrome(options=chrome_option)
driver.fullscreen_window()
time.sleep(3)
driver.quit()
