

from common.handle_config import conf
import re



def replace_data(data, cls):
    """替换用例参数"""
    while re.search("#(.+?)#", data):
        item = re.search("#(.+?)#", data)
        # 需要替换的数据
        rep_data = item.group()
        # 要替换的属性
        key = item.group(1)
        try:
            value = conf.get("test_data", key)
        except:
            value = getattr(cls, key)
        data = data.replace(rep_data, str(value))
    return data

