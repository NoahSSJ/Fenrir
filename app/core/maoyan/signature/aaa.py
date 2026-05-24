import requests

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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
    # 'cookie': '_lxsdk_cuid=19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8; uuid=19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8; _lxsdk=19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8; _lxsdk_s=19df09d7082-80d-019-1d4%7C%7C14; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic',
}

params = {
    'orderType': '0',
    'uuid': '19d49b61f10c8-0918b2735d039d-4c657b58-280000-19d49b61f10c8',
    'timeStamp': '1777858538942',
    'User-Agent': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0Ny4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xNDcuMC4wLjA=',
    'index': '378',
    'channelId': '40009',
    'sVersion': '2',
    'signKey': '31ed45b17bd07eca46b2fcb1dc2b8710',
    'WuKongReady': 'h5',
}

response = requests.get('https://piaofang.maoyan.com/i/api/dashboard-ajax', params=params, cookies=cookies, headers=headers)
print(response.json())