from .basepage import BasePage
from appium.webdriver.webdriver import By


class OpenScreenPage(BasePage):
    SKIP = (By.ID, "com.molihe.test:id/skipTextView")
    IMAGE = (By.ID, "com.molihe.test:id/openImageView")
