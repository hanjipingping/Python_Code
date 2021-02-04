
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):

    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding=encoding)
        self.filename = filename
        self.encoding = encoding

    def write_data(self, select, option, value):
        """往配置文件中写入数据"""
        self.set(select, option, value)
        self.write(fp=open(self.filename, "w", encoding=self.encoding))


# 创建一个配置文件解析器
conf = Config(os.path.join(CONF_DIR, "config.ini"))
