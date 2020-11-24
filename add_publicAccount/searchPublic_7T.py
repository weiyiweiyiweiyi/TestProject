#根据微信id搜索得到对应的微信账号的名称

#coding = UFT-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import sys


#从外部txt文件获取公众号账号值
values=[]
with open('/Users/weiyi/pythonProject1/appiumWechat/data.txt','r') as f:
 for line in f:
    values.append(list(line.strip('\n').split(',')))
#print(values)


desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="10"
desired_caps["deviceName"]="OnePlus7T"
desired_caps["appPackage"]="com.tencent.mm"
desired_caps["appActivity"]="com.tencent.mm.ui.LauncherUI"
desired_caps['noReset'] = True
desired_caps['fullReset'] = False

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

time.sleep(3)

el1 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
el1.click()

el2 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
el2.click()
time.sleep(4)

count=0  #计数器

for value in values:
    
    #进入到搜索公众号界面，点击添加按钮
    driver.implicitly_wait(10)
    #el3 = driver.find_element_by_xpath('//android.support.v7.widget.LinearLayoutCompat/android.widget.LinearLayout[2]')
    #el3.click()

    el3 = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="添加"]')
    el3.click()

    driver.implicitly_wait(10)

    #输入公众号的值，调出系统键盘点击搜索
    el4 = driver.find_element_by_id("com.tencent.mm:id/ji")
    el4.send_keys(value)
    driver.implicitly_wait(10)

    driver.keyevent(66)
    driver.press_keycode(66)
    driver.implicitly_wait(10)

    souce = driver.page_source

    if driver.find_element_by_xpath('//*[@text="公众号"]').text in souce:
        # 点击搜索结果的头像部分进入关注页面
        TouchAction(driver).press(x=116, y=461).release().perform()
        driver.implicitly_wait(10)

        wechatName = driver.find_element_by_id("com.tencent.mm:id/awq").text
        print(wechatName)

        el7 = driver.find_element_by_accessibility_id("返回")
        el7.click()
        driver.implicitly_wait(10)

        el8 = driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/jf"]')
        el8.click()
        driver.implicitly_wait(10)

driver.close_app()