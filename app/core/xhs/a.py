import json
from pprint import pprint
import requests
import re

cookies = {
    'abRequestId': '35b100b5-d7f7-5fa6-af52-82151e849f72',
    'a1': '19b27173470jmu4jdf8cosnqayhhnh35dqf85zqmf50000136404',
    'webId': 'a74a82425c063518a289a4f4b44203b0',
    'gid': 'yjDJWyW4qyfJyjDJWyWq4AuAW8V674VfiYSli6iMIA0vxY28xIxq22888yqK4848DyY2iWdq',
    'xsecappid': 'xhs-pc-web',
    'web_session': '040069b0de1d7812247f78e6863b4bdcbd0ab2',
    'id_token': 'VjEAACPon4rxw3cosz5L6Oi4/P2uwJBaBmrOVgvRCGvZ4tDRvyUtwv3mSAc6dLiUt+OXyXrtZXtgZOFWoYfkh1/QN2u4y+eAljz5OukZZMQA1qOAqX7vInyiVg3JStPCX+ajQquo',
    'ets': '1774769071108',
    'acw_tc': '0a00dcc017772108054613674e3c21a7f68d99891a063f1351ef27608699db',
    'webBuild': '6.7.4',
    'websectiga': '7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4',
    'sec_poison_id': '6655b633-368f-427e-b81d-1e276e9b9388',
    'loadts': '1777212312021',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
    # 'cookie': 'abRequestId=35b100b5-d7f7-5fa6-af52-82151e849f72; a1=19b27173470jmu4jdf8cosnqayhhnh35dqf85zqmf50000136404; webId=a74a82425c063518a289a4f4b44203b0; gid=yjDJWyW4qyfJyjDJWyWq4AuAW8V674VfiYSli6iMIA0vxY28xIxq22888yqK4848DyY2iWdq; xsecappid=xhs-pc-web; web_session=040069b0de1d7812247f78e6863b4bdcbd0ab2; id_token=VjEAACPon4rxw3cosz5L6Oi4/P2uwJBaBmrOVgvRCGvZ4tDRvyUtwv3mSAc6dLiUt+OXyXrtZXtgZOFWoYfkh1/QN2u4y+eAljz5OukZZMQA1qOAqX7vInyiVg3JStPCX+ajQquo; ets=1774769071108; acw_tc=0a00dcc017772108054613674e3c21a7f68d99891a063f1351ef27608699db; webBuild=6.7.4; websectiga=7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4; sec_poison_id=6655b633-368f-427e-b81d-1e276e9b9388; loadts=1777212312021',
}

response = requests.get(
    'https://www.xiaohongshu.com/user/profile/57a036536a6a693c92af5a14?xsec_token=ABp_9ri_0rd9b-DSAGk9C1Hbz2Sqq7TiV0gHSlz0leM1c=&xsec_source=pc_search',
    cookies=cookies,
    headers=headers,
)

# print(response.text)
res_list = re.findall(r'window\.__INITIAL_STATE__\s*=\s*([\s\S]*?)</script>', response.text)
if res_list:
    res = res_list[0]
    # 清理JSON字符串，移除可能的末尾分号
    res = res.rstrip(';')
    # 将undefined替换为null
    res = res.replace('undefined', 'null')
    try:
        data = json.loads(res)
        pprint(data)
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        # 打印出错位置附近的内容进行调试
        error_pos = e.pos
        start = max(0, error_pos - 50)
        end = min(len(res), error_pos + 50)
        print(f"出错位置附近的内容: {res[start:end]}")
else:
    print("未找到window.__INITIAL_STATE__")