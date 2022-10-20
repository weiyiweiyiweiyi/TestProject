# 用户模块接口
import pytest
import requests


class TestUserApi:
    access_token = ""

    # 用户登录
    @pytest.mark.smoke
    def test_login(self):
        url = "http://apiv2.nbd.com.cn/login/pwd_login"
        data = {
            "app_key": "d401a38c50a567882cd71cec43201c78",
            "app_version_name": "7.0.3",
            "timestamp": "1665295014",
            "uuid": "ed3b0d597c664b138ec72612b7dc2728",
            "password": "nbd123456",
            "tel": "17602894576"
        }

        res = requests.post(url=url, data=data)
        TestUserApi.access_token = res.json()["data"]["access_token"]
        assert res.json()["status_code"] == 1
        return res

    # 验证用户身份
    def test_verifyUserToken(self):
        url = "http://apiv2.nbd.com.cn/user_auth/auth_by_token"
        data = {
            "user_token": TestUserApi.access_token,
            "timestamp": "1665295014"
        }

        res = requests.post(url=url, data=data)
        assert res.json()["status_code"] == 1
        return res

    # 获取用户信息
    def test_getUserInfo(self):
        url = "http://apiv2.nbd.com.cn/users/user_info.json"
        data = {
            "app_key": "d401a38c50a567882cd71cec43201c78",
            "app_version_name": "7.0.3",
            "timestamp": "1665295014",
            "uuid": "ed3b0d597c664b138ec72612b7dc2728",
            "app_token": TestUserApi.access_token
        }
        res = requests.get(url=url, params=data)
        assert res.json()["status_code"] == 1
        return res


# if __name__ == '__main__':
#     t = TestUserApi()
#     t.test_login()
#     print(t.access_token)
#     print(t.test_getUserInfo().request.url)
