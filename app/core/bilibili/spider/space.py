import json
from pprint import pprint
import sys
from loguru import logger
from .utils import BiliBiliUtils
# from .api import BiliBiliApi
from .fetch import BiliBiliSpider
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "api"))
from space import BiliBiliSpaceApi

class BiliBiliSpace():
    @staticmethod
    def get_article(url, session=BiliBiliSpider.session):
        mid = BiliBiliUtils.get_mid(url)
        # print(mid)
        api, params = BiliBiliSpaceApi.get_article(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        # pprint(params)
        response = session.get(url=api, params=params)
        json_dict = json.loads(response.text)
        pprint(json_dict)

    @staticmethod
    def get_detail(url, session=BiliBiliSpider.session):
        mid = BiliBiliUtils.get_mid(url)
        # print(mid)
        api, params = BiliBiliSpaceApi.get_detail(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        # pprint(params)
        response = session.get(url=api, params=params)
        json_dict = json.loads(response.text)
        pprint(json_dict)

    @staticmethod
    def get_nav_num(url, session):
        """
        获取博主主页导航栏数据
        """
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_nav_num(mid=mid)
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
    def get_stat(url, session): 
        vmid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_stat(vmid=vmid)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_upstat(url, session):
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_upstat(mid=mid)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_entrance(session):
        "b站动态更新提示接口"
        api, params = BiliBiliSpaceApi.get_entrance()
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_acc_info(url, session):
        "获取博主账号信息接口"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_acc_info(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_masterpiece(url, session):
        "获取up主个人空间展示代表作"
        vmid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_masterpiece(vmid=vmid)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_notice(url, session):
        "获取up主个人空间通知"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_notice(mid=mid)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_relation(url, session):
        "获取up主个人空间关注关系"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_relation(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_reservation(url, session): 
        "获取up主个人空间预约"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_reservation(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_arc_search(url, session):
        "获取up主个人空间批量作品"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_arc_search(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_seasons_series(url, session):
        "获取up主个人空间合集系列"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_seasons_series(mid=mid)
        # params = BiliBiliUtils.get_wid_signature(params)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_lastplaygame(url, session):
        "获取up主个人空间最近游玩的游戏"
        mid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_lastplaygame(mid=mid)
        params = BiliBiliUtils.get_wid_signature(params)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_coin_video(url, session):
        "获取up主个人空间投币视频"
        vmid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_coin_video(vmid=vmid)
        response = session.get(url=api, params=params)
        pprint(response.json())

    @staticmethod
    def get_like_video(url, session):
        "获取up主个人空间点赞视频"
        vmid = BiliBiliUtils.get_mid(url)
        api, params = BiliBiliSpaceApi.get_like_video(vmid=vmid)
        response = session.get(url=api, params=params)
        pprint(response.json())

    
    
    
    
