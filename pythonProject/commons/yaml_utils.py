import os
import yaml


# 读、写、清空yaml文件，用于读、写、清空全局变量

class YamlUtils:
    # 获取yaml文件的路径,当前路径的上一级路径+文件名

    # testCase文件夹下执行用这个路径
    # path = os.path.dirname(os.getcwd()) + "/extract.yaml"
    # main.py文件执行用这个路径
    path = os.getcwd() + "/extract.yaml"

    def read_yaml(self):
        with open(YamlUtils.path, encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def write_yaml(self, data):
        with open(YamlUtils.path, encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clear_yaml(self):
        with open(YamlUtils.path, encoding="utf-8", mode="w") as f:
            f.truncate()


# if __name__ == '__main__':
#     t = YamlUtils()
#     t.write_yaml({"age": 12})
#     print(t.read_yaml())
#     t.clear_yaml()
