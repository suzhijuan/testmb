from .testcase import TestCase
import time
from pages import recomendpage


class TestLivePage(TestCase):

    # def test_gift(self):
    #     rp = self.homepage.to_recomendpage()
    #     wp = rp.to_webviewpage(recomendpage.RecomendPage.CELL_LIVE)
    #     lp = wp.to_livepage(26)
    #     lp.ready().show_gift()
    #     lp.hits(times=999, index=2)

    def test_msg(self):
        rp = self.homepage.to_recomendpage()
        wp = rp.to_webviewpage(recomendpage.RecomendPage.CELL_LIVE)
        lp = wp.to_livepage(26)
        lp.ready().send_msg(1000)
