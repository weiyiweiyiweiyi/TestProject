from commons.yaml_utils import YamlUtils
import time
from commons.request_utils import RequestUtils
import pytest


class TestUser:
    app_token = ""

    # 用户登录成功获取用户信息:
    # 1.登录; 2.验证token; 3.获取用户信息

    def test_getUserInfo(self):
        # 1.登录
        # 读取yaml文件的获取请求参数值
        readyaml = YamlUtils()
        para_value = readyaml.read_yaml()

        url = para_value["url"]
        method = para_value["method"]
        data = {
            "app_key": para_value["data"]["app_key"],
            "app_version_name": para_value["data"]["app_version_name"],
            "timestamp": int(time.time()),
            "uuid": para_value["data"]["uuid"],
            "password": para_value["data"]["password"],
            "tel": para_value["data"]["tel"]
        }

        # 调用统一请求接口获取响应
        request = RequestUtils()
        res_pwd_login = request.test_sendRequest(method=method, url=url, data=data)

        # 响应里的token赋值给全局变量
        TestUser.app_token = res_pwd_login.json()["data"]["access_token"]

        # 2.验证token
        url_auth_by_token = para_value["url_auth_by_token"]
        method_auth_by_token = para_value["method_auth_by_token"]
        data_auth_by_token = {
            "user_token": TestUser.app_token,
            "timestamp": int(time.time())
        }

        # 调用统一请求接口获取响应
        res_auth_by_token = request.test_sendRequest(method=method_auth_by_token, url=url_auth_by_token,
                                                     data=data_auth_by_token)
        # 断言
        assert res_auth_by_token.json()["status_code"] == 1

        # 3.获取用户信息
        method_user_info = "get"
        url_user_info = "http://apiv2.nbd.com.cn/users/user_info.json"
        data_user_info = {
            "app_key": para_value["data"]["app_key"],
            "app_version_name": para_value["data"]["app_version_name"],
            "timestamp": int(time.time()),
            "uuid": para_value["data"]["uuid"],
            "app_token": TestUser.app_token
        }
        res_user_info = request.test_sendRequest(method=method_user_info, url=url_user_info, params=data_user_info)

        #断言
        assert res_user_info.json()["status_code"] == 1

        return res_user_info

if __name__ == '__main__':
    t = TestUser()
    re = t.test_getUserInfo()
    print(re.json())

