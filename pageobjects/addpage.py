from selenium.webdriver.common.by import By


class addpage:
    def __init__(self, driver):
        self.driver = driver
        # print("1.1")

    # product = (By.XPATH, "//li[@class='nav-item']/a/p[contains(text(), 'Products')]")
    add = (By.LINK_TEXT, "Add")
    firmname = (By.XPATH, "//*[@id='firmname']")
    ownername = (By.ID, "ownername")
    mobileno = (By.ID, "mobileno")
    genp = (By.ID, "genp")
    setting_search_add = (By.ID, "setting-search-add")
    searchAddressChecked = (By.ID, "searchAddressChecked")
    city = (By.ID, "city")
    status = (By.XPATH, "//select[@name='status']")
    submituser = (By.CSS_SELECTOR, "[type='submit']")
    succeesmessage = (By.XPATH, "//div[@class='alert alert-success']")
    # genp = (By.ID, "genp")
    checkboxes = (By.XPATH, "//label[@class='form-check-label']")

    def Productcheckboxes(self):
        return self.driver.find_elements(*addpage.checkboxes)
    def get_status(self):
        return self.driver.find_element(*addpage.status)
    def ProductAdd(self):
        return self.driver.find_element(*addpage.add)

    def get_firmname(self):
        # print("test get firmname")
        return self.driver.find_element(*addpage.firmname)

    def get_ownername(self):
        return self.driver.find_element(*addpage.ownername)

    def get_mobileno(self):
        return self.driver.find_element(*addpage.mobileno)

    def get_genp(self):
        return self.driver.find_element(*addpage.genp)

    def get_setting_search_add(self):
        return self.driver.find_element(*addpage.setting_search_add)

    def get_searchAddressChecked(self):
        return self.driver.find_element(*addpage.searchAddressChecked)

    def get_city(self):
        return self.driver.find_element(*addpage.city)

    def get_submituser(self):
        return self.driver.find_element(*addpage.submituser)

    def get_succeesmessage(self):
        return self.driver.find_element(*addpage.succeesmessage)
