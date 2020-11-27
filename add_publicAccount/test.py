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
import requests
import time

'''
url = 'http://api.nbd.com.cn/3/user/cancel_account'
para = {
        'app_key': 'd401a38c50a567882cd71cec43201c78',
        'client_key': 'iPhone',
        "access_token": "46b5620f0fd3db400d0923a7888f3155"
        }

r = requests.post(url, json=para)
print(r.status_code)
print(r.json())
'''

# 获取验证码
app_key_ios = 'd401a38c50a567882cd71cec43201c78'
uuid_ios = 'ed3b0d597c664b138ec72612b7dc2728'

app_key_android = 'ae1bd0a8b32505a86c0b20187f5093ec'
uuid_android = '37A5AAD522B7900C8CD364162AD5E1BC'

app_version = '6.2.4'
opt = 'password_reset'
time_stamp = time.time()

phone_no = '17602894576'

url = 'http://api.nbd.com.cn/3/specials/sms_captcha'
para = {
        'app_key': app_key_android,
        'app_version_name': app_version,
        'opt': opt,
        'phone_no': phone_no,
        'timestamp': time_stamp,
        'uuid': uuid_android
        }

r = requests.get(url,para)
print(r.status_code)
print(r.json())