from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/atpl/Downloads/chromedriver")
driver.get("https://auditorium.mydemoapp.us/admin/time-slot")
time.sleep(5)
print(driver.title)  # it will display auditorium page
driver.get("https://safaidaar.mydemoapp.us/admin/login")
time.sleep(5)
print(driver.title)  # it will display safaidaar page

driver.back()  # It will Get back window page
time.sleep(5)
print(driver.title)  # it will display auditorium page
driver.refresh()  # it willl refresh the page
driver.forward()  # it will get next  page
time.sleep(5)
print(driver.title)  # it will display safaidaar page
