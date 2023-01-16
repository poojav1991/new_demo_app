from selenium.webdriver.common.by import By
from selenium import webdriver


class loginpage:
    def __init__(self, driver):
        self.driver = driver
        #print("1.1")

    login = (By.XPATH, "//button[@type='submit']")
    mobileno = (By.ID, "login_mobileno")
    password = (By.ID, "login_password")

    def Login(self):
        return self.driver.find_element(*loginpage.login)
        # driver.find_element("id", 'login_mobileno')
    def get_mobileno(self):
        return self.driver.find_element(*loginpage.mobileno)
        # driver.find_element("id", 'login_mobileno')

    def get_password(self):
        return self.driver.find_element(*loginpage.password)
