# coding = UFT-8
from appium import webdriver
import time
import random
import os


# 从外部txt文件获取公众号账号值
values = []
with open('/Users/weiyi/pythonProject1/appiumWechat/data.txt', 'r') as f:
    for line in f:
        values.append(list(line.strip('\n').split(',')))
# print(values)


desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "10"
desired_caps["deviceName"] = "OnePlus 8"
desired_caps["appPackage"] = "com.tencent.mm"
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps['newCommandTimeout'] = "99999"
desired_caps['noReset'] = True
desired_caps['fullReset'] = False

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(3)

# 点击通讯录按钮
os.system('adb shell input tap 417 2260')

# 点击公众号按钮
id_class2 = 'resourceId("com.tencent.mm:id/a3c").className("android.widget.LinearLayout")'
driver.find_element_by_android_uiautomator(id_class2).click()
time.sleep(4)

count = 0  # 计数器
for value in values:
    #点击"添加"按钮
    driver.implicitly_wait(10)
    time.sleep(10)
    #os.system('adb shell input tap 1010 167')
    driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="添加"]').click()
    time.sleep(3)
    driver.implicitly_wait(10)

    el4 = driver.find_element_by_id("com.tencent.mm:id/bhn")
    el4.send_keys(value)
    time.sleep(3)

    #点击键盘的搜索按钮
    driver.keyevent(66)
    driver.press_keycode(66)
    time.sleep(10)

    try:
        if driver.find_element_by_xpath('//*[@text="公众号"]').text == '公众号':
            # 点击搜索的第一个结果
            os.system('adb shell input tap 798 513')
            wechatName = driver.find_element_by_id("com.tencent.mm:id/a4k").text

            # 点击关注按钮
            time.sleep(5)
            os.system('adb shell input tap 548 634')
            time.sleep(5)

            #点击三个返回按钮回到"添加页面"再次循环
            driver.find_element_by_id("com.tencent.mm:id/rs").click()
            driver.implicitly_wait(10)
            time.sleep(5)

            os.system('adb shell input tap 30 165')
            driver.implicitly_wait(10)
            time.sleep(5)

            os.system('adb shell input tap 34 168')
            driver.implicitly_wait(10)

            count += 1
            print("{} {} {} {}".format(wechatName, value, count, "succeed"))

            sleepTime=random.randrange(30,120,8)
            time.sleep(sleepTime)


    except Exception as e:
            count += 1
            print("{} {} {} {}".format("搜索不到结果",value,count,"fail"))
            os.system('adb shell input tap 34 168')
            driver.implicitly_wait(10)

            sleepTime=random.randrange(30,60)
            time.sleep(sleepTime)

print('\n'"All task finished:",count)
driver.close_app()