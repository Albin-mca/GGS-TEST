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
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

username_element = driver.find_element("name", "username")
username_element.clear()
driver.find_element("name", "username").send_keys("projectagk28@gmail.com")
time.sleep(3)

password_element = driver.find_element("name", "password")
password_element.clear()
driver.find_element("name", "password").send_keys("1234")
time.sleep(3)

driver.find_element("xpath", "/html/body/div/div[2]/div/div[1]/form/div[3]/button").click()
time.sleep(3)
print("Admin Logged In")

driver.find_element("xpath", "/html/body/div[2]/div/div/div/ul/li[7]/div[1]").click()
time.sleep(3)
driver.find_element("xpath", "/html/body/div[2]/div/div/div/ul/li[7]/div[2]/div[2]/a").click()
time.sleep(3)
driver.find_element("xpath", "/html/body/div[3]/div[3]/div/ul/li/div/a/i").click()
time.sleep(3)

driver.find_element("name", "product_name").send_keys("Testingg")
time.sleep(3)
driver.find_element("name", "description").send_keys("Testingg Description")
time.sleep(3)
driver.find_element("name", "price").send_keys("1000")
time.sleep(3)
driver.find_element("name", "product_name").send_keys("Testingg")
time.sleep(3)
