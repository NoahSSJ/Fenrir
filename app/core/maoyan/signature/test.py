import hashlib
import base64
import re

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
SIGN_KEY = "A013F70DB97834C0A5492378BD76C53A"

ua_b64 = base64.b64encode(USER_AGENT.encode('utf-8')).decode('utf-8')
print(f"UA base64: {ua_b64}")
print(f"curl 里的: TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0Ny4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xNDcuMC4wLjA=")
print(f"UA 是否一致: {ua_b64 == 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0Ny4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xNDcuMC4wLjA='}")
print()

o = {
    "method": "GET",
    "timeStamp": 1777858538942,
    "User-Agent": ua_b64,
    "index": 378,
    "channelId": 40009,
    "sVersion": 2,
    "key": SIGN_KEY,
}

parts = []
for k, v in o.items():
    if v == 0 or v:
        parts.append(f"&{k}={v}")
    else:
        parts.append(f"&{k}=''")
d = "".join(parts)[1:]
d = re.sub(r'\s+', ' ', d)

print(f"待签名字符串:\n{d}\n")

sign = hashlib.md5(d.encode('utf-8')).hexdigest()
print(f"算出来的签名: {sign}")
print(f"目标签名:     31ed45b17bd07eca46b2fcb1dc2b8710")
print(f"是否匹配:     {sign == '31ed45b17bd07eca46b2fcb1dc2b8710'}")