import requests
import hashlib
import base64
import time
import random
import re


# ============ 签名函数 ============
SIGN_KEY = "A013F70DB97834C0A5492378BD76C53A"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"


def generate_sign(method="GET", timestamp=None, channel_id=40009, s_version=2):
    """
    生成猫眼票房接口的 signKey 签名
    返回签名以及需要拼到 query 里的相关字段
    """
    timestamp = timestamp if timestamp else int(time.time() * 1000)
    index = random.randint(1, 1000)
    user_agent_b64 = base64.b64encode(USER_AGENT.encode('utf-8')).decode('utf-8')
    
    # 顺序必须和 JS 代码一致
    o = {
        "method": method,
        "timeStamp": timestamp,
        "User-Agent": user_agent_b64,
        "index": index,
        "channelId": channel_id,
        "sVersion": s_version,
        "key": SIGN_KEY,
    }
    
    # 拼接成 &k=v&k=v 的字符串,去掉开头的 &
    parts = []
    for k, v in o.items():
        if v == 0 or v:
            parts.append(f"&{k}={v}")
        else:
            parts.append(f"&{k}=''")
    d = "".join(parts)[1:]
    d = re.sub(r'\s+', ' ', d)
    
    sign = hashlib.md5(d.encode('utf-8')).hexdigest()
    
    return {
        "signKey": sign,
        "timeStamp": timestamp,
        "index": index,
        "channelId": channel_id,
        "sVersion": s_version,
        "User-Agent": user_agent_b64,
    }


# ============ 请求 ============
cookies = {
    '_lxsdk_cuid': '19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8',
    'uuid': '19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8',
    '_lxsdk': '19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8',
    '_lxsdk_s': '19df09d7082-80d-019-1d4%7C%7C14',
    '_lx_utm': 'utm_source%3Dbing%26utm_medium%3Dorganic',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'm-appkey': 'fe_com.sankuai.movie.fe.ipro',
    'm-traceid': '8724469486950254016',
    'mygsig': '{"m1":"0.0.3","m2":0,"m3":"0.0.67_tool","ms1":"2b5339f853637e51604f30fe1ae9b050","ts":1777858539596,"ts1":1777858539572}',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://piaofang.maoyan.com/dashboard',
    'sec-ch-ua': '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'uid': 'fd567d896d9f03395a89569e150c1f00ef5ea865',
    'user-agent': USER_AGENT,
}

# 调用签名函数,动态生成签名相关字段
sign_data = generate_sign(method="GET")

params = {
    'orderType': '0',
    'uuid': '19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8',
    'timeStamp': sign_data["timeStamp"],
    'User-Agent': sign_data["User-Agent"],
    'index': sign_data["index"],
    'channelId': sign_data["channelId"],
    'sVersion': sign_data["sVersion"],
    'signKey': sign_data["signKey"],
    'WuKongReady': 'h5',
}

print("签名信息:")
print(f"  timeStamp: {sign_data['timeStamp']}")
print(f"  index:     {sign_data['index']}")
print(f"  signKey:   {sign_data['signKey']}")
print()

response = requests.get(
    'https://piaofang.maoyan.com/i/api/dashboard-ajax',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(f"HTTP 状态码: {response.status_code}")
print(f"响应内容:\n{response.text[:1000]}")