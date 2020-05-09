from appium import webdriver
import time

'''
启动单个应用
'''

#创建字典
desired_caps=dict()
#平台的名字（android or ios）
desired_caps['platformName']='android'
#平台的系统版本
desired_caps['platformVersion']='5'
#设备的名字
desired_caps['deviceName']='androidDevice'
#要打开的应用程序
desired_caps['appPackage']='cn.com.nbd.nbdmobile'
#要打开的界面
desired_caps['appActivity']='.activity.MainActivity'
desired_caps['noReset']='True'

#获取driver对象调用相应的方法，发送给移动设备
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

time.sleep(5)

#退出
driver.quit()