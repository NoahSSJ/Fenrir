from http.cookies import SimpleCookie
import json
import os
from pathlib import Path
from pprint import pprint
import re
from dotenv import load_dotenv
from .api import XhsApi

class XhsUtils():
    def __init__(self):
        pass

    @staticmethod
    def get_headers():
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.xiaohongshu.com/user/profile/68f441e2000000003700733e?xsec_token=AB43Iw6UkZyiAVGm6jhFmDNbCyqQfVQj4wtQUQ8rtdMvY=&xsec_source=pc_like',
            'sec-ch-ua': '"Chromium";v="147", "Not-A.Brand";v="24", "Microsoft Edge";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
        }
        return headers
    
    @staticmethod
    def get_cookies():
        auth_path = Path(__file__).parent.parent.parent / "config" / "auth" / "cookies" / ".env.xhs"
        load_dotenv(auth_path)
        cookie_str = os.getenv('XHS_COOKIES')
        print("cookie_str:", cookie_str)
        cookie = SimpleCookie(cookie_str)
        cookie_dict = {k: v.value for k, v in cookie.items()}
        pprint(cookie_dict)
        return cookie_dict

    @staticmethod
    def get_post(session, url):
        headers = XhsUtils.get_headers()
        # headers['cookie'] = XhsUtils.get_cookies()
        response = session.get(url=url, headers=headers)
        json_str = re.findall(r'window\.__INITIAL_STATE__\s*=\s*([\s\S]*?)</script>', response.text)[0]
        # pprint(res)
        json_dict = json.loads(json_str)
        pprint(json_dict)

        

