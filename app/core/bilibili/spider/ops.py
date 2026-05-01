import json
from pprint import pprint
from .api import BiliBiliApi
from .fetch import BiliBiliSpider
from .utils import BiliBiliUtils

class BiliBiliOps():
        @staticmethod
        def like(url:str):
            """
            Note: 点赞博主某个视频
            Args:
                url (str): 视频url
            Returns:
                None
            """
            response = BiliBiliSpider.session.get(url)
            print(response.text)

        @staticmethod
        def add_coin(url, mutiply=2):       
            """
            Note: 给指定视频投币  
            Args:
                aid: 视频aid
                mutiply: 倍数

            ReturnS:
                None
            """ 
            csrf = BiliBiliUtils.get_csrf()
            aid, _, _ = BiliBiliUtils.get_video_id(url, session=BiliBiliSpider.session)
            api, params = BiliBiliApi.get_coin_add(aid=aid, csrf=csrf, mutiply=mutiply)
            response = BiliBiliSpider.session.post(url=api, params=params)
            json_dict = json.loads(response.text)
            pprint(json_dict)

        @staticmethod
        def collect_one_video(url, add_media_id=None):
            """
            Note: 收藏指定视频 
            Args:
                url: 视频url
                add_media_id: 收藏夹id

            ReturnS:
                None
            """ 
            aid, _, _ = BiliBiliUtils.get_video_id(url, session=BiliBiliSpider.session)
            api, params = BiliBiliApi.get_collect_data(rid=116253708519246, add_media_id=add_media_id)
            response = BiliBiliSpider.session.post(url=api, params=params)
            json_dict = json.loads(response.text)
            pprint(json_dict)