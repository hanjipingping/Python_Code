from threading import Timer
import requests
import random
import time



# 获取金山词霸每日一句英文和翻译
def get_news():
    url = "http://open.iciba.com/dsapi/"
    res = requests.get(url)
    content = res.json()['content']
    note = res.json()['note']
    translation = res.json()['translation']
    translation = translation.replace('小编的话', '进击物语')
    return content, note, translation


# 文本类型消息
def send_msg_txt(content):
    headers = {"Content-Type": "text/plain"}
    send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=326467ee-e7b2-4ef3-bb98-bf794780a444"
    send_data = {
        "msgtype": "text",  # 消息类型，此时固定为text
        "text": {
            "content": content  # 文本内容，最长不超过2048个字节，必须是utf8编码
        }
    }

    requests.post(url=send_url, headers=headers, json=send_data)


def send_job():
    contents = get_news()

    for text in contents:
        rand_sec = random.randint(1, 5)  # 利用随机数让前后消息发送的时间产生延时
        time.sleep(rand_sec)
        # 打印下发送内容
        print("当前时间：%s，消息内容：%s" % (time.ctime(), text))
        send_msg_txt(text)


send_job()