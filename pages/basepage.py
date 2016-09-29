from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.webdriver import By


class BasePage(object):
    PKG = "com.molihe.test"

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=10, poll_frequency=0.5):
        self.__wait = WebDriverWait(
            self.driver, timeout, poll_frequency=poll_frequency)
        return self.__wait
