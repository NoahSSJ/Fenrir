from http.cookies import SimpleCookie
import re
import execjs
import requests
from pprint import pprint
import urllib
import os
import json
from requests.utils import cookiejar_from_dict
import time
import random
from bs4 import BeautifulSoup
import csv
# from typing import deprecated
from pathlib import Path
from .utils import BiliBiliUtils


class BiliBiliSpider():
    session = requests.Session()
    session.headers = BiliBiliUtils.get_headers()
    session.cookies.update(BiliBiliUtils.get_cookies())
    session.proxies = {
        # 'http': 'http://127.0.0.1:7890',      # 代理地址
        # 'https': 'http://127.0.0.1:7890',
    }
    _csrf = None
