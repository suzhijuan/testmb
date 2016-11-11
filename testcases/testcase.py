import unittest
from appium import webdriver
from utils.utils import path, DecoMeta, generate_filename, pic_to_str
from pages.homepage import HomePage
import time


class TestCase(unittest.TestCase, metaclass=DecoMeta):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'whatever if only one'
        desired_caps['app'] = path(
            './app-standard-debug-3.1.5.-17.apk_3.1.5.-17.apk'
        )
        desired_caps['appPackage'] = 'com.molihe.test'
        # 'com.movier.magicbox'
        # 'vmovier.com.activity'
        # desired_caps['appActivity'] = '.ContactManager'
        desired_caps['appActivity'] = 'com.vmovier.magicbox.main.MainActivity'
        desired_caps['newCommandTimeout'] = 300
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.homepage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def shot(self, filename, time=0):

    #     print(self.driver.current_activity)
    #     self.driver.save_screenshot(str(filename) + ".png")

    # def ntest_(self):
    #     for i in range(5):
    #         self.shot(i, 1)
    #     el = self.driver.find_element_by_name("发现")
    #     el.click()
    #     self.shot(5)
    #     mine = self.driver.find_element_by_name("我")
    #     mine.click()
    #     self.shot(6)

    # def wait(self, timeout=10, poll_frequency=0.5):
    #     self.__wait = WebDriverWait(
    #         self.driver, timeout, poll_frequency=poll_frequency)
    #     return self.__wait

    def debug(self, delay=1, times=1):
        for i in range(times):
            print(self.driver.current_activity)
            self.driver.implicitly_wait(delay)

    def burst_shot(self, count=5, interval=1, delay=0):
        time.sleep(delay)
        fs = []
        for i in range(count):
            f = generate_filename()
            fs.append(f)
            self.driver.save_screenshot(f)
            time.sleep(interval)
        return fs

    def assertInToast(self, text):
        screenshots = self.burst_shot()
        results = []
        for f in screenshots:
            results.append(pic_to_str(f))
        print(results)
        inToast = False
        for result in results:
            if text in result:
                inToast = True
        self.assertTrue(inToast)
