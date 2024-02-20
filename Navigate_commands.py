# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "compendiumdev").click()
# time.sleep(3)
# driver.back()
# driver.forward()
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# time.sleep(3)
# driver.refresh()
# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# html_source_code=driver.page_source
# print(html_source_code)
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# driver.fullscreen_window()
# time.sleep(2)
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# time.sleep(2)
# driver.set_window_size(300, 800)
# time.sleep(2)
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.find_element(By.ID, "input-password").submit()
time.sleep(3)
driver.quit()