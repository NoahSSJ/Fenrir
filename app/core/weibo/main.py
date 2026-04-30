from http.cookies import SimpleCookie
import json
import os
import random
import re
from curl_cffi import requests
from pprint import pprint
import time

from api import WeiBoApi
from annotation import MinIOClient, RedisClient
from dotenv import load_dotenv

load_dotenv()
class WeiBoSpider():
    session = requests.Session()
    cookie_str = os.getenv('MY_COOKIES')
    cookie = SimpleCookie(cookie_str)
    cookie_dict = {k: v.value for k, v in cookie.items()}
    session.cookies.update(cookie_dict)
    session.headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'client-version': '3.0.0',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://weibo.com/n/%E4%BA%BA%E9%97%B4%E5%86%B7%E6%9A%96Lens',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2026.03.23.1',
    'traceparent': '00-4cc0416e9dfd906afe8625924178b8c0-1834183052c77b23-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'rCoTzCVtsubEfnG7iWZJZVFc',
    # 'cookie': '',
}
    session.proxies = {
        # 'http': 'http://127.0.0.1:7890',
        # 'https': 'http://127.0.0.1:7890',
    }
    def __init__(self):
        pass

    class MediaSpider():
        def __init__(self):
           pass

        @staticmethod
        def producer(url, r: RedisClient):
            page = 1
            uid = WeiBoSpider.Utils.get_uid(url=url)
            while True:
                params = {
                    'uid': f'{uid}',
                    'page': f'{page}',
                    'feature': '0',
                }
                response = WeiBoSpider.session.get('https://weibo.com/ajax/statuses/mymblog', params=params)
                # pprint(response.json())
                for i in response.json()['data']['list']:
                    text = i['text']
                    id = i['id']
                    if r.r.sismember('wbibo:media:feed', f"{id}:{text}"):
                        continue
                    task = json.dumps({
                        'id': id,
                        'text': text,
                        'uid': uid,
                    })
                    r.r.lpush(f'{os.getenv("REDIS_TASK_PREFIX")}:{uid}', task)
                break

        @staticmethod
        def consumer(r: RedisClient, url: str, type: str, mode: str,**kwargs):
            uid = WeiBoSpider.Utils.get_uid(url=url)
            task_key = f"{os.getenv('REDIS_TASK_PREFIX')}:{uid}"
            task_cnt = 1
            while True:
                task = r.r.lpop(task_key)
                if not task:
                    break
                task = json.loads(task)
                pprint(task)
                if type == 'cmt':
                    match mode:
                        case 'one':
                            WeiBoSpider.MediaSpider.get_cmt(url=url, quantity='one')
                        case 'some':
                            WeiBoSpider.MediaSpider.get_cmt(url=url, quantity='some')
                        case 'all':
                            WeiBoSpider.MediaSpider.get_cmt(url=url, quantity='all')
                        case 'specify':
                            WeiBoSpider.MediaSpider.get_cmt(url=url, quantity='specify')  
                if type == 'media':
                    match mode:
                        case 'one':
                            WeiBoSpider.MediaSpider.get_media(url=url, quantity='one')
                        case 'some':
                            WeiBoSpider.MediaSpider.get_media(url=url, quantity='some')
                        case 'all':
                            WeiBoSpider.MediaSpider.get_media(url=url, quantity='all')
                        case 'specify':
                            WeiBoSpider.MediaSpider.get_media(url=url, quantity='specify')  
                task_cnt += 1


        @staticmethod 
        def get_media(url, quantity, mode, download:MinIOClient):
            page = 1
            uid, _ = WeiBoSpider.Utils.get_info(url=url)
            while True:
                params = {
                    'uid': f'{uid}',
                    'page': f'{page}',
                    'feature': '0',
                }

                response = WeiBoSpider.session.get('https://weibo.com/ajax/statuses/mymblog', params=params)
                # pprint(response.json())
                for i in response.json()['data']['list']:
                    # text = i['text']
                    id = i['id']
                    name = i['user']['screen_name']
                    text = (lambda x: matches[0] if (matches := re.findall("(.*?)<br /><br />", x)) else x)(i['text'])
                    print(id, text)
                    text='123'
                    pic_infos = i.get('pic_infos')
                    if pic_infos:

                        print("---")
                        for i, j in pic_infos.items():
                            print(f"序号:{i}")
                            url = j["original"]["url"]
                            
                            pic_content = WeiBoSpider.session.get(url).content
                            with open(save_url:=f"{uid}_{text}_{i}.jpg", mode='wb') as f:
                                f.write(pic_content)
                            # if isinstance(download, MinIOClient):
                            #     download.upload_file(name, save_url, save_url)
                    elif mix_media_info := i.get('mix_media_info'):
                        # pprint(mix_media_info)
                        for i, j in mix_media_info['items'].items():
                            url = j['data']['original']['url'] if j['data'].get('original', {}) else j['data']['media_info']['mp4_hd_url']
                            print(url)
                            response = WeiBoSpider.session.get(url, stream=True)
                            with open(save_url:=f"{uid}_{text}_{i}.mp4", mode='wb') as f:
                                for chunk in response.iter_content(chunk_size=8192):
                                    if chunk:  # 过滤掉保持活动的新块
                                        f.write(chunk)
                    else:
                        pass
                    if quantity == "one":
                        return
                    time.sleep(random.uniform(1, 3))
                if quantity == "some":
                    return
                

        @staticmethod
        def get_cmt(url, quantity):
            is_first = True
            cnt = 0
            uid, statuses_count = WeiBoSpider.Utils.get_info(url=url)
            while True:
                api, params = WeiBoApi.get_cmt('5276386847621761', uid, is_first)
                response = WeiBoSpider.session.get(api, params=params)
                # pprint(response.json())
                max_id = response.json()['max_id']
                for i in response.json()['data']:
                    text = i['text'].split('<')[0]
                    id = i['user']['id']
                    scree_name = i['user']['screen_name']
                    cnt += 1
                    print(cnt, id, scree_name, text)
                    if quantity == "one":
                        return
                is_first = False
                if cnt == quantity:
                    return
                if quantity == "some":
                    return
                if max_id == 0:
                    break


    class Utils():

        @staticmethod
        def get_uid(url):
            if url.split('/')[-2] == 'n':
                return url.split('/')[-1], True 
            else:
                return url.split('/')[-1], False
            
        @staticmethod
        def get_cmt_id(url):
            pass
 
        @staticmethod
        def get_info(url):
                uid, is_n = WeiBoSpider.Utils.get_uid(url=url)
                api, params = WeiBoApi.get_info(uid, is_n)
                # print(api, params)
                response = WeiBoSpider.session.get(api, params=params, impersonate="chrome124")

                # pprint(response.json())
                description = response.json()['data']['user'].get('description', '')
                followers_count = response.json()['data']['user']['followers_count']
                followers_count_str = response.json()['data']['user']['followers_count_str']
                friends_count = response.json()['data']['user']['friends_count']
                gender = response.json()['data']['user']['gender']
                id = response.json()['data']['user']['id']
                id_str = response.json()['data']['user']['idstr']
                location = response.json()['data']['user']['location']
                statuses_count = response.json()['data']['user']['statuses_count']
                print(statuses_count)
                return id, statuses_count
        
        @staticmethod
        def get_following(url):
            uid = WeiBoSpider.Utils.get_uid(url=url)
            api, params = WeiBoApi.get_following(uid)
            response = WeiBoSpider.session.get(url=api, params=params)
            # pprint(response.json())
            bloggers = response.json()['data']['follows']['users']
            for i in bloggers:
                id = i['id']
                followers_count = i['followers_count']
                followers_count_str = i['followers_count_str']
                location = i['location']
                name = i['name']
                print(id, followers_count, followers_count_str, location, name)


if __name__ == "__main__":
    print(type(MinIOClient))
    print(isinstance("a", str))
    # WeiBoSpider.MediaSpider.get_media(r'https://weibo.com/n/人间冷暖Lens', mode="one", download="local")
    WeiBoSpider.MediaSpider.get_cmt(r'https://weibo.com/n/人间冷暖Lens', quantity="one")