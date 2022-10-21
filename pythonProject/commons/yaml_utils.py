import os
import yaml


# 读、写、清空yaml文件，用于读、写、清空全局变量

class YamlUtils:

    def read_yaml(self, file):
        with open(file, encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def write_yaml(self, write_data,file):
        with open(file, encoding="utf-8", mode="a") as f:
            yaml.dump(write_data, stream=f, allow_unicode=True)

    def clear_yaml(self,file):
        with open(file, encoding="utf-8", mode="w") as f:
            f.truncate()

# if __name__ == '__main__':
#
#     # 获取通用数据文件
#     config_file = os.path.dirname(os.getcwd()) + "/config/config.yaml"
#     print(config_file)
#     t = YamlUtils()
#     value = t.read_yaml(config_file)
#
#     # 获取测试数据文件名
#     # print(value["test_data_name"]["TestUser_test_getUserInfo"])
#
#     # 获取测试数据文件
#     testData_path = os.path.dirname(os.getcwd()) + "/testData/"
#     testData_file= testData_path + value["test_data_name"]["TestUser_test_getUserInfo"]
#     print(testData_file)
#
#     value = t.read_yaml(testData_file)
#     print(value)