from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self, file_name, encoding='utf-8'):
        super().__init__()
        self.read(file_name, encoding=encoding)
        self.file_name = file_name
        self.encoding = encoding

    def write_data(self, select, option, value):
        """往配置文件中写入数据"""
        self.set(select, option, value)
        self.write(fp=open(self.file_name, "w", encoding=self.encoding))


if __name__ == '__main__':
    res = Config("test.ini")
    ponse = res.get('file', 'name')
    print(ponse)
