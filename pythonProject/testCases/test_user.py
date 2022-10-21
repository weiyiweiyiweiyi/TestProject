import pytest
import requests

from commons.yaml_utils import YamlUtils
from commons.request_utils import RequestUtils
import time
import os

class TestUser:

    # 定义全局变量
    app_token = ""

    # 获取配置文件的通用参数作为全局变量
    # config_file = os.path.dirname(os.getcwd()) + "/config/config.yaml"  # 本文件内执行路径
    config_file = os.getcwd() + "/config/config.yaml"  # main函数内执行路径
    yaml_utils = YamlUtils()
    config_vale = yaml_utils.read_yaml(config_file)

    base_url = config_vale["base_params"]["base_url"]
    app_key = config_vale["base_params"]["base_app_key"]
    app_version_name = config_vale["base_params"]["base_app_version_name"]
    uuid = config_vale["base_params"]["base_uuid"]
    timeStamp = int(time.time())

    # 用户登录成功获取用户信息:1.登录; 2.验证token; 3.获取用户信息
    def test_getUserInfo(self):
        # 获取该测试用例的路径及数据
        test_file_name = TestUser.config_vale["test_data_name"]["TestUser_test_getUserInfo"]
        #test_file = os.path.dirname(os.getcwd()) + "/testData/" + test_file_name  # 本文件内执行路径
        test_file = os.getcwd() + "/testData/" + test_file_name  # main函路径数内执行
        test = YamlUtils()
        test_data = test.read_yaml(test_file)

        path_pwd_login = test_data["path_pwd_login"]
        path_auth_by_token = test_data["path_auth_by_token"]
        path_user_info = test_data["path_user_info"]
        password = test_data["password"]
        tel = test_data["tel"]


        # 1.登录
        # 读取yaml文件的获取请求参数值
        url_pwd_login = TestUser.base_url + path_pwd_login
        method_pwd_login = "post"
        data_pwd_login = {
            "app_key": TestUser.app_key,
            "app_version_name": TestUser.app_version_name,
            "timestamp": TestUser.timeStamp,
            "uuid": TestUser.uuid,
            "password": password,
            "tel": tel
        }

        # 调用统一请求接口获取响应
        request = RequestUtils()
        res_pwd_login = request.test_sendRequest(method=method_pwd_login, url=url_pwd_login, data=data_pwd_login)

        # 响应里的token赋值给全局变量
        TestUser.app_token = res_pwd_login.json()["data"]["access_token"]

        # 2.验证token
        url_auth_by_token = TestUser.base_url + path_auth_by_token
        method_auth_by_token = "post"
        data_auth_by_token = {
            "user_token": TestUser.app_token,
            "timestamp": TestUser.timeStamp
        }

        # 调用统一请求接口获取响应
        res_auth_by_token = request.test_sendRequest(url=url_auth_by_token, method=method_auth_by_token,
                                                     data=data_auth_by_token)
        # 断言
        assert res_auth_by_token.json()["status_code"] == 1

        # 3.获取用户信息
        url_user_info = TestUser.base_url + path_user_info
        method_user_info = "get"
        data_user_info = {
            "app_key": TestUser.app_key,
            "app_version_name": TestUser.app_version_name,
            "timestamp": TestUser.timeStamp,
            "uuid": TestUser.uuid,
            "app_token": TestUser.app_token
        }
        res_user_info = request.test_sendRequest(method=method_user_info, url=url_user_info, params=data_user_info)

        # 断言
        assert res_user_info.json()["status_code"] == 1

        return res_user_info


if __name__ == '__main__':
    t = TestUser()
    re = t.test_getUserInfo()
    print(re.json())
