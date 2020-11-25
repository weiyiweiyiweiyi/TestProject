# coding = UFT-8
import pandas as pd
import selenium
import urllib3
from appium import webdriver
import time
import random
import os
import xlrd
from xlutils.copy import copy


# 读取本地excel文件的公众号id的值：指定行和列获取特定的一列值返回一个列表，行和列与excel的序号一致
def read_fromExcel(excelName, sheetName, row, column):
    file = pd.read_excel(excelName, sheet_name=sheetName)
    row_new = row - 2
    column_new = column - 1
    columnList = file[file.columns[column_new]]  # 获取某列的所有值的列表
    columnList_new = columnList[row_new:]  # 获取上述列表的第n个元素直到末尾，组成新的列表
    return columnList_new


# 将list列表里的元素依次同行不同列写入excel，多次调用该方法追加不覆盖原有内容
def write_toExcel(excelName, sheetName, valueList):
    # 打开需要操作的excel表
    wb = xlrd.open_workbook(excelName,formatting_info=True)
    # 复制原有表
    wb_new = copy(wb)
    # 获取原有excel表中需要写入的sheet
    sheet_new = wb_new.get_sheet(sheetName)
    # k表示该sheet的最后一行
    k = len(sheet_new.rows)
    # 向原有sheet后面新增数据
    for i in range(len(valueList)):
        sheet_new.write(k, i, valueList[i])
    # 保存为原有的excel表路径
    wb_new.save(excelName)


# 输入多个元素组成列表list
def construct_list(*value):  # 参数为可变参数，即参数的个数不确定
    list_new = []
    for i in value:
        list_new.append(i)

    return list_new


# 判断页面是否存在元素：存在返回true，不存在返回false
def is_element_exist(self, elementText):
    source = self.driver.page_source
    print(source)
    if elementText in source:
        return True
    else:
        return False


count = 0  # 计数

# 读取excel信息
read_excelFile = "/Users/weiyi/Desktop/上海上市公司信息表.xlsx"
read_excelSheet = "微信号(智慧2)"
read_excelRow = 960
read_excelColumn = 7

# 写入excel信息
write_excelFile = "/Users/weiyi/Desktop/test1.xlsx"
write_excelSheet = "Sheet1_sz"

# 关闭并清除已打开的微信进程和终端进程
os.system('adb -s b27b6578 shell am force-stop com.tencent.mm')
os.system('adb -s b27b6578 shell am force-stop jackpal.androidterm')
time.sleep(5)

# 获取待搜索id的列表
publicIds = read_fromExcel(read_excelFile, read_excelSheet, read_excelRow, read_excelColumn)
time.sleep(2)

desired_caps = {"platformName": "Android", "platformVersion": "10", "deviceName": "oneplus1",
                "udid": "b27b6578", "appPackage": "com.tencent.mm", "appActivity": "com.tencent.mm.ui.LauncherUI",
                'newCommandTimeout': "10000", 'noReset': True, 'fullReset': False}
time.sleep(2)

driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)
time.sleep(3)

try:
    # 点击通讯录按钮
    os.system('adb -s b27b6578 shell input tap 417 2260')
    time.sleep(2)

    # 点击公众号按钮
    id_class = 'resourceId("com.tencent.mm:id/a3c").className("android.widget.LinearLayout")'
    driver.find_element_by_android_uiautomator(id_class).click()
    time.sleep(2)

    for value in publicIds:  # 获取搜索id
        # 点击"添加"按钮
        time.sleep(3)
        #driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="添加"]').click()
        os.system('adb -s b27b6578 shell input tap 997 170')
        time.sleep(3)

        # 给输入框传值
        driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys(value)
        time.sleep(3)

        # 点击键盘的搜索按钮
        driver.keyevent(66)
        driver.press_keycode(66)
        time.sleep(8)

        # 判断是否存在搜索结果
        source = driver.page_source
        if "没有更多的搜索结果" in source:
            if "公众号" in source:
                # 点击搜索的第一个结果
                os.system('adb -s b27b6578 shell input tap 798 513')
                time.sleep(5)

                # 判断是否可关注，即判断是否已关注过该公众号，已关注则返回页面进行下一个循环
                source = driver.page_source
                if "不再关注" in source:
                    publicName = driver.find_element_by_id("com.tencent.mm:id/a4k").text
                    time.sleep(3)

                    os.system('adb -s b27b6578 shell input tap 30 165')
                    time.sleep(5)

                    os.system('adb -s b27b6578 shell input tap 34 168')
                    time.sleep(5)

                    count += 1
                    # 将结果写入excel并且在控制台打印出来
                    write_toExcel(write_excelFile, write_excelSheet,construct_list(publicName, value, count, "succeed(concerned)"))
                    print("{} {} {} {}".format(publicName, value, count, "succeed(concerned)"))
                elif "关注公众号" in source:
                    # 点击关注按钮
                    wechatName = driver.find_element_by_id("com.tencent.mm:id/a4k").text
                    time.sleep(3)
                    os.system('adb -s b27b6578 shell input tap 548 634')
                    time.sleep(5)

                    # 判断是否能关注该公众号，不能则跳出页面，否则关注，打印对应信息
                    source = driver.page_source
                    if "操作过于频繁，请稍后再试。" in source:
                        print("操作过于频繁，请稍后再试")
                        time.sleep(3)
                        break
                    else:
                        # 成功关注后，点击三个返回按钮回到"添加页面"再次循环
                        driver.find_element_by_id("com.tencent.mm:id/rs").click()
                        time.sleep(5)

                        os.system('adb -s b27b6578 shell input tap 30 165')
                        time.sleep(5)

                        os.system('adb -s b27b6578 shell input tap 34 168')

                        count += 1
                        # 将结果写入excel并且在控制台打印出来
                        write_toExcel(write_excelFile, write_excelSheet,construct_list(wechatName, value, count, "succeed"))
                        print("{} {} {} {}".format(wechatName, value, count, "succeed"))

                        # 停留随机的时间后再次循环搜索添加
                        sleepTime = random.randrange(20, 30)
                        time.sleep(sleepTime)
            else:
                count += 1
                # 将结果写入excel并且在控制台打印出来
                write_toExcel(write_excelFile, write_excelSheet,construct_list("搜索不到结果", value, count, "fail"))
                print("{} {} {} {}".format("搜索不到结果", value, count, "fail"))
                # 返回上一个页面再次循环
                os.system('adb -s b27b6578 shell input tap 34 168')
                sleepTime = random.randrange(5, 10)
                time.sleep(sleepTime)
        else:
            # 点击搜索的第一个结果
            os.system('adb -s b27b6578 shell input tap 798 513')

            # 判断是否可关注，即判断是否已关注过该公众号，已关注则返回页面进行下一个循环
            source = driver.page_source
            if "不再关注" in source:
                publicName = driver.find_element_by_id("com.tencent.mm:id/a4k").text

                os.system('adb -s b27b6578 shell input tap 30 165')
                time.sleep(5)

                os.system('adb -s b27b6578 shell input tap 34 168')
                time.sleep(5)

                count += 1
                # 将结果写入excel并且在控制台打印出来
                write_toExcel(write_excelFile, write_excelSheet,construct_list(publicName, value, count, "succeed(concerned)"))
                print("{} {} {} {}".format(publicName, value, count, "succeed(concerned)"))

            elif "关注公众号" in source:
                # 点击关注按钮
                wechatName = driver.find_element_by_id("com.tencent.mm:id/a4k").text
                time.sleep(5)
                os.system('adb -s b27b6578 shell input tap 548 634')
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
                    time.sleep(5)

                    os.system('adb -s b27b6578 shell input tap 30 165')
                    time.sleep(5)

                    os.system('adb -s b27b6578 shell input tap 34 168')

                    count += 1
                    # 将结果写入excel并且在控制台打印出来
                    write_toExcel(write_excelFile, write_excelSheet,construct_list(wechatName, value, count, "succeed"))
                    print("{} {} {} {}".format(wechatName, value, count, "succeed"))

                    # 停留随机的时间后再次循环搜索添加
                    sleepTime = random.randrange(20, 30)
                    time.sleep(sleepTime)

except ConnectionResetError as e:
    print('exception:', e)
except urllib3.exceptions.ProtocolError as e:
    print('exception:', e)
except selenium.common.exceptions.NoSuchElementException as e:
    print('exception:', e)
finally:
    print('\n'"All task finished:", count)
    driver.close_app()
