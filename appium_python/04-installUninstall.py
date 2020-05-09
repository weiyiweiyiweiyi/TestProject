from appium import webdriver

'''
1.判断app是否存在
2.存在则卸载该app
3.不存在则安装该app
'''
desire=dict()
desire['platformName']='android'
desire['platformVersion']='7'
desire['deviceName']='androidDevice'
desire['appPackage']='com.taobao.taobao'
desire['appActivity']='com.taobao.tao.TBMainActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desire)

if driver.is_app_installed('cn.com.nbd.nbdmobile'):
    driver.remove_app('cn.com.nbd.nbdmobile')  #卸载app
else:
    driver.install_app('/Users/weiyi/Downloads/app-nbd-release.apk')  #安装app

driver.quit()
