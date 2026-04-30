from http.cookies import SimpleCookie
import re
from urllib.parse import unquote
import execjs
import requests
from pprint import pprint
import urllib
from .items import CommentItem, FollowingsItem
from dotenv import load_dotenv
import os
import json
from requests.utils import cookiejar_from_dict
import time
import random
from bs4 import BeautifulSoup
import csv
# from typing import deprecated
from pathlib import Path
from .api import DouYinApi
from .utils import DouYinUtils
from mods.interceptors import RequestInterceptor

auth_path = Path(__file__).parent.parent.parent / "config" / "auth" / "cookies" / ".env.douyin"
load_dotenv(auth_path)
class DouYinSpider():
    session = requests.Session()
    cookie_str = os.getenv("DOUYIN_COOKIES")
    # print(cookie_str)
    cookie = SimpleCookie()
    cookie.load(cookie_str.replace("douyin.com;", "").replace("IsDouyinActive=true;", ""))
    # print(cookie)
    cookie_dict = {k: v.value for k, v in cookie.items()}
    # pprint(cookie_dict) 
    session.cookies.update(cookie_dict)
    # session.cookies.update(cookie_dict)
    session.headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://www.douyin.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
}
    session.proxies = {
        # 'http': 'http://127.0.0.1:7890',
        # 'https': 'http://127.0.0.1:7890',
    }

    def __init__(self):
        pass

    class MediaSpider():

        @staticmethod
        def producer(url: str, r=None):
            sec_uid = DouYinUtils.get_sec_uid(url)
            api, params = DouYinApi.get_post(sec_uid)
            params = params.copy()
            # pprint(params)
            page = 1
            while True:
                response = DouYinSpider.session.get(url=api, params=params)
                # print(response.text)
                json_dict = response.json()
                # pprint(json_dict)
                for k, v in enumerate(json_dict['aweme_list'], 1):
                    aweme_id = v['aweme_id']
                    # if r.r.sismember(f'{DY_REDIS_DOWNLOAD_SET}:{sec_uid}', aweme_id):
                    #     break
                    nickname = v['author']['nickname']
                    desc = v['desc']
                    url =  f"https://www.douyin.com/user/self?from_tab_name=main&modal_id={aweme_id}&showTab=like",
                    suid = sec_uid
                    
                    if v.get('video'):
                        # 安全获取视频地址，遇到空值自动跳过
                        bit_rate = v['video'].get('bit_rate')
                        if not bit_rate:
                            print("该视频无播放地址，跳过")
                            continue  # 跳过，不崩
                        download_video_url = bit_rate[0]['play_addr']['url_list'][0]
                        print(aweme_id, nickname, desc, url, suid, download_video_url)
                    elif v.get('image'):
                        
                        download_image_list = [img['url_list'][0] for img in v['images']]
                        print(aweme_id, nickname, desc, url, suid, download_image_list)
                    else:
                       print("目前只支持纯视频和图片合集")
                    # print(k, aweme_id, nickname, desc, url, suid, download_video_url)
                    # task = json.dumps({
                    #     'aweme_id': aweme_id,
                    #     'nickname': nickname,
                    #     'desc': desc,
                    #     'url': url,
                    #     'suid': suid,
                    #     'download_video_url': download_video_url,
                    #     'download_image_list': download_image_list,
                    # })
                    # yield
                    # r.r.lpush(f'{DY_REDIS_TASK_PREFIX}:{sec_uid}', task)
                if page % 3 == 0:
                    time.sleep(random.uniform(3, 9))
                time.sleep(random.uniform(1, 3))
                if page == 3:
                    return
                page += 1
                if json_dict['has_more'] == 0:
                    return
                params['max_cursor'] = json_dict['max_cursor']

        @staticmethod
        def consumer(url: str, r, type, mode):
            suid = DouYinUtils.get_sec_uid(url)
            task_key = f"{os.getenv('DY_REDIS_TASK_PREFIX')}:{suid}"
            task_cnt = 1
            while True:
                task = r.r.rpop(task_key)
                if task is None:
                    break
                task = json.loads(task)
                pprint(task)
                if type == 'media':
                    match mode:
                        case 'one': 
                            DouYinSpider.MediaSpider.get_media(url=task['url'], quantity='one')
                        case 'some':
                            DouYinSpider.MediaSpider.get_media(url=task['url'], quantity='some')
                        case 'all':
                            DouYinSpider.MediaSpider.get_media(url=task['url'], quantity='all')
                        case 'specify':
                             DouYinSpider.MediaSpider.get_media(url=task['url'], quantity='specify')  
                elif type == 'cmt':
                    match mode:
                        case 'one':
                            DouYinSpider.MediaSpider.get_cmt(url=task['url'], quantity='one')
                        case 'some':
                            DouYinSpider.MediaSpider.get_cmt(url=task['url'], quantity='some')       
                        case 'all':
                            DouYinSpider.MediaSpider.get_cmt(url=task['url'], quantity='all')   
                        case 'specify':
                            DouYinSpider.MediaSpider.get_cmt(url=task['url'], quantity='specify')
                task_cnt += 1
            

        @staticmethod
        def get_media(url, quantity=None):
            sec_uid = Utils.get_sec_uid(url)
            # print(sec_uid)
            api, params, headers = DouYinApi.get_media(sec_uid)
            # print(api, params, headers)
            
            # print('-----------')
            # print(DouYinSpider.session.cookies)
            # print(DouYinSpider.session.headers)
            interceptor = RequestInterceptor(DouYinSpider.session)
            DouYinSpider.session.send = interceptor.send  # 挂载
            response = DouYinSpider.session.get(url=api, params=params, headers=headers)
            os.makedirs("download/media", exist_ok=True)
            with open(f"download/media/{sec_uid}.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            json_str = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text)
            # print(json_str)
            data = json.loads(unquote(json_str[0]))
            # pprint(data)
            url = data['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']
            # print(url)
            video_content = DouYinSpider.session.get(url).content
            with open(f"download/media/{sec_uid}.mp4", mode="wb") as f:
                f.write(video_content)
            # print(response.text)  
            pprint(1)
            
            
        @staticmethod
        def get_cmt(url, quantity):
            cnt = 0
            if quantity == 'one':
                end = 10
            elif quantity == 'some':
                end = 30
            modal_id = DouYinUtils.get_modal_id(url)
            # modal_id = '7606785573176575729'
            print(modal_id)
            download_path = Path(__file__).parent.parent.parent / "download" / "comment" / f"{modal_id}.csv"
            os.makedirs(download_path.parent, exist_ok=True)
            api, params = DouYinApi.get_cmt(modal_id)
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMi42ZmQ3MTQ1MDVlNTViZjBmMzA5NThmMDRjODkxOTk1MzgxMmJhMjk3Njc5ZDdkODBkNmRhYWE0YjE2MjJhYWM4YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJidEFmdGk0amVmMXRGYVNLQ2dCYng0TThWUXpicU9XNXVwbnJGdis3UTNFPSIsInRpbWVzdGFtcCI6MTc3NDg2NjQwN30=',
                'bd-ticket-guard-ree-public-key': 'BB5TwqhuR7kfq/3RUj6FLjCN6PlXEG0rmEZtN5eCPDRb5T6cELoQfiSxVtP3Lgb1ysVF1Oqd4PAlpoYlnaZyu4k=',
                'bd-ticket-guard-version': '2',
                'bd-ticket-guard-web-sign-type': '1',
                'bd-ticket-guard-web-version': '2',
                'cache-control': 'no-cache',
                'origin': 'https://www.douyin.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://www.douyin.com/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            }
            with open(download_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['cid', '昵称', '评论内容', '时间', 'ip'])
            while True:
                params = DouYinUtils.get_a_bogus(params)
                response = DouYinSpider.session.get(url=api, params=params, headers=headers)
                json_dict = response.json()
                # pprint(json_dict)
                comment = CommentItem()
                for i in json_dict['comments']:
                    comment.cid = i['cid']
                    comment.ip = i['ip_label']
                    comment.name = i['user']['nickname']
                    comment.text = i['text']
                    comment.time = i['create_time']
                    cnt += 1
                    print(cnt, comment.cid, comment.name, comment.text, comment.time, comment.ip)
                    with open(download_path, 'a', newline='', encoding='utf-8-sig') as f:
                        writer = csv.writer(f)
                        writer.writerow([comment.cid, comment.name, comment.text, comment.time, comment.ip])
                    if cnt == end:
                        return
                params['cursor'] = json_dict['cursor']
                if json_dict['has_more'] == 0:
                    return


            

        @staticmethod
        def get_reply(url, quantity=None):
            modal_id = DouYinUtils.get_modal_id(url)
            api, params = DouYinApi.get_reply(modal_id)
            params = DouYinUtils.get_a_bogus(params)
            # params['fp'] = DouYinUtils.get_fp()
            # print(params['fp'])
            response = DouYinSpider.session.get(url=api, params=params)
            json_dict = response.json()
            pprint(json_dict)

        @staticmethod
        def get_search(query: str):
            api, params = DouYinApi.get_search(query)
            params = DouYinUtils.get_a_bogus(params)
            response = DouYinSpider.session.get(url=api, params=params)
            json_dict = response.json()
            pprint(json_dict)

        @staticmethod
        def get_blogger_info(url: str):
            sec_uid = DouYinUtils.get_sec_uid(url)
            api, params = DouYinApi.get_other(sec_uid)
            # params['msToken'] = DouYinUtils.get_ms_token()
            # pprint(params)
            params = DouYinUtils.get_a_bogus(params)
            
            response = DouYinSpider.session.get(url=api, params=params)
            print(response.text)
            print(response.status_code)
            # print(response.text)
            json_dict = response.json()
            pprint(json_dict)

        @staticmethod
        def get_my_followings():
            api, params = DouYinApi.get_followings()
            params = DouYinUtils.get_a_bogus(params)
            pprint(params)
            while True:
                response = DouYinSpider.session.get(url=api, params=params)
                json_dict = response.json()
                pprint(json_dict)
                followings = FollowingsItem()
                for k, v in enumerate(json_dict['followings']):
                    # avatar_small = v['avatar_small']['url_list'][0]
                    # avatar_thumb = v['avatar_thumb']['url_list'][0]
                    # nickname = v['nickname']
                    # sec_uid = v['sec_uid']
                    # signature = v['signature']
                    # uid = v['uid']
                    # unique_id = v['unique_id']
                    # short_id = v['short_id']
                    # aweme_count = v['aweme_count']
                    followings.avatar_thumb = v['avatar_thumb']['url_list'][0]
                    followings.nickname = v['nickname']
                    followings.sec_uid = v['sec_uid']
                    followings.signature = v['signature']
                    followings.uid = v['uid']
                    followings.unique_id = v['unique_id']
                    followings.short_id = v['short_id']
                    followings.aweme_count = v['aweme_count']
                    print(k, followings.nickname, followings.sec_uid, followings.signature, followings.uid, followings.unique_id, followings.short_id, followings.aweme_count)
                    yield followings
                #     s.cursor.execute('''
                #         INSERT OR IGNORE INTO followings 
                #         (uid, sec_uid, unique_id, short_id, nickname, signature, avatar_thumb, aweme_count)
                #         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                #     ''', (uid, sec_uid, unique_id, short_id, nickname, signature, avatar_thumb, aweme_count))
                # s.conn.commit()
                break
                time.sleep(random.uniform(1,3))
                print("-" * 30)
                params['offset'] += params['count']
                if json_dict['rec_has_more'] == False:
                    return
                       
    


    class Download():

        @staticmethod
        def download_singal_video(url: str):
            response = DouYinSpider.session.get(url=url, stream=True)
            with open("video.mp4", 'wb') as f:
               f.write(response.content)
        
    class Ops():
        pass




# if __name__ == '__main__':
    # s = DouYinSpider()
    # s.MediaSpider.get_search('极端天气')
    # s.Utils.get_user_info()
    # s.MediaSpider.get_search('极端天气')
    # s.MediaSpider.get_cmt('https://www.douyin.com/user/MS4wLjABAAAAARd_zguz0GWEiQ2xMRxfaTg9Ur2qCb_K1lggv0mRqcboJYAZElny9j8XxpJdf62I/search/%E6%9E%81%E7%AB%AF%E5%A4%A9%E6%B0%94?aid=5286fe38-92dd-4758-bde8-aea666dd9ea1&modal_id=7591861063445593515&type=general', 'some')
    # s.MediaSpider.get_my_followings()
