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
driver.find_element("xpath", "/html/body/header/section/div/div/div[3]/div/div/div/a[1]").click()
time.sleep(3)
driver.find_element("name", "email").send_keys("albingeorgework284@gmail.com")
time.sleep(3)
driver.find_element("name", "password").send_keys("1234")
time.sleep(3)
driver.find_element("xpath", "/html/body/section/div/div/form/div[4]/button").click()
time.sleep(3)
print("User Logged In")

driver.find_element("xpath", "/html/body/section/div/div/aside/ul/a[3]").click()
time.sleep(3)
print("Clicked Edit profile")

driver.find_element("xpath", "/html/body/section/div/div/main/article/div/div[2]/div/form/div[3]/input").click()
time.sleep(3)
print("Clicked Address line")

address_line_1_element = driver.find_element("name", "address_line_1")
address_line_1_element.clear()
driver.find_element("name", "address_line_1").send_keys("Amal Jyothi College")
time.sleep(3)

address_line_1_element = driver.find_element("name", "address_line_2")
address_line_1_element.clear()
driver.find_element("name", "address_line_2").send_keys("Kanjirappally")
time.sleep(3)

driver.find_element("xpath", "/html/body/section/div/div/main/article/div/div[2]/div/form/input[2]").click()
time.sleep(3)
print("Clicked Save Button")
print("Test Passed")


