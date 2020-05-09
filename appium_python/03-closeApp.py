from appium import webdriver
import time

'''
1.driver.close_app() //关闭应用
2.driver.quit() //关闭driver驱动对象
'''

desired=dict()
desired['platformName']='Android'
desired['platformVersion']='7'
desired['deviceName']='androidDevice'
desired['appPackage']='cn.com.nbd.nbdmobile'
desired['appActivity']='.activity.MainActivity'


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired)
time.sleep(3)
#关闭应用
driver.close_app()

#打开其他的app
driver.start_activity('com.taobao.taobao','com.taobao.tao.TBMainActivity')
time.sleep(3)
print(driver.current_package)
print(driver.current_activity)
driver.close_app()

#关闭driver驱动对象
driver.quit()