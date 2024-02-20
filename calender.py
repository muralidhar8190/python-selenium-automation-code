# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calender-in-selenium.html")

# driver.find_element(By.ID, "datepicker").click()
#
# wait = WebDriverWait(driver, 5)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))
#
#
# def select_date_in_calender(month, year, day):
#     current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#
#     while not(current_month.__eq__(month) and current_year.__eq__(year)):
#         driver.find_element(By.XPATH, "//span[text()='Next']").click()
#         current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#         current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#     day_text = "//td[@data-handler='selectDay']/a[text()='"+str(day)+"']"
#     driver.find_element(By.XPATH, day_text).click()
# select_date_in_calender("August", "2025", "19")
# driver.quit()


#JavaScript Calender:
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calender-in-selenium.html")
# driver.execute_script("document.getElementById('datepicker'), value='19/08/2024'")
# time.sleep(2)
# driver.quit()

# select the past dates:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calender-in-selenium.html")
# #click calender field
# driver.find_element(By.ID, "datepicker").click()
# #calender box ni alagey hold cheyali kabbati WebDriverWait use chestham some time kosam.
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))
#
# #calender lo current month ni text chestham
# current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
# #calender lo current year ni text chestham
# curernt_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#
# while not(current_month.__eq__("May") and curernt_year.__eq__("2000")):
#     driver.find_element(By.XPATH, "//span[text()='Prev']")
#     #Latest months and year store avuthadi every loop lo, manaku kavalisna month and year vasthey loop stop avuthadi.
#     current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     curernt_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
# #Select the date
# driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[text()='27']").click()
# time.sleep(3)
# driver.quit()

#select past and future dates calender using selenium
# import time
# from datetime import datetime
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calender-in-selenium.html")
# driver.find_element(By.ID, "datepicker").click()
#
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))
#
# expected_date = "2028-08-19"
# formatted = datetime.strptime(expected_date, "%Y-%m-%d")
# date = formatted.day
# month = formatted.month #int lo undi edi
# year = formatted.year  #int lo undi edi
# print(date, month, year)
#
# current_month_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
# month_number = {"January":1, "Febuary":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
# current_month_nbr = month_number[current_month_text]
# print(current_month_nbr)
#
# current_year_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
# current_year_nbr = int(current_year_text)
#
# while current_year_nbr < year or current_month_nbr < month:
#     driver.find_element(By.XPATH, "//span[text()='Next']").click()
#     current_month_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     month_number = {"January": 1, "Febuary": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
#                     "September": 9, "October": 10, "November": 11, "December": 12}
#     current_month_nbr = month_number[current_month_text]
#     current_year_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#     current_year_nbr = int(current_year_text)
#
# while current_year_nbr > year or current_month_nbr > month:
#     driver.find_element(By.XPATH, "//span[text()='Prev']").click()
#     current_month_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     month_number = {"January": 1, "Febuary": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
#                     "September": 9, "October": 10, "November": 11, "December": 12}
#     current_month_nbr = month_number[current_month_text]
#     current_year_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#     current_year_nbr = int(current_year_text)
#
# driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[text()='"+str(expected_date)+"']").click()
# time.sleep(3)
# driver.quit()

#Type 3 calender:
# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("https://demo.guru99.com/test/")
# driver.find_element(By.NAME, "bdaytime").send_keys("19082028") #ddmmyyyy
# driver.find_element(By.NAME, "bdaytime").send_keys(Keys.TAB) #press Tab key
# driver.find_element(By.NAME, "bdaytime").send_keys(1050)  #minuteseconds
# driver.find_element(By.XPATH, "//input[@type='submit']")  #submit button
# time.sleep(5)
# driver.quit()

#Type 4 Calender:
# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
# driver.find_element(By.ID, "third_date_picker").click()
# #Hold the hole calender
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))
# driver.find_element(By.XPATH, "//option[text()='Nov']").click() #select month
# driver.find_element(By.XPATH, "//option[text()='2034']").click() #select year
# driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[text()='22']").click() #select date
# time.sleep(5)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
# driver.find_element(By.ID, "third_date_picker").click()
# #Hold the hole calender
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))
#
# #dropdown kabbati Select() use cheysi easy ah month ayeina findout cheyavachu.
# dropdown_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
# select_month = Select(dropdown_month)
# select_month.select_by_visible_text("Nov")
#
# #dropdown kabbati Select() use cheysi easy ah year ayeina findout cheyavachu.
# dropdown_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
# select_year = Select(dropdown_year)
# select_year.select_by_visible_text("2034")
#
# driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[text()='22']").click() #select date
# time.sleep(5)
# driver.quit()

#Type 5 Calender:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
# driver.find_element(By.ID, "fourth_date_picker").click()
# #Hold the hole calender
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))

# #dropdown kabbati Select() use cheysi easy ah month ayeina findout cheyavachu.
# dropdown_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
# select_month = Select(dropdown_month)
# select_month.select_by_visible_text("Aug")
#
# #dropdown kabbati Select() use cheysi easy ah year ayeina findout cheyavachu.
# dropdown_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
# select_year = Select(dropdown_year)
# select_year.select_by_visible_text("2024")
# driver.find_element(By.XPATH, "(//td[@data-handler='selectDay']/a[text()='28'])[2]").click() #select date
# time.sleep(5)
# driver.quit()

#Type 6 calender:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
driver.find_element(By.CLASS_NAME, "ui-datepicker-trigger").click()
#Hold the hole calender
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))

driver.find_element(By.CSS_SELECTOR, "td.ui-datepicker-today").click()
time.sleep(5)
driver.quit()