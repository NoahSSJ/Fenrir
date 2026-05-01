class BiliBiliVideoApi():
    @staticmethod
    def get_danmaku(oid, pid):
        api = 'https://api.bilibili.com/x/v2/dm/wbi/web/seg.so'
        params = {
            'type': '1',
            'oid': oid,
            'pid': pid,
            'segment_index': '3',
            # 'pull_mode': '1',
            # 'ps': '0',
            # 'pe': '120000',
            'web_location': '1315873',
        }

        return api, params
        
    @staticmethod
    def get_cmt(oid, pagination_str):
        api = 'https://api.bilibili.com/x/v2/reply/wbi/main'
        params = {
                "oid": f"{oid}",          # 改成你需要的 oid
                "type": 1,
                "mode": 3,
                "pagination_str": pagination_str,   # 用变量
                "plat": 1,
                "seek_rpid": "",
                "web_location": 1315875,
            }
        return api, params
