from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pytest

from pageobjects.listpage import listpage
from pageobjects.loginpage import loginpage
from testdata.adduserdata import adduserdata
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")

class TestOne(BaseClass):

    def test_e2e(self):
        LoginPage = loginpage(self.driver)  # This one is return from login page object
        log = self.getlogger()
        # log.debug(dataload[0])
        # log.info(dataload[1])
        # print(dataload)
        log.info(LoginPage.get_mobileno())
        LoginPage.get_mobileno().send_keys("9876543210")  # this one is sent keyword to input box
        LoginPage.get_password().send_keys("P@ssw0rd")  # this one is sent keyword to input box
        LoginPage.Login().click()  # this function call from login page .py with loginpage object
        ListPage = listpage(self.driver)  # This one is return from Lostpage.py object
        add = ListPage.ProductList()  # Product list function has click to product list and return
        # object of another file which is add button and checkboxes
        add.ProductAdd().click()  # call product add function with object without import addpage.py
        # time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500);")
        log.info("getting all checkboxes")
        checkboxes = add.Productcheckboxes()  # checked checkboxes from addpage.py without import addpage.py
        time.sleep(3)
        #self.driver.execute_script("window.scrollBy(0,500);")

        for checks in checkboxes:  # checkboxes variable store all checkboxes to iterate one by one
            log.info(checks.is_selected())
            log.info(checks.text)
            #print(checks.text)
            checks.click()  # click on checkboxes from checkboxes array

            time.sleep(2)  # it wil wait for one second after clicking checkbox
        # time.sleep(3)
        adduser = ListPage.UserList()
        # time.sleep(3)
        adduser.ProductAdd().click()
        # time.sleep(5)
        log.info("Enterring area name in address")
        self.driver.find_element(By.ID, "setting-search-add").send_keys(
            "Maninadfggar")  # this one is send keyword to input box
        # print("1")
        # log.info("Enterring area name in address")
        self.verify_presence_of_element_located(
            "//div/ul/li/div[text()='Maninagar Cross Road, Balvatika, Maninagar, Ahmedabad, Gujarat']")
        # print("2")
        self.driver.find_element(By.XPATH,
                                 "//div/ul/li/div[text()='Maninagar Cross Road, Balvatika, Maninagar, Ahmedabad, Gujarat']").click()

    # time.sleep(5)
