import pytest
import os
from testCases.test_user import TestUser
from commons.log_utils import get_log

if __name__ == '__main__':
    pytest.main()

    # 调用系统指令生成allure报告
    # os.system("allure generate ./temps -o ./report --clean")

# if __name__ == '__main__':
#     t = TestUser()
#     re = t.test_getUserInfo()
#     print(re.json())
