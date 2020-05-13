from appium import webdriver
import time

'''
将app置于后台一段时间再回到前台
'''
desire=dict()
desire['platformName']='android'
desire['platformVersion']='7'
desire['deviceName']='androidDevice'
desire['appPackage']='cn.com.nbd.nbdmobile'
desire['appActivity']='.activity.SplashActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desire)
time.sleep(2)

#将app置于后台一段时间再回到前台
driver.background_app(2)

time.sleep(2)
driver.quit()
