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
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
# caps["appActivity"] = ".plugin.appbrand.ui.AppBrandUI"
caps["noReset"] = "true"
caps["automationname"] = "uiautomatorl"
caps["ensureWebviewsHavePages"] = True

# 启动会话
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

# 等待一段时间或执行其他操作
driver.implicitly_wait(10)
# # 先点击搜索
el1 = driver.find_element(By.ID, 'com.tencent.mm:id/h5n')
el1.click()
driver.hide_keyboard()  # 隐藏键盘
driver.implicitly_wait(1)

# 输入
el2 = driver.find_element(By.ID, 'com.tencent.mm:id/d98')
key_word = '大众点评'
el2.send_keys(key_word)
el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tencent.mm:id/odf"]')
el3.click()
time.sleep(2)
# el4 = driver.find_element(By.ID, 'com.android.systemui:id/notification_stack_scroller')
# el4.click()

