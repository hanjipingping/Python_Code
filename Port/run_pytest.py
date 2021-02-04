import pytest
import os
import time

pytest.main(["--alluredir=report"])

print('运行完成')

os.system("allure serve allure_report")
