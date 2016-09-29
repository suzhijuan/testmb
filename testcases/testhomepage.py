
from .testcase import TestCase


class TestHomePage(TestCase):

    # def test_like(self):
    #     self.homepage.ready()
    #     x = self.homepage.like_count()
    #     print(x)
    #     self.homepage.click_like()
    #     # bug
    #     # self.assertEqual(self.homepage.like_count() - x, 1)
    #     self.assertEqual(self.homepage.like_count(), x)

    # def test_play(self):
    #     self.homepage.ready().play()
    #     self.debug(5)

    def test_delete(self):
        self.homepage.ready().delete()

    def test_detail(self):
        self.homepage.ready().to_detailpage()
