from request import http
#使用人人打码，需要自己注册付费使用
def game_captcha(gt: str, challenge: str):
    rep = http.post(
        url="http://api.rrocr.com/api/recognize.html",
        data={
            "appkey": "",
            "gt": gt,
            "challenge": challenge,
            "referer": "https://api-takumi.mihoyo.com/event/luna/sign"
        }
    ).json()
    return rep["data"]["validate"]

def bbs_captcha(gt: str, challenge: str):
    rep = http.post(
        url="http://api.rrocr.com/api/recognize.html",
        data={
            "appkey": "",
            "gt": gt,
            "challenge": challenge,
            "referer": "https://bbs-api.miyoushe.com/apihub/app/api/signIn"
        }
    ).json()
    return rep["data"]["validate"]
