from .testcase import TestCase
from pages import homepage


class TestSharePage(TestCase):
    def test_weibo_share(self):
        self.homepage.to_sharepage().weibo_share()
        # .wait_loaded()
        self.assertInToast(homepage.HomePage.TOAST_SHARE_SUCCESS)

    def test_qq_share(self):
        self.homepage.to_sharepage().qq_share()
        # .wait_loaded()
        self.assertInToast(homepage.HomePage.TOAST_SHARE_SUCCESS)
