import requests
import os
import json
from pathlib import Path
from .utils import XhsUtils

from pprint import pprint

class XhsSpider():
    
    session = requests.Session()
    session.headers = XhsUtils.get_headers()
    session.cookies.update(XhsUtils.get_cookies())
    XhsUtils.get_post(session, 'https://www.xiaohongshu.com/user/profile/68f441e2000000003700733e?xsec_token=AB43Iw6UkZyiAVGm6jhFmDNbCyqQfVQj4wtQUQ8rtdMvY=&xsec_source=pc_like')





    

