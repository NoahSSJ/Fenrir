import os
import sys
from core.bilibili.spider.media import BiliBiliMedia
# from core.bilibili.spider.a import BiliBiliMedia
from core.douyin.fetch import DouYinSpider
# from core.xhs.fetch import XhsSpider
from core.bilibili.spider.fetch import BiliBiliSpider
from core.bilibili.spider.space import BiliBiliSpace
from core.bilibili.spider.utils import BiliBiliUtils
from core.bilibili.spider.live import BiliBiliLiveSpider
import os
import sqlite3
from urllib.parse import unquote
from pathlib import Path
from controller.engine import Engine
from database.client import SQLiteConfig
if __name__ == '__main__':

    # a = BiliBiliSpace.get_acc_info('https://space.bilibili.com/1166997747/upload/video', BiliBiliSpider.session)
    # a = BiliBiliMedia().get_danmaku('https://www.bilibili.com/video/BV1fMQZB9Euz/?spm_id_from=333.337.search-card.all.click&vd_source=cd2f30c4c2b17931e5fe4b95752072ee')
    BiliBiliLiveSpider.get_live_info(BiliBiliSpider.session)
