from appium import webdriver
import time

'''
1.定位一个元素
2.定位一组元素
'''

#创建字典
desired_caps=dict()
#平台的名字（android or ios）
desired_caps['platformName']='android'
#平台的系统版本
desired_caps['platformVersion']='7'
#设备的名字
desired_caps['deviceName']='androidDevice'
#要打开的应用程序
desired_caps['appPackage']='cn.com.nbd.nbdmobile'
#要打开的界面，此处必须是app打开的第一个activity，否则会报权限错误
desired_caps['appActivity']='.activity.SplashActivity'
#不清除app里的原有的数据，即第二次以后打开app不是第一次打开的状态（含有欢迎页）
desired_caps['noReset']='True'
#获取driver对象调用相应的方法，发送给移动设备
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)

#定位一个元素
driver.find_element_by_id("cn.com.nbd.nbdmobile:id/logo_title_search_icon").click()
time.sleep(10)
#driver.find_element_by_class_name("android.widget.EditText").send_keys("经济")
#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView").click()


#定位一组元素
textViews=driver.find_elements_by_id("cn.com.nbd.nbdmobile:id/public_column_item_text")
#for textView in textViews:
#    print(textView.text)
   
textViews[3].click()
time.sleep(10)

#退出
driver.quit()