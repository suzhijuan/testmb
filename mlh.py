import os
import unittest
from appium import webdriver
from appium.webdriver.webdriver import By
from time import sleep

# Returns abs path relative to this file and not cwd


def path(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class MagicboxTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'whatever if only one'
        desired_caps['app'] = path(
            './app-standard-debug-3.1.3.6.apk_3.1.3.6.apk'
        )
        desired_caps['appPackage'] = 'com.molihe.test'
        # 'com.movier.magicbox'
        # 'vmovier.com.activity'
        # desired_caps['appActivity'] = '.ContactManager'
        desired_caps['appActivity'] = 'com.vmovier.magicbox.main.MainActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def shot(self, filename, time=0):
        sleep(time)
        print(self.driver.current_activity)
        self.driver.save_screenshot(str(filename) + ".png")

    def ntest_(self):
        for i in range(5):
            self.shot(i, 1)
        el = self.driver.find_element_by_name("发现")
        el.click()
        self.shot(5)
        mine = self.driver.find_element_by_name("我")
        mine.click()
        self.shot(6)

    def like_card(self):
        sleep(10)
        self.shot('card0', 3)
        ivs = self.driver.find_elements_by_class_name(
            'android.widget.ImageView')
        # el = self.driver.find_element_by_class_name(
        #     'android.widget.ImageView')
        ivs[2].click()
        self.shot('card1', 3)
        sleep(3)

    # def test_sina_login(self):
    #     print(self.driver.current_activity)
    #     sleep(10)
    #     mine = self.driver.find_element_by_name("我")
    #     mine.click()
    #     click_me_to_login = self.driver.find_element_by_name("点击登录")
    #     click_me_to_login.click()
    #     weixin_login = self.driver.find_element_by_name("新浪登录")
    #     weixin_login.click()

    #     for i in range(10):
    #         print(self.driver.current_activity)
    #         print(self.driver.contexts)
    #         sleep(1)

    #     sleep(10)

    def weixin_login(self):
        # self.driver.switch_to.context('WEBVIEW_com.molihe.test')
        # weixin_confirmation = self.driver.find_element_by_name("确认登录")
        # weixin_confirmation.click()
        pass

    def test_weibo_share(self):
        print(self.driver.current_activity)
        sleep(10)
        self.driver.find_element(by=By.ID,
                                 value='com.molihe.test:id/magicview_share_icon').click()
        self.driver.find_element(by=By.NAME, value="新浪微博").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value="发送").click()
        self.driver.implicitly_wait(10)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MagicboxTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
