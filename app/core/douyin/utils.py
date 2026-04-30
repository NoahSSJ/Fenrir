
from pathlib import Path
from pprint import pprint
import random
import re
import time
# from warnings import deprecated

import execjs
import urllib
from .api import DouYinApi


class DouYinUtils():
        
        @staticmethod
        def get_sec_uid(url: str) -> str:
            return url.split('/')[4].split('?')[0]
        
        @staticmethod
        def get_modal_id(url: str) -> str:
            if "modal_id=" not in url:
                raise ValueError("URL 中没有找到 modal_id")
            modal_id = url.split("modal_id=")[1].split("&")[0]
            return modal_id
        
        @staticmethod
        def clean_string(s: str) -> str:
            s = s.replace('\n', '').replace('\r', '').replace('\t', '').replace('\\', '/').strip().replace('//', '/').replace('//', '/').replace('//', '/').replace('<', '').replace('>', '').replace(':', '').replace('"', '').replace('|', '').replace('?', '').replace('*', '')
            return s

        @staticmethod
        def get_a_bogus(params):
            open_args = "/aweme/v1/web/comment/list/reply/?" + urllib.parse.urlencode(params)
            js_path = Path(__file__).parent / "signature" / "a_bogus.js"
            with open(js_path, mode="r", encoding="utf-8") as f:
                js_code = f.read()
            ctx = execjs.compile(js_code)
            a_bogus = ctx.call("get_ab", open_args)
            params['a_bogus'] = a_bogus
            return params
            # pprint(params)1323

        @staticmethod
        def get_fp():
            chars = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            timestamp = format(int(time.time() * 1000), 'x')
            r = [None] * 36
            r[8] = r[13] = r[18] = r[23] = "_"
            r[14] = "4"
            for o in range(36):
                if not r[o]:
                    i = int(random.random() * len(chars))
                    r[o] = chars[3 & i | 8] if o == 19 else chars[i]
            
            return "verify_" + timestamp + "_" + "".join(r)
        
        @staticmethod
        def get_all_open_api(session):
            api, params = DouYinApi.get_open_api()
            response = session.get(url=api, params=params)
            pprint(response.json())

        @staticmethod
        def get_get_social_count(session):
            api, params = DouYinApi.get_social_count()
            params = Utils.get_a_bogus(params)
            response = session.get(url=api, params=params)
            json_dict = response.json()
            # pprint(response.json())
            # live_num = json_dict['notice_count'][0]['group']
        
        @staticmethod
        # @deprecated("get_ms_token", "无效函数")
        def get_ms_token(session):
            api, params, data = DouYinApi.get_ms_token()
            response = session.post(url=api, params=params, data=data)
            # pprint(response.headers)
            ms_token = response.headers['X-Ms-Token']
            # print(ms_token)
            # print(len(ms_token))
            return ms_token
        
        @staticmethod
        def get_aweme_count(session, url: str):
            sec_uid = DouYinUtils.get_sec_uid(url)
            api, params = DouYinApi.get_user(sec_uid)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.douyin.com/user/MS4wLjABAAAAARd_zguz0GWEiQ2xMRxfaTg9Ur2qCb_K1lggv0mRqcboJYAZElny9j8XxpJdf62I?enter_from=general_search&from_tab_name=main',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            }
            response = session.get(url=api, headers=headers, params=params)
            # pprint(response.text)
            awemeCount = re.findall(r'\\"awemeCount\\":(.*?),', response.text)[1]
            # print(awemeCount)
            return awemeCount
        

        @staticmethod
        # @property
        def get_user_info(session):
            api, params = DouYinApi.get_user_info()
            response = session.get(url=api, params=params)
            json_dict = response.json()
            pprint(json_dict)
            create_time = json_dict['create_time']
            create_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(create_time)))
            last_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(json_dict['last_time'])))
            webid = json_dict['id']
            user_uid = json_dict['user_uid']
            print(webid, user_uid, create_time_str, last_time_str)
            return webid, user_uid, create_time_str, last_time_str
        