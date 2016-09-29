from .basepage import BasePage
from appium.webdriver.webdriver import By
from selenium.webdriver.support import expected_conditions as ec
from . import homepage


class SharePage(BasePage):

    SHARE_WEIXIN = (By.NAME, "微信好友")
    SHARE_CIRCLE = (By.NAME, "微信朋友圈")
    SHARE_WEIBO = (By.NAME, "新浪微博")
    SHARE_QQ = (By.NAME, "QQ好友")
    SHARE_QQZONE = (By.NAME, "QQ空间")
    SEND = (By.NAME, "发送")

    QQ_USER = (By.NAME, "g")
    QQ_SEND = (By.NAME, "发送")
    QQ_BACK = (By.NAME, "返回魔力盒")

    def wait_loaded(self):
        pass

    def weibo_share(self):
        self.driver.find_element(*SharePage.SHARE_WEIBO).click()
        self.wait().until(ec.presence_of_element_located(SharePage.SEND))
        self.driver.find_element(*SharePage.SEND).click()
        return homepage.HomePage(self.driver)

    def qq_share(self):
        self.driver.find_element(*SharePage.SHARE_QQ).click()
        self.wait().until(ec.presence_of_element_located(SharePage.QQ_USER))
        self.driver.find_element(*SharePage.QQ_USER).click()
        self.driver.find_element(*SharePage.QQ_SEND).click()
        self.wait().until(ec.presence_of_element_located(SharePage.QQ_BACK))
        self.driver.find_element(*SharePage.QQ_BACK).click()
        return homepage.HomePage(self.driver)
