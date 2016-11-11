from .basepage import BasePage
from appium.webdriver.webdriver import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class LivePage(BasePage):

    # MSG_INPUT = (By.CLASS_NAME, "android.widget.EditText")
    MSG = (By.ID, 'com.molihe.test:id/chatRoomChat')
    MSG_INPUT = (By.ID, 'com.molihe.test:id/chatbarEt')
    MSG_SEND = (By.ID, 'com.molihe.test:id/chatbarSend')
    GIFTS = (By.ID, 'com.molihe.test:id/chatRoomGift')
    GIFT_IMG = (By.ID, 'com.molihe.test:id/giftItemImg')
    GIFT_NAME = (By.ID, 'com.molihe.test:id/giftItemName')
    GIFT_PRICE = (By.ID, 'com.molihe.test:id/giftItemPrice')
    GIFT_SEND = (By.ID, 'com.molihe.test:id/giftSend')

    # TAPS = (By.ID, 'com.molihe.test:id/giftHitTextView')
    TAPS = (By.ID, 'com.molihe.test:id/giftHitLayout')

    def ready(self):
        self.wait().until(ec.presence_of_element_located(LivePage.MSG))
        return self

    def send_msg(self, times=1):
        for i in range(times):
            self.driver.find_element(*LivePage.MSG).click()
            self.driver.find_element(*LivePage.MSG_INPUT).send_keys(i)
            self.driver.find_element(*LivePage.MSG_SEND).click()
        return self

    def show_gift(self):
        self.driver.find_element(*LivePage.GIFTS).click()
        return self

    def send_gift(self, index=0):
        self.driver.find_elements(*LivePage.GIFT_IMG)[index].click()
        self.driver.find_element(*LivePage.GIFT_SEND).click()
        return self

    def multiple_hit(self, times=1):
        m = self.driver.find_element(*LivePage.TAPS)
        for i in range(times):
            m.click()
        return self

    def hits(self, index=0, times=0):
        self.driver.find_elements(*LivePage.GIFT_IMG)[index].click()
        give = self.driver.find_element(*LivePage.GIFT_SEND)
        give.click()
        if times:
            hit = None
            while not hit:
                try:
                    hit = self.driver.find_element(*LivePage.TAPS)
                except:
                    give.click()
            for _ in range(times):
                try:
                    hit.click()
                except NoSuchElementException:
                    give.click()
                    # self.driver.find_element(*LivePage.GIFT_SEND).click()
