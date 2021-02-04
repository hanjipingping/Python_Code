
# import random
#
# import requests
# from jsonpath import jsonpath
#
# from common.handle_config import conf
# from common.handle_db import db
# from tools.handle_sign import HandleSign
#
#
# def random_phone():
#     """随机生成一个未注册手机号"""
#     while True:
#         phone = "131"
#         for i in range(8):
#             i = random.randint(0, 9)
#             phone += str(i)
#         # 判断改手机号是否已注册
#         sql = "SELECT * FROM futureloan.member WHERE mobile_phone={}".format(phone)
#         res = db.find_data(sql)
#         if not res:
#             return phone
#
#
# def register(user_conf, pwd_conf, type=1):
#     """注册,保存到配置文件"""
#     url = conf.get("env", "base_url") + "/member/register"
#     params = {"mobile_phone": random_phone(),
#               "pwd": "12345678",
#               "type": type,
#               }
#     headers = eval(conf.get("env", "headers"))
#     requests.request(url=url, method="post", json=params, headers=headers)
#     mobile = str(params["mobile_phone"])
#     pwd = str(params["pwd"])
#     # 保存到配置文件
#     conf.write_data("test_data", user_conf, mobile)
#     conf.write_data("test_data", pwd_conf, pwd)
#     return mobile, pwd
#
#
# def login(mobile, pwd):
#     """登录"""
#     login_url = conf.get("env", "base_url") + "/member/login"
#     login_params = {"mobile_phone": mobile,
#                     "pwd": pwd}
#     headers = eval(conf.get("env", "headers"))
#     response = requests.request(url=login_url, method="post", json=login_params, headers=headers)
#     res = response.json()
#     # 提取token
#     token_value = jsonpath(res, "$..token")[0]
#     token = "Bearer" + " " + token_value
#     # 提取用户id
#     member_id = jsonpath(res, "$..id")[0]
#     return token, member_id, token_value
#
#
# def recharge(token, member_id, token_value, money=500000):
#     """充值"""
#     headers = eval(conf.get("env", "headers"))
#     headers["Authorization"] = token
#     recharge_url = conf.get("env", "base_url") + "/member/recharge"
#     recharge_params = {"member_id": member_id,
#                        "amount": money}
#     # ---------v3-----------
#     # 根据token生成加密的sign
#     cryto_info = HandleSign.generate_sign(token_value)
#     recharge_params.update(cryto_info)
#
#     requests.request(url=recharge_url, method="post", json=recharge_params, headers=headers)
#
#
# def init_env_data():
#     # 注册普通用户（借款人），保存到配置文件
#     user_info = register(user_conf="mobile", pwd_conf="pwd")
#     # 注册普通用户（投资人），保存到配置文件
#     user2 = register(user_conf="invest_mobile", pwd_conf="invest_pwd")
#     # 注册管理员，保存到配置文件
#     register(user_conf="admin_mobile", pwd_conf="admin_pwd", type=0)
#
#     # (借款人)登录获取用户id
#     token, member_id, token_value = login(*user_info)
#     # 给用户充值
#     recharge(token, member_id, token_value)
#     recharge(token, member_id, token_value)
#
#     # (投资人)登录获取用户id
#     token2, member_id2, token_value2 = login(*user2)
#     # 给用户充值
#     recharge(token2, member_id2, token_value2)
#     recharge(token2, member_id2, token_value2)
