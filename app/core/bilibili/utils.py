from http.cookies import SimpleCookie
import json
import math
import os
from pathlib import Path
from pprint import pprint
import re
# from warnings import deprecated
from pathlib import Path
import execjs
from loguru import logger
from .api import BiliBiliApi
from dotenv import load_dotenv
class BiliBiliUtils():
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
            'referer': 'https://space.bilibili.com/1166997747/upload/video',
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
        return headers
    
    @staticmethod
    def get_cookies():
        auth_path = Path(__file__).parent.parent.parent / "config" / "auth" / "cookies" / ".env.bilibili"
        load_dotenv(auth_path)
        cookie_str = os.getenv('BILIBILI_COOKIES')
        # print(cookie_str)
        cookie = SimpleCookie(cookie_str)
        cookie_dict = {k: v.value for k, v in cookie.items()}
        return cookie_dict

    @staticmethod
    def get_wbi_key(session):
        """
        Note: 获取bilibiliwid签名
        Args:
            session: requests会话实例
        Returns:
            dict: wbi_key
        """
        response = session.get(url = BiliBiliApi.nav)
        wbi_key = response.json()["data"]["wbi_img"]
        wbiImgKey = wbi_key["img_url"].split('.')[-2].split('/')[-1]
        wbiSubKey = wbi_key["sub_url"].split('.')[-2].split('/')[-1]
        return {
            "wbiImgKey": wbiImgKey,
            "wbiSubKey": wbiSubKey
        }

    @staticmethod
    def get_wid_signature(params):
        """
        Note: 获取bilibiliwid签名
        Args:
            params: 请求参数
        Returns:
            dict: 请求参数，包含wid签名
        """
        # wbi_key = BiliBiliAuth.get_wbi_key(session)
        # pprint(wbi_key)
        wbi_key = {'wbiImgKey': '7cd084941338484aae1ad9425b84077c',
 'wbiSubKey': '4932caff0ff746eab6f01bf08b70ac45'}
        js_path = Path(__file__).parent.parent.parent / "core" / "bilibili" / "signature" / "wid.js"
        with open(js_path, mode='r', encoding='utf-8') as f:
            js_code = f.read()
        ctx = execjs.compile(js_code)
        wid = ctx.call("XN", params, wbi_key)
        params.update(wid)
        return params

    @staticmethod
    def get_mid(url):
        match = re.search(r'space\.bilibili\.com/(\d+)', url)
        return match.group(1) if match else None

    @staticmethod
    def get_nav_num(url, session):
        """
        获取博主主页导航栏数据
        """
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliApi.get_nav_num(mid=mid)
        response = session.get(url=api, params=params)
        album = response.json()['data']['album']
        article = response.json()['data']['article']    
        audio = response.json()['data']['audio']
        bangumi = response.json()['data']['bangumi'] 
        opus = response.json()['data']['opus']
        video = response.json()['data']['video']
        logger.info(f"album: {album}, article: {article}, audio: {audio}, bangumi: {bangumi}, opus: {opus}, video: {video}")
        pprint(response.json())
        return video
    
    @staticmethod
    # @deprecated("请改用 new_function")
    def get_video_id(url, session):
        """
        Note: 获取指定视频的aid, bvid, cid
        Args:
            url: 视频url

        ReturnS:
            aid: 视频aid
            bvid: 视频bvid
            cid: 视频cid
        """
        response = session.get(url)
        # print(response.text)
        html = response.text

        aid  = re.search(r'"aid"\s*:\s*(\d+)', html).group(1)
        bvid = re.search(r'"bvid"\s*:\s*"([^"]+)"', html).group(1)
        cid  = re.search(r'"cid"\s*:\s*(\d+)', html).group(1)
        print(aid, bvid, cid)
        return aid, bvid, cid
    
    # @staticmethod
    # def 














    
    @staticmethod
    def get_my_stat(url, session):
        """
        Note: 获取指定博主(自己)关注者和粉丝数
        Args:
            vmid: 博主(自己)vmid

        ReturnS:
            following: 关注者数
            follower: 粉丝数
        """
        vmid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliApi.get_stat(vmid=vmid)
        response = session.get(url=api, params=params)
        json_dict = json.loads(response.text)
        # pprint(json_dict)
        following = json_dict['data']['following']
        follower = json_dict['data']['follower']
        print(f"关注: {following}, 粉丝: {follower}")
        return following, follower
    
    @staticmethod
    def get_my_following(url, session):
        """
        Note: 获取指定博主(自己)所有关注者
        Args:
            vmid: 博主(自己)vmid    
            cnt: 序号
            pn: 页码
            ps: 每页数量
            end: 总页数

        ReturnS:
            None
        """
        vmid = BiliBiliUtils.get_mid(url)
        cnt =  1
        pn =  2
        ps =  24
        following_num, _ = BiliBiliUtils.get_my_stat(url)
        end = math.ceil(following_num / ps)
        while True:
            if (pn >= end):
                break
            api, params = BiliBiliApi.get_followings(vmid=vmid, pn=pn, ps=ps)
            response = session.get(url=api, params=params)
            json_dict = json.loads(response.text)
            pprint(json_dict)
            for i in json_dict['data']['list']:
                name = i['uname']
                mid = i['mid']
                print(f"序号: {cnt} | 名称: {name} | mid: {mid}")
                cnt += 1
            pn += 1
            break

    @staticmethod
    def get_my_collect_files(vmid, session):
        """
        Note: 获取指定博主(自己)所有收藏文件夹id
        Args:
            vmid: 博主(自己)vmid

        ReturnS:
            None
        """
        if vmid == None:
            logger.warning("请输入vmid")
            return
        api, params = BiliBiliApi.get_collect_files_params(vmid=vmid)
        response = session.get(url=api, params=params)
        json_dict = json.loads(response.text)
        # pprint(json_dict)
        for i in json_dict['data']['list']:
            print(i['id'], i['title'])

    @staticmethod
    @property
    def get_csrf():

        csrf = os.getenv("MY_COOKIES").split("bili_jct")[1].split(";")[0].split("=")[1]
        # BiliBiliSpider._csrf = csrf
        # print(csrf)
        return csrf


# if __name__ == "__main__":
#     BiliBiliUtils.get_cookies()