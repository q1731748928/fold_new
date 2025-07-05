import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sympy.plotting.intervalmath import interval

# 配置Desired Capabilities
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "9B141FFAZ00F06"
caps["appPackage"] = "com.dianping.v1"
caps["appActivity"] = ".NovaMainActivity"
caps["noReset"] = "true"
caps["automationname"] = "uiautomatorl"
caps["ensureWebviewsHavePages"] = True

# 启动会话
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

# 等待一段时间或执行其他操作
driver.implicitly_wait(10)
# 定义点击的目标
el1 = driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@content-desc="搜索"]/android.view.View')
el1.click()
# # 点击输入框，清空，并输入
el2 = driver.find_element(By.ID, 'com.dianping.v1:id/search_keyword_edit')
el2.clear()
el2.send_keys('老碗会')
el3 = driver.find_element(By.ID, 'com.dianping.v1:id/tv_search')
el3.click()
# # 获取屏幕尺寸
screen_size = driver.get_window_size()
screen_width = screen_size['width']
screen_height = screen_size['height']
print("screen_width:", screen_width)
print("screen_height:", screen_height)
end_x = screen_width  # 水平位置保持不变
end_y = screen_height - 100  # 向上滑动 100px
#
start_x = screen_width * 0.5
start_y = screen_height * 0.8
end_y = screen_height * 0.2
for _ in range(10):
    driver.swipe(int(start_x), int(start_y), int(start_x), int(end_y), 1000)
    time.sleep(1)
# while True:
#     pass
# time.sleep(1)
# el3 = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.jd.lib.search.feature:id/ab5"]')
# el3.click()
# time.sleep(2)
# 关闭会话
# driver.quit()

# adb shell dumpsys window | grep mCurrentFocus
