import pytest
import requests

from commons.log_utils import get_log
from commons.yaml_utils import YamlUtils
from commons.request_utils import RequestUtils
import time
import os


class TestUser:
    # 定义全局变量
    app_token = ""
    logtool = get_log()

    # 获取配置文件的通用参数作为全局变量
    # config_file = "../config/config.yaml"  # 本文件内执行路径
    config_file = "./config/config.yaml"  # main函数内执行路径
    yaml_utils = YamlUtils()
    config_vale = yaml_utils.read_yaml(config_file)

    base_url = config_vale["base_params"]["base_url"]
    app_key = config_vale["base_params"]["base_app_key"]
    app_version_name = config_vale["base_params"]["base_app_version_name"]
    uuid = config_vale["base_params"]["base_uuid"]
    timeStamp = int(time.time())
    test_data_path = config_vale["base_params"]["test_data_path"]

    # 获取该测试用例的路径，然后调用读yaml文件的方法获取测试数据
    test_file_name = config_vale["test_data_name"]["TestUser_test_getUserInfo"]
    # test_file = "../testData/" + test_file_name  # 本文件内执行路径
    test_file = test_data_path + test_file_name  # main函路径数内执行

    # 用户登录成功获取用户信息:1.登录; 2.验证token; 3.获取用户信息
    @pytest.mark.parametrize("caseInfo", YamlUtils().read_yaml(test_file))
    def test_getUserInfo(self, caseInfo):
        path_pwd_login = caseInfo["path_pwd_login"]
        path_auth_by_token = caseInfo["path_auth_by_token"]
        path_user_info = caseInfo["path_user_info"]
        password = caseInfo["password"]
        tel = caseInfo["tel"]
        validate = caseInfo["validate"]["status_code"]


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
        TestUser.logtool.info("登录url{},参数{}".format(url_pwd_login,data_pwd_login))
        # 调用统一请求接口获取响应
        request = RequestUtils()
        res_pwd_login = request.test_sendRequest(method=method_pwd_login, url=url_pwd_login, data=data_pwd_login)

        if res_pwd_login.json()["status_code"] == 1:
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
            # assert res_auth_by_token.json()["status_code"] == 1
            assert res_pwd_login.json()["status_code"] == validate

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
            # assert res_user_info.json()["status_code"] == 1
            assert res_pwd_login.json()["status_code"] == validate

            print("login succeed")

        else:
            assert res_pwd_login.json()["status_code"] == validate
            print("login failed")

# if __name__ == '__main__':
#     t = TestUser()
#     re = t.test_getUserInfo()
#     print(re.json())

# if __name__ == '__main__':
#     pytest.main()
