from .basepage import BasePage
from appium.webdriver.webdriver import By
from selenium.webdriver.support import expected_conditions as ec
from . import livepage


class WebviewPage(BasePage):
    LIVE_BUTTON = (By.CSS_SELECTOR, "div.live_go")
    CONFIRM_BUTTON = (By.NAME, "确定")
    INPUT_TEXT = (By.CSS_SELECTOR, 'input')

    def ready(self):
        self.wait().until(ec.presence_of_element_located(
            WebviewPage.CONFIRM_BUTTON))
        self.confirm()
        return self

    def confirm(self):
        self.driver.find_element(*WebviewPage.CONFIRM_BUTTON).click()

    def to_livepage(self, live_id):
        self.webview()
        room_id = self.driver.find_element(*WebviewPage.INPUT_TEXT)
        room_id.clear()
        room_id.send_keys(live_id)
        self.driver.find_element(*WebviewPage.LIVE_BUTTON).click()
        self.driver.switch_to.context(self.driver.contexts[0])
        return livepage.LivePage(self.driver)

    def webview(self):
        self.ready()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
