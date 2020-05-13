from appium import webdriver
import time

'''
1.打开一个app的同时打开跳转到其他的app
2.获取当前app的包名和界面名
'''

desired=dict()
desired['platformName']='Android'
desired['platformVersion']='7'
desired['deviceName']='androidDevice'
desired['appPackage']='cn.com.nbd.nbdmobile'
desired['appActivity']='.activity.SplashActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired)
time.sleep(3)
#获取当前app的包名和界面名
print(driver.current_package)
print(driver.current_activity)

#打开其他的app
driver.start_activity('com.taobao.taobao','com.taobao.tao.TBMainActivity')
time.sleep(3)
#获取当前app的包名和界面名
print(driver.current_package)
print(driver.current_activity)

driver.quit()