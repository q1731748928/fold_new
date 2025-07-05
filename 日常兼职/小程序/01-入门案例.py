import time

from appium.webdriver import webdriver
from selenium.webdriver.common.by import By

class TestWXMicroView:
    def setup(self):
        caps = {}
        caps["platformName"]= "Android"
        caps["deviceName"]= "Tango"
        caps["appPackage"]= "com.tencent.mm"
        caps["appActivity"]="com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps['unicodeKeyboard']= True
        caps['resetKeyboard']= True
        caps['chromedriverExecutable']= "/users/tango/Documents/B站直播/1.Python/MP _Test/src/chromedriver"
        self.driver.implicitly_wait(30)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH,"//*[@text='通讯录']")
        self.driver.implicitly_wait(10)
        self.enter_micro_program()

    def enter_micr_program(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.9)
        self.driver.find_element(By.XPATH, "//*[@text='抽奖']").click()
        time.sleep(20)

    def test_search_webview(self):
        # Handles = self.driver.window handles# print(Handles)
        print(self.driver.contexts)
        # print(self.driver.current_context)self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand")
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")
        for window in self.driver.window_handlers:
            self.driver.switch_to.window(window)
            print(self.driver.title)

if __name__ == '__main__':
    a = TestWXMicroView()
    a.setup