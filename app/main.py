import os
from core.bilibili.media import BiliBiliMedia
from core.douyin.fetch import DouYinSpider
# from core.xhs.fetch import XhsSpider
from core.bilibili.fetch import BiliBiliSpider
from core.bilibili.space import BiliBiliSpace
import os
import sqlite3
from urllib.parse import unquote
from pathlib import Path
from controller.engine import Engine
from database.client import SQLiteConfig
if __name__ == '__main__':

    # s = DouYinSpider()
    # xhs_s = XhsSpider()
    a = BiliBiliSpace()
    a.get_arc_search('https://space.bilibili.com/1166997747', session=BiliBiliSpider.session)
    # pipeline = SQLiteConfig('a.db')
    # engine = Engine(s.MediaSpider.get_my_followings(), [pipeline])
    # engine.run()

    # s.MediaSpider.get_search('极端天气')
    # s.Utils.get_user_info()
    # s.MediaSpider.get_search('极端天气')
    # s.MediaSpider.get_cmt('https://www.douyin.com/user/MS4wLjABAAAAARd_zguz0GWEiQ2xMRxfaTg9Ur2qCb_K1lggv0mRqcboJYAZElny9j8XxpJdf62I/search/%E6%9E%81%E7%AB%AF%E5%A4%A9%E6%B0%94?aid=5286fe38-92dd-4758-bde8-aea666dd9ea1&modal_id=7591861063445593515&type=general', 'some')
    # s.MediaSpider.get_my_followings()
    # print(SQLiteClient.get_all("followings"))
    # s.MediaSpider.get_media('https://www.douyin.com/user/MS4wLjABAAAAqTbVAwQKFqhIQ9JmNOlE2jN3jm2nl73cth079q5H3WrszFmPPUKNbpluBwuaruGI?from_tab_name=main&modal_id=7623054442161605926&vid=7622322995519819048')
    # s.MediaSpider.producer('https://www.douyin.com/user/MS4wLjABAAAAqTbVAwQKFqhIQ9JmNOlE2jN3jm2nl73cth079q5H3WrszFmPPUKNbpluBwuaruGI?from_tab_name=main')
    # s.Download.download_singal_video("https://v5-dy-o-abtest.zjcdn.com/6861b7bb2909f12d0396afde7876529b/69cbf61e/video/tos/cn/tos-cn-ve-15c000-ce/ogiTyPXvxhtipBMATsW1AQHWHa6E1dWvIS9JN/?a=6383\u0026ch=10010\u0026cr=3\u0026dr=0\u0026lr=all\u0026cd=0%7C0%7C0%7C3\u0026cv=1\u0026br=4171\u0026bt=4171\u0026cs=0\u0026ds=6\u0026ft=dqukd5S30BN12NvjDyznCnRfS9NuG-4kSYNc\u0026mime_type=video_mp4\u0026qs=1\u0026rc=M2k5ZTYzOmY3Ojo1OTs4ZEBpM21weHc5cnBwODMzbGkzNEBgLi42YTNeNi0xLy8zMTMxYSNfcmU2MmRrbmdhLS1kLWJzcw%3D%3D\u0026btag=c0000e00010000\u0026cquery=100z_100o_101r_100B_100x\u0026dy_q=1774963679\u0026feature_id=0ea98fd3bdc3c6c14a3d0804cc272721\u0026l=2026033121275868AC98D1A9043EAFE8F0")
    # s.Utils.get_ms_token()
    # s.MediaSpider.get_blogger_info('https://www.douyin.com/user/MS4wLjABAAAAuoUCZcfFoZqv1gS5lyEC2nNsH7LL2uEZP4rKrT77W9kp7nrhRAnYalqwmBmNAu3Y?from_tab_name=main')
