import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from datetime import datetime
import hashlib
from pprint import pprint

class RequestInterceptor:
    def __init__(self, session: requests.Session):
        self.session = session
        self.original_send = session.send  # 保存原生send（关键！）
        self.setup_retry()

    def setup_retry(self):
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[408, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def send(self, request, **kwargs):
        # 请求拦截 + 统一处理
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0'
        self.add_sign(request)

        # 调用 原生send，不会递归！
        return self.original_send(request, **kwargs)

    def add_sign(self, request):
        sign = hashlib.md5(request.url.encode()).hexdigest()
        token = "12345"
        timestamp = int(datetime.now().timestamp())
        request.headers['sign'] = sign
        request.headers['token'] = token
        request.headers['timestamp'] = timestamp

# ======================
# 使用方法（超级简单）
# ======================

# # 1. 创建 session
# session = requests.Session()

# # 2. 安装拦截器（自动替换 send）
# interceptor = RequestInterceptor(session)
# session.send = interceptor.send  # 挂载

# # 3. 正常使用！
# res = session.get("https://httpbin.org/get")
# pprint(res.json())