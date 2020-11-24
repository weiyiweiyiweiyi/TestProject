
#coding = UFT-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import sys
import os

#从外部txt文件获取公众号账号值
values=[]
with open('/Users/weiyi/pythonProject1/appiumWechat/data.txt','r') as f:
 for line in f:
    values.append(list(line.strip('\n').split(',')))
#print(values)


desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="10"
desired_caps["deviceName"]="OnePlus 8"
desired_caps["appPackage"]="com.tencent.mm"
desired_caps["appActivity"]="com.tencent.mm.ui.LauncherUI"
desired_caps['noReset'] = True
desired_caps['fullReset'] = False

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

time.sleep(3)

#点击通讯录按钮
#el1 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
#el1.click()
#id_class1 = 'resourceId("com.tencent.mm:id/cnh").className("android.widget.ImageView")'
#driver.find_element_by_android_uiautomator(id_class1).click()
os.system('adb shell input tap 417 2260')

#点击公众号按钮
id_class2 = 'resourceId("com.tencent.mm:id/a3c").className("android.widget.LinearLayout")'
driver.find_element_by_android_uiautomator(id_class2).click()
time.sleep(4)

count=0  #计数器

for value in values:
    
    #进入到搜索公众号界面，点击添加按钮
    driver.implicitly_wait(10)
    #el3 = driver.find_element_by_xpath('//android.support.v7.widget.LinearLayoutCompat/android.widget.LinearLayout[2]')
    #el3.click()
    el3 = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="添加"]')
    el3.click()

    driver.implicitly_wait(10)

    #输入公众号的值，调出系统键盘点击搜索
    #el4 = driver.find_element_by_id("com.tencent.mm:id/ji")
    el4 = driver.find_element_by_id("com.tencent.mm:id/bhn")
    el4.send_keys(value)
    time.sleep(3)

    driver.keyevent(66)
    driver.press_keycode(66)
    time.sleep(5)

    souce = driver.page_source
    time.sleep(5)

    try:
        if driver.find_element_by_xpath('//*[@text="公众号"]').text in souce:
            # 点击搜索结果的头像部分进入关注页面
            #TouchAction(driver).press(x=0.435, y=0.223).release().perform()
            #driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/a4h"]').click()
            time.sleep(5)
            os.system('adb shell input tap 798 513')
            time.sleep(5)

            #获取微信账号名称
            wechatName = driver.find_element_by_id("com.tencent.mm:id/a4k").text
            #print(wechatName)

            # 点击关注公众号按钮
            #id_class = 'resourceId("com.tencent.mm:id/a16").className("android.widget.TextView")'
            #driver.find_element_by_android_uiautomator(id_class).click()

            #driver.find_element_by_id("com.tencent.mm:id/a16").click()
            #TouchAction(driver).press(x=692, y=680).release().perform()
            #e = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="当前所在页面,戈壁创投"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView')
            #e.click()
            #driver.find_element_by_accessibility_id("关注公众号").click()
            #driver.tap([(425,647), (655,709)], 100)
            #TouchAction(driver).press(x=677, y=680).move_to(x=737, y=683).release().perform()
            #TouchAction(driver).tap(x=95, y=740).perform()
            #TouchAction(driver).press(x=95, y=740).release().perform()
            #driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/a16"]').click()
            os.system('adb shell input tap 548 634')
            driver.implicitly_wait(10)

            # 连续点击3个返回到公众号列表页面便于再次添加
            el7 = driver.find_element_by_accessibility_id("返回")
            el7.click()
            driver.implicitly_wait(10)

            driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/dn"]').click()
            driver.implicitly_wait(10)

            driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/dn"]').click()
            driver.implicitly_wait(10)

            count += 1

            print("{} {} {} {}".format(wechatName,value,count,"succeed"))

    except Exception as e:
        count += 1
        time.sleep(1)

        print("{} {} {} {}".format("无数据",value,count,"fail"))

        el7 = driver.find_element_by_accessibility_id("返回")
        el7.click()
        driver.implicitly_wait(10)

print('\n'"All task finished:",count)
driver.close_app()