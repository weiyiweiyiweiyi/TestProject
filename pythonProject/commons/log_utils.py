# 日志信息方法：日志器、处理器、格式器

import logging

def get_log():
    # 日志器：存放日志信息
    test_logger = logging.getLogger()  # 创建日志器对象
    test_logger.setLevel(logging.INFO)  # 设置级别，高于该级别的才显示

    # 处理器： 指定日志显示的位置，控制台or文件
    sh = logging.StreamHandler()  # 创建处理器控制台对象
    fh = logging.FileHandler("./log.txt", encoding="utf-8")  # 创建处理器文件对象

    # 格式器： 日志信息格式化显示
    # 创建格式器对象及设置显示格式
    test_formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")

    sh.setFormatter(test_formatter) # 将设置的格式赋给处理器对象
    test_logger.addHandler(sh)  # 将日志信息打印到控制台

    # fh.setFormatter(test_formatter) # 将设置的格式赋给处理器对象
    # test_logger.addHandler(fh)  # 将日志信息打印到文件

    return test_logger

def a():
    b = 1
    return b


# test_logger.debug("1")
# test_logger.info("2")
# test_logger.warning("3")
# test_logger.error("4")
# test_logger.critical("5")

if __name__ == '__main__':
    logtool.debug('12313')
    logtool.warning('qeeqe')
    logtool.error('12313213')
    logtool.critical('11321313')
