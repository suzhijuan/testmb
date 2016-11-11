from .basepage import BasePage
from appium.webdriver.webdriver import By
from selenium.webdriver.support import expected_conditions as ec
from . import openscreenpage, detailpage, sharepage, recomendpage
from enum import Enum


class CardState(Enum):
    network_error = 0
    downloaded = 1
    downloading = 2
    network_interrupted = 3
    error = 4
    predownload = 5


class HomePage(BasePage):

    TAB_HOME = (By.ID, "com.molihe.test:id/toolbar_molihe")
    TAB_FIND = (By.ID, "com.molihe.test:id/toolbar_faxian")
    TAB_ME = (By.ID, "com.molihe.test:id/toolbar_wo")

    LIKE = (By.ID, "com.molihe.test:id/magicview_like_icon")
    SHARE = (By.ID, "com.molihe.test:id/magicview_share_icon")
    COMMENT = (By.ID, "com.molihe.test:id/magicview_comment_icon")
    LIKE_COUNT = (By.ID, "com.molihe.test:id/magicview_like_count")
    SHARE_COUNT = (By.ID, "com.molihe.test:id/magicview_share_count")
    COMMENT_COUNT = (By.ID, "com.molihe.test:id/magicview_comment_count")

    LOGIN_SINA = (By.NAME, "新浪登录")
    LOGIN_WEIXIN = (By.NAME, "微信登录")
    LOGIN_QQ = (By.NAME, "QQ登录")

    REFRESH = (By.ID, "com.molihe.test:id/magicview_loading_restart")
    # "出错了, 点击重试"
    NETWORK_ERROR = (By.ID, "com.molihe.test:id/magicview_loading_label")
    # "请检查网络连接\n连接成功后, 会为您自动下载精彩短片"
    NO_NETWORK = (By.ID, "com.molihe.test:id/magicview_no_network_view")
    NETWORK = (By.ID, "com.molihe.test:id/magicview_speed_info")
    DOWNLOADING_SPEED = (By.ID, "com.molihe.test:id/magicview_speed_info")

    VIDEO_PLAY = (By.ID, "com.molihe.test:id/magicview_play")
    VIDEO_DOWNLOADING = (By.ID, "com.molihe.test:id/magicview_waveview")
    VIDEO_TITLE = (By.ID, "com.molihe.test:id/magicview_title")
    VIDEO_LABEL = (By.ID, "com.molihe.test:id/magicview_label")
    VIDEO_DELETE = (By.ID, "com.molihe.test:id/molihe_delete")

    INDICATOR = (By.ID, "com.molihe.test:id/molihe_indicator")

    TOAST_SHARE_SUCCESS = "分享成功"

    NEW_VERSION_FOUND = (By.NAME, "发现新版本")
    CANCEL_UPDATE = (By.NAME, "以后再说")

    def wait_loaded(self, timeout=10, poll_frequency=0.5):
        self.wait(timeout, poll_frequency).until(
            ec.presence_of_element_located(HomePage.TAB_HOME))

    def skip_openscreen(self):
        try:
            self.wait().until(ec.presence_of_element_located(
                openscreenpage.OpenScreenPage.SKIP))
            self.driver.find_element(
                *openscreenpage.OpenScreenPage.SKIP).click()
        except:
            pass

    def skip_update(self):
        try:
            self.wait().until(ec.presence_of_element_located(
                HomePage.NEW_VERSION_FOUND))
            self.driver.find_element(
                *HomePage.CANCEL_UPDATE).click()
        except:
            pass

    def skip(self):
        self.skip_openscreen()
        self.skip_update()

    def cancel_update(self):
        try:
            self.driver.find_element(*HomePage.NEW_VERSION_FOUND)
            self.driver.find_element(HomePage.CANCEL_UPDATE).click()
        except:
            pass

    def card_state(self):
        pass

    def ready(self):
        self.skip()
        self.cancel_update()
        self.wait_loaded()
        return self

    def click_share(self):
        self.driver.find_element(*HomePage.SHARE).click()
        return self

    def to_sharepage(self):
        # print(pages.openscreenpage.OpenScreenPage.SKIP)
        self.skip()
        self.wait_loaded()
        self.click_share()
        return sharepage.SharePage(self.driver)

    def click_like(self):
        self.driver.find_element(*HomePage.LIKE).click()
        return self

    def like_count(self):
        return int(self.driver.find_element(*HomePage.LIKE_COUNT).text)

    def click_find(self):
        self.driver.find_element(*HomePage.TAB_FIND).click()
        return self

    def play(self):
        self.driver.find_element(*HomePage.VIDEO_PLAY).click()
        return self

    def to_detailpage(self):
        self.driver.find_element(*HomePage.COMMENT).click()
        return detailpage.DetailPage(self.driver)

    def delete(self):
        self.driver.find_element(*HomePage.VIDEO_DELETE).click()
        return self

    def to_recomendpage(self):
        self.ready().click_find()
        return recomendpage.RecomendPage(self.driver)
