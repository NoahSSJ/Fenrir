class BiliBiliLiveApi():
    @staticmethod
    def get_live_info():
        api = 'https://live.bilibili.com/440006'
        headers = {
            'Referer': 'https://live.bilibili.com/?spm_id_from=333.337.0.0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
            'sec-ch-ua': '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'session_id': '57cd81dfe119e1f101c3df547969f4ec_F359D6DC-3EB7-4F80-9DB5-341A4746A25A',
            'launch_id': '1000216',
            'live_from': '71001',
        }
        return api, params, headers