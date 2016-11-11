from .basepage import BasePage
from appium.webdriver.webdriver import By
from selenium.webdriver.support import expected_conditions as ec
from . import detailpage, webviewpage


from appium.webdriver.common.touch_action import TouchAction


class RecomendPage(BasePage):
    TITLE = (By.ID, "com.molihe.test:id/discoveryItemVideoTitleTv")
    BG_IMAGE = (By.ID, "com.molihe.test:id/discoveryItemBackgroundIv")
    CELL_LIVE = (By.NAME, "充值")

    def ready(self):
        self.wait().until(
            ec.presence_of_element_located(RecomendPage.BG_IMAGE))
        return self

    def click_background(self, index):
        self.driver.find_elements(*RecomendPage.BG_IMAGE)[index].click()

    def to_detailpage(self, index):
        self.ready().click_background(index)
        return detailpage.DetailPage(self.driver)

    def to_webviewpage(self, selector):
        action = TouchAction(self.driver)
        self.ready()
        for _ in range(30):
            try:
                cell = self.driver.find_element(*selector)
            except:
                action.press(self.driver.find_elements(
                    *RecomendPage.BG_IMAGE)[1]).move_to(
                    self.driver.find_elements(
                        *RecomendPage.BG_IMAGE)[0]).release().perform()
        cell.click()
        return webviewpage.WebviewPage(self.driver)
