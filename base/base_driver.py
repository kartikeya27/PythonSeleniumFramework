import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        
    # Function to wait for the loading indicator to disappear
    def wait_for_loading_indicator(self, timeout=120):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@ng-show='loaderstatus']//div[1]")))
        except TimeoutError:
            print("Loading indicator did not disappear.")
        
    def page_scroll(self):
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            match = False
            while (match == False):
                lastCount = pageLength
                time.sleep(1)
                pageLength = self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount == pageLength:
                    match = True
            time.sleep(4)
        
    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 120)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element