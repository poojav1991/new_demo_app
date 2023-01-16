import inspect
from telnetlib import EC
import logging

import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.loginpage import loginpage


@pytest.mark.usefixtures("setup")
class BaseClass:
    # def implicitlywait(self):
    login = (By.XPATH, "//button[@type='submit']")
    def verify_presence_of_element_located(self, text):
        wait = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, text)))
        #

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logfile.log")
        formattor = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formattor)
        logger.addHandler(filehandler)  # file handler object
        logger.setLevel(logging.DEBUG)
        return logger

    def selectoptionbytext(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def login_credential(self):
        test_login = {"mobileno": "9876543210", "password": "P@ssw0rd"}
        return test_login
    def Login(self):
        return self.driver.find_element(*loginpage.login)