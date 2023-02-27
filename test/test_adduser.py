from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pytest
from selenium.webdriver.support.select import Select
"""
from PythonSelfFramework.pageobjects.listpage import listpage
from PythonSelfFramework.pageobjects.loginpage import loginpage
from PythonSelfFramework.testdata.adduserdata import adduserdata
from PythonSelfFramework.utilities.BaseClass import BaseClass

"""
from pageobjects.addpage import addpage
from pageobjects.listpage import listpage
from pageobjects.loginpage import loginpage
from testdata.adduserdata import adduserdata
from utilities.BaseClass import BaseClass


class TestAddUser(BaseClass):
    def test_login(self):
        log = self.getlogger()
        login_credential = self.login_credential()
        LoginPage = loginpage(self.driver)  # This one is return from login page object
        log.info("Login with this mobile number " + login_credential["mobileno"])
        log.info("Login with this password " + login_credential["password"])
        LoginPage.get_mobileno().send_keys(login_credential["mobileno"])  # this one is sent keyword to input box
        LoginPage.get_password().send_keys(login_credential["password"])  # this one is sent keyword to input box
        self.Login().click()

    def test_submitUser(self, getdata):
        log = self.getlogger()
        ListPage = listpage(self.driver)  # This one is return from Lostpage.py object adduser = ListPage.UserList()
        adduser = ListPage.UserList()
        adduser.ProductAdd().click()
        #print(getdata["firmname"])
        adduser.get_firmname().send_keys(getdata["firmname"])  # this one is sent keyword to input box
        time.sleep(2)
        adduser.get_ownername().send_keys(getdata[
                                              "ownername"])  # this one is sent keyword to input box adduser.get_mobileno().send_keys(getdata["mobileno"])  # this one is sent keyword to input box
        adduser.get_mobileno().send_keys(getdata["mobileno"])
        adduser.get_genp().click()  # click on generate password button in form
        time.sleep(2)
        self.selectoptionbytext(adduser.get_status(), getdata["status"])
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        adduser.get_setting_search_add().send_keys(
            getdata["setting_search_add"])  # this one is sent keyword to input box
        self.verify_presence_of_element_located(
            "//div/ul/li/div[text()='Maninagar Cross Road, Balvatika, Maninagar, Ahmedabad, Gujarat']")
        self.driver.find_element(By.XPATH,
                                 "//div/ul/li/div[text()='Maninagar Cross Road, Balvatika, Maninagar, Ahmedabad, Gujarat']").click()
        adduser.get_searchAddressChecked().click()  # click to manually add address checkbox
        time.sleep(2)
        adduser.get_city().send_keys(getdata["city"])
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(2)
        adduser.get_submituser().click()

        # if getdata != None:
        success_text = adduser.get_succeesmessage().text
        # if success_text != "":
        log.info("success message recieved from add user " + success_text)
        time.sleep(5)
        assert ("Successfully" in success_text)
        time.sleep(5)

    # @pytest.fixture(params=[("9876514710","Psdds0rd"),
    #                       ("9876788788","P@ssw0rd"),
    #                       ("9876788788","P@sdsdsdsdsd"),
    #                       ("9876543210","P@ssw0rd")]) This fixture using tupple data
    @pytest.fixture(params=adduserdata.get_user_data())  # This fixture using dictionary data with key and value
    def getdata(self, request):
        return request.param