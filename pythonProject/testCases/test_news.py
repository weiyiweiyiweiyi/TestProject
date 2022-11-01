# 新闻模块接口

import requests


class TestNews:
    def test_homeArticle(self):
        url = "http://apiv2.nbd.com.cn/article_lists/home_news_header_v2.json"
        data = {
            "app_key": "d401a38c50a567882cd71cec43201c78",
            "app_version_name": "7.0.3",
            "timestamp": "1665295014",
            "uuid": "ed3b0d597c664b138ec72612b7dc2728",
            "count": "15",
        }

        res = requests.get(url=url, params=data)
        return res


if __name__ == '__main__':
    t = TestNews()
    print(t.test_homeArticle().json())
