import pytest
import os
import time
import allure
import json
import sys
from allure_commons.types import AttachmentType


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument("-private")
        firefox_options.set_preference("dom.push.enabled", False)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=firefox_options)
        
    elif browser == "edge":
        edge_options = Options()
        # edge_options.add_argument("inprivate")
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install(),options=edge_options)
        )
    driver.get(url)
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver    
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    # extra = getattr(report, "extra", [])
    # if report.when == "call":
    #     # always add url to report
    #     extra.append(pytest_html.extras.url("http://www.yatra.com/"))
    #     xfail = hasattr(report, "wasxfail")
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         # only add additional html on failure
    #         report_directory = os.path.dirname(item.config.option.htmlpath)
    #         file_name = str(int(round(time.time() * 1000))) + ".png"
    #         # file_name = report.nodeid.replace("::", "_") + ".png"
    #         destinationFile = os.path.join(report_directory, file_name)
    #         driver.save_screenshot(destinationFile)
    #         if file_name:
    #             html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
    #                     'onclick="window.open(this.src)" align="right"/></div>'%file_name
    #         extra.append(pytest_html.extras.html(html))
    #     report.extra = extra
    # Check if the test has failed and is in the call phase (the test execution itself)
    if report.when == 'call' and report.failed:
        global driver
        if driver:
            screenshot_directory = os.path.join('reports', 'allure-results', 'screenshots')
            os.makedirs(screenshot_directory, exist_ok=True)
            screenshot_path = os.path.join(screenshot_directory, f'{int(time.time())}.png')
            driver.save_screenshot(screenshot_path)
            assert os.path.exists(screenshot_path), "Screenshot was not saved"

            if os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as file:
                    allure.attach(file.read(), name='Screenshot on failure', attachment_type=allure.attachment_type.PNG)
                    
def pytest_html_report_title(report):
    report.title = "Yatra Travel Website Automation Report"              
