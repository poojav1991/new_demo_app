import time

import pytest
#from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


# from selenium.webdriver.Chrome import webdriver
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/home/atpl/selenium-firefox/drivers/geckodriver")

    driver.implicitly_wait(5)
    driver.get("https://koilapp.mydemoapp.us/admin/login")
    # driver.get("https://www.amarinfotech.com/")
    driver.maximize_window()  # it will maximize the driver window
    # time.sleep(5)
    # driver.close()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

     #   Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
      #  :param item:

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + time.ctime() + ".png"
            mod_string = file_name[5:]
            mod_string = 'screenshot/' + mod_string
            _capture_screenshot(mod_string)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % mod_string
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    # driver.get_screenshot_as_file(name)
    # path = '/home/atpl/Pooja/PycharmProjects/PythonSelfFramework/screenshot/'+name

    driver.get_screenshot_as_file(name)
