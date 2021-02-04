import requests
import os
import unittest
import pytest
from common.handle_config import conf
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
from common import myddt
from common.handle_log import log
from common.handle_data import replace_data

file_path = os.path.join(DATA_DIR, "cases.xlsx")
import pytest


# @pytest.mark.usefixtures("login_class",'login_01')

@pytest.mark.han  # 标记用例，用于调节测试
class TestLogin:
    excel = Excel(file_path, "login")
    cases = excel.read_data()

    @pytest.mark.parametrize("item", cases)
    def test_login(self, item):

        url = conf.get("env", "base_url") + item["url"]
        # 请求头
        headers = eval(conf.get("env", "headers"))
        # 请求参数
        item["data"] = replace_data(item["data"], TestLogin)
        params = eval(item["data"])
        # 预取结果
        expected = eval(item["expected"])
        # 请求方法
        method = item["method"]
        # 第二步：调用接口，获取实际结果
        response = requests.request(method, url=url, json=params, headers=headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", response.text)
        # 第三步：断言
        try:
            assert expected["code"] == res["code"]
            assert expected["msg"]== res["msg"]
        except AssertionError as e:
            log.error("用例{}，执行未通过".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例{}，执行通过".format(item["title"]))

    def test_01(self):
        assert 1 == 100
