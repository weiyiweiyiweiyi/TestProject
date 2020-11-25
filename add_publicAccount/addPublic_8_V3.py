# coding = UFT-8
from appium import webdriver
import time
import random
import os


count = 0  # 计数器

# 从外部txt文件获取公众号账号值
values = []
with open('/Users/weiyi/pythonProject1/appiumWechat/data.txt', 'r') as f:
    for line in f:
        values.append(list(line.strip('\n').split(',')))

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
time.sleep(5)

# 点击通讯录按钮
os.system('adb shell input tap 417 2260')

# 点击公众号按钮
id_class = 'resourceId("com.tencent.mm:id/a3c").className("android.widget.LinearLayout")'
driver.find_element_by_android_uiautomator(id_class).click()

for value in values:
    # 点击"添加"按钮
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="添加"]').click()
    time.sleep(3)
    driver.implicitly_wait(10)

    # 给输入框传值
    driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys(value)
    time.sleep(3)

    # 点击键盘的搜索按钮
    driver.keyevent(66)
    driver.press_keycode(66)
    time.sleep(10)

    # 判断是否存在搜索结果
    source = driver.page_source
    if "没有更多的搜索结果" in source:
        if "公众号" in source:
            # 点击搜索的第一个结果
            os.system('adb shell input tap 798 513')
            wechatName = driver.find_element_by_id("com.tencent.mm:id/a4k").text

            # 点击关注按钮
            time.sleep(5)
            os.system('adb shell input tap 548 634')
            time.sleep(5)

            # 判断是否能关注该公众号，不能则跳出页面，否则关注，打印对应信息
            source=driver.page_source
            if "操作过于频繁，请稍后再试。" in source:
                print("操作过于频繁，请稍后再试")
                time.sleep(5)
                break
            else:
                # 成功关注后，点击三个返回按钮回到"添加页面"再次循环
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

                # 停留随机的时间后再次循环搜索添加
                sleepTime = random.randrange(40, 110)
                time.sleep(sleepTime)
        else:
            count += 1
            print("{} {} {} {}".format("搜索不到结果",value,count,"fail"))
            # 返回上一个页面再次循环
            os.system('adb shell input tap 34 168')
            sleepTime=random.randrange(30,60)
            time.sleep(sleepTime)
    elif "公众号" in source:
        # 点击搜索的第一个结果
        os.system('adb shell input tap 798 513')
        wechatName = driver.find_element_by_id("com.tencent.mm:id/a4k").text

        # 点击关注按钮
        time.sleep(5)
        os.system('adb shell input tap 548 634')
        time.sleep(5)

        # 判断是否能关注该公众号，不能则跳出页面，否则关注，打印对应信息
        source = driver.page_source
        if "操作过于频繁，请稍后再试。" in source:
            print("操作过于频繁，请稍后再试")
            time.sleep(5)
            break
        else:
            # 成功关注后，点击三个返回按钮回到"添加页面"再次循环
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

            # 停留随机的时间后再次循环搜索添加
            sleepTime = random.randrange(40, 110)
            time.sleep(sleepTime)

print('\n'"All task finished:",count)
driver.close_app()