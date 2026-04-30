from .api import BiliBiliApi
from .utils import BiliBiliUtils
from .fetch import BiliBiliSpider

class BiliBiliComment(BiliBiliSpider):
    @staticmethod
    def get_one_cmt(url):
        """
        Note:   获取博主某个视频一级评论数据
        Args:
            url (str): 视频url
        Returns:
            None
        """
        oid, _, _ = BiliBiliUtils.get_video_id(url, BiliBiliSpider.session)
        # print(oid)
        next_offset = ''
        cnt = 1
        while True:
            pagination_str = f'{{"offset":"{next_offset}"}}'
            api, params = BiliBiliApi.get_cmt(oid=oid, pagination_str=pagination_str)
            params = BiliBiliUtils.get_wid_signature(params=params)
            # pprint(params)
            response = BiliBiliSpider.session.get(url=api, params=params)
            # pprint(response.json())
            # next_offset = response.json()['data']['cursor']['pagination_reply']['next_offset']
            for i in response.json()['data']['replies']:
                msg = i['content']['message']
                like = i['like']
                name = i['member']['uname']
                print(cnt, msg, like, name)
            if response.json()['data']['cursor']['is_end'] == True:
                break
            return



if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1uLWQzqEmj/?spm_id_from=333.337.search-card.all.click"
    BiliBiliComment.get_one_cmt(url)