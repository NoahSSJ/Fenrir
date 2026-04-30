# ua/ip/ck
from pprint import pprint
from fake_useragent import UserAgent
 

class RequestPool():
    def __init__(self):
        pass

    def get_random_headers(self):
        ua = UserAgent()
        headers = {"User-Agent": ua.random} 
        return headers
    
    def get_random_ip(self):
        pass

    def get_random_ck(self):
        pass