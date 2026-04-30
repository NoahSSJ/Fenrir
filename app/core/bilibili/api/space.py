class BiliBiliSpaceApi():
    @staticmethod
    def get_article(mid: str):
        api = 'https://api.bilibili.com/x/space/wbi/article'
        params = {
            'mid': mid,
            'ps': '10',
            'pn': '1',
            'platform': 'web',
            'web_location': '333.1387',
        #     'w_rid': '78a349cad7492f04e57f310d7347eff4',
        #     'wts': '1777479999',
        }
        return api, params

    @staticmethod
    def get_detail(mid: str):
        api = 'https://api.bilibili.com/x/space/wbi/detail'
        params = {
            'mid': mid,
            'token': '',
            'platform': 'web',
            'web_location': '1550101',
            'dm_img_list': '[]',
            'dm_img_str': 'V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ',
            'dm_cover_img_str': 'QU5HTEUgKE5WSURJQSwgTlZJRElBIEdlRm9yY2UgUlRYIDQwNzAgTGFwdG9wIEdQVSAoMHgwMDAwMjg2MCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSlHb29nbGUgSW5jLiAoTlZJRElBKQ',
            'dm_img_inter': '{"ds":[],"wh":[4167,2209,111],"of":[494,988,494]}',
            # 'w_rid': '7d18bedb8f2666586274869e92ce6ebc',
            # 'wts': '1777479944',
        }
        return api, params
    
    @staticmethod
    def get_stat(vmid):
        api = 'https://api.bilibili.com/x/relation/stat'
        params = {
            'vmid': vmid,
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_upstat(mid):
        api = 'https://api.bilibili.com/x/space/upstat'
        params = {
            'mid': mid,
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_entrance():
        api = 'https://api.bilibili.com/x/web-interface/dynamic/entrance'
        params = {
            'alltype_offset': '1196675156789952512',
            'video_offset': '0',
            'article_offset': '0',
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_acc_info(mid):
        api = 'https://api.bilibili.com/x/space/wbi/acc/info'
        params = {
            'mid': mid,
            'token': '',
            'platform': 'web',
            'web_location': '1550101',
            'dm_img_list': '[]',
            'dm_img_str': 'V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ',
            'dm_cover_img_str': 'QU5HTEUgKE5WSURJQSwgTlZJRElBIEdlRm9yY2UgUlRYIDQwNzAgTGFwdG9wIEdQVSAoMHgwMDAwMjg2MCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSlHb29nbGUgSW5jLiAoTlZJRElBKQ',
            'dm_img_inter': '{"ds":[],"wh":[4146,2202,104],"of":[88,176,88]}',
            # 'w_rid': '01e7f00513e61dc05449a898434f8604',
            # 'wts': '1777480321',
        }
        return api, params
    
    @staticmethod
    def get_masterpiece(vmid):
        api = 'https://api.bilibili.com/x/space/masterpiece'
        params = {
            'vmid': vmid,
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_notice(mid):
        api = 'https://api.bilibili.com/x/space/notice'
        params = {
            'mid': mid,
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_relation(mid):
        api = 'https://api.bilibili.com/x/space/wbi/acc/relation'
        params = {
            'mid': mid,
            'web_location': '333.1387',
            # 'w_rid': '99f3fc3c0b7809c32da7d9b37b688aa9',
            # 'wts': '1777480320',
        }
        return api, params
    
    @staticmethod
    def get_reservation(vmid):
        api = 'https://api.bilibili.com/x/space/reservation'
        params = {
            'vmid': vmid,
            'web_location': '333.1387',
            # 'w_rid': 'cf8ac3a26765e52b19a482e1c515e966',
            # 'wts': '1777480321',
        }
        return api, params
    
    @staticmethod
    def get_arc_search(mid, pn=1, ps=25, order='pubdate'):
        api = 'https://api.bilibili.com/x/space/wbi/arc/search'
        params = {
            'mid': mid,
            'order': order,
            'ps': ps,
            'pn': pn,
            'index': pn,
            'order_avoided': 'true',
            'platform': 'web',
            'web_location': '333.1387',
            'dm_img_list': '[]',
            'dm_img_str': 'V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ',
            'dm_cover_img_str': 'QU5HTEUgKE5WSURJQSwgTlZJRElBIEdlRm9yY2UgUlRYIDQwNzAgTGFwdG9wIEdQVSAoMHgwMDAwMjg2MCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSlHb29nbGUgSW5jLiAoTlZJRElBKQ',
            'dm_img_inter': '{"ds":[],"wh":[3945,2135,37],"of":[151,302,151]}',
            # 'w_rid': '0e1fad394d19d143ad86c98ac4791fd2',
            # 'wts': '1777480321',
        }
        return api, params
    
    @staticmethod
    def get_seasons_series(mid, page_num=1, page_size=10):
        api = 'https://api.bilibili.com/x/polymer/web-space/home/seasons_series'
        params = {
            'mid': mid,
            'page_size': page_size,
            'page_num': page_num,
            'web_location': '333.1387',
        }
        return api, params

    @staticmethod
    def get_lastplaygame(mid):
        api = 'https://api.bilibili.com/x/space/lastplaygame/v2'
        params = {
            'mid': mid,
            'web_location': '333.1387',
            # 'w_rid': 'db57338c807aaeea97b42c9c1da9ec9c',
            # 'wts': '1777482210',
        }
        return api, params
    
    @staticmethod
    def get_coin_video(vmid):
        api = 'https://api.bilibili.com/x/space/coin/video'
        params = {
            'vmid': vmid,
            'web_location': '333.1387',
        }
        return api, params

    @staticmethod
    def get_like_video(vmid):
        api = 'https://api.bilibili.com/x/space/like/video'
        params = {
            'vmid': vmid,
            'web_location': '333.1387',
        }
        return api, params