import requests


# 请求接口统一封装方法

class RequestUtils:
    # 获取全局的会话对象
    sess = requests.session()

    def test_sendRequest(self, method, url, **kwargs):
        # 会话对象调用请求接口的方法，保持同一个会话不中断
        res = RequestUtils.sess.request(method, url, **kwargs)
        # 打印session值
        # print(RequestUtils.sess)
        return res


# if __name__ == '__main__':
#     data = {
#         "app_key": "d401a38c50a567882cd71cec43201c78",
#         "app_version_name": "7.0.4",
#         "timestamp": "1665295014",
#         "uuid": "ed3b0d597c664b138ec72612b7dc2728",
#         "password": "nbd123456",
#         "tel": "17602894576"
#     }
#     t = RequestUtils()
#     r = t.test_sendRequest(method="post", url="http://apiv2.nbd.com.cn/login/pwd_login", data=data)
#     print(r.json())


# if __name__ == '__main__':
#     url = "http://apiv2.nbd.com.cn/users/user_info.json"
#     data = {
#         "app_key": "d401a38c50a567882cd71cec43201c78",
#         "app_version_name": "7.0.3",
#         "timestamp": "1665295014",
#         "uuid": "ed3b0d597c664b138ec72612b7dc2728",
#         "app_token": "NjoxNjM5MDM5MDg3OjE2NjU5Mzk5NTQ6VGxNTks3eEQxeg=="
#     }
#     t = RequestUtils()
#     r = t.test_sendRequest(method="get", url=url, params=data)
#     print(r.json())