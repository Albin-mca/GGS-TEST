from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
print("Login test case started")
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
driver.find_element("xpath", "/html/body/header/section/div/div/div[3]/div/div/div/a[2]").click()
time.sleep(3)
print("Clicked Register")

driver.find_element("name", "first_name").send_keys("Abraham")
time.sleep(3)
driver.find_element("name", "last_name").send_keys("Lincoln")
time.sleep(3)
driver.find_element("name", "email").send_keys("abraham@gmail.com")
time.sleep(3)
driver.find_element("name", "phone_number").send_keys("9191929293")
time.sleep(3)
driver.find_element("name", "password").send_keys("Abraham@123")
time.sleep(3)
driver.find_element("name", "confirm_password").send_keys("Abraham@123")
time.sleep(3)


driver.find_element("xpath", "/html/body/section/div/article/form/div[4]/button").click()
time.sleep(3)
print("Test Passed")





