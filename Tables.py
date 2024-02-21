import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# table_heading_text = driver.find_elements(By.XPATH, "//table[@id='table1']/thead")
# for data in table_heading_text:
#     print(data.text)
# driver.quit()

import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# table_heading = driver.find_element(By.XPATH, "//table[@id='table1']//th")
# for headings in table_heading:
#     print(headings.text)
# driver.quit()
#

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# table_data = driver.find_elements(By.XPATH, "//table[@id='table1']//td")
# for data in table_data:
#     print(data.text)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# table_data = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody//td[3]")
# for data in table_data:
#     print(data.text)
# driver.quit()

#Printing entire table:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# rows = driver.find_elements(By.XPATH, "//table[@id='table1']//tr")
# rows_count = len(rows)
# colunms = driver.find_elements(By.XPATH, "//table[@id='table1']//th")
# colunms_count = len(colunms)
#
# for r in range(1, rows_count+1):
#     for c in range(1, colunms_count+1):
#         if r == 1:
#             data = driver.find_element(By.XPATH, "//table[@id='table1']//tr["+str(r)+"]//th+["+str(c)+"]")
#             print(data.text, end=" ")
#         else:
#             data = driver.find_element(By.XPATH, "//table[@id='table1']//tr["+str(r-1)+"]//td+["+str(c)+"]")
#             print(data.text, end=" ")
#         print()
# driver.quit()

#Dynamic Table:
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.opencart.com/admin/")
# driver.find_element(By.ID,"input-username").send_keys("demo")
# driver.find_element(By.ID, "input-password").send_keys("demo")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.CLASS_NAME, "btn-close").click()
# driver.find_element(By.XPATH, "//a[contains(text(), 'Sales')]").click()
# driver.find_element(By.XPATH, "//a[contains(text(), 'Orders')]").click()
#
# expected_customer_name = "gaurav singh"
# xpath_text = "//form[@id='form-order']//tr//td[text()='"+expected_customer_name+"']"
# driver.find_element(By.XPATH, xpath_text+"/preceding-sibling::td[3]").click()
# time.sleep(3)
# driver.quit()

#Dynamic Table in Pagination.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/")
driver.find_element(By.ID,"input-username").send_keys("demo")
driver.find_element(By.ID, "input-password").send_keys("demo")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "btn-close").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Sales')]").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Orders')]").click()

expected_customer_name = "gaurav singh"
xpath_text = "//form[@id='form-order']//tr//td[text()='"+expected_customer_name+"']"

page_text = driver.find_element(By.XPATH, "//div[contains(text(), 'Showing 1 to 10' )]").text
start_index = page_text.index("(")+1
end_index = page_text.index("Pages)")-1

pages = int(page_text[start_index:end_index])
for page in range(1, pages+1):
    driver.find_element(By.XPATH, xpath_text + "/preceding-sibling::td[3]").click()

driver.quit()

def test_sample():
    print("Sample Text Case")

def test_sample_1():
    print("Sample Text Case_1")






