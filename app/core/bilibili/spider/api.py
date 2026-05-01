import json
import urllib


class BiliBiliApi():
    @staticmethod
    def get_nav_num(mid):
        api = 'https://api.bilibili.com/x/space/navnum'
        params = {
            'mid': f'{mid}',
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_search(pn):
        api = 'https://api.bilibili.com/x/space/wbi/arc/search'
        params = {
                "pn": f"{pn}",
                "ps": "40",
                "tid": "0",
                "special_type": "",
                "order": "pubdate",
                "mid": "1166997747",
                "index": "0",
                "keyword": "",
                "order_avoided": "true",
                "platform": "web",
                "web_location": "333.1387",
                'dm_img_list': urllib.parse.quote(json.dumps([
                    {"x":534,"y":390,"z":0,"timestamp":0,"k":101,"type":0},
                    {"x":1331,"y":322,"z":57,"timestamp":4,"k":72,"type":0},
                    {"x":1327,"y":165,"z":29,"timestamp":106,"k":94,"type":0}
                ])),
                'dm_img_str': 'V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ',
                'dm_cover_img_str': 'QU5HTEUgKE5WSURJQSwgTlZJRElBIEdlRm9yY2UgUlRYIDQwNzAgTGFwdG9wIEdQVSAoMHgwMDAwMjg2MCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSlHb29nbGUgSW5jLiAoTlZJRElBKQ',
                'dm_img_inter': urllib.parse.quote('{"ds":[{"t":0,"c":"bnByb2dyZXNzLWJ1c3","p":[294,98,98],"s":[504,3478,-1300]}],"wh":[2924,673,94],"of":[419,838,419]}'),
                # 'w_webid':'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzcG1faWQiOiIzMzMuMTM4NyIsImJ1dmlkIjoiQjlCQjFCOUUtOUYwMC0wNDFFLTJCNjgtRUMyRTI0RTU3N0UxNjI4MTFpbmZvYyIsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM5LjAuMC4wIFNhZmFyaS81MzcuMzYgRWRnLzEzOS4wLjAuMCIsImJ1dmlkX2ZwIjoiYmNiZThlYzU0ZWY3ZjEyODZkNDBiODM1NjNhZTE2N2IiLCJiaWxpX3RpY2tldCI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW10cFpDSTZJbk13TXlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKbGVIQWlPakUzTlRVek16VTROakFzSW1saGRDSTZNVGMxTlRBM05qWXdNQ3dpY0d4MElqb3RNWDAuYk1XdVY2Y3J3TXRtVUNMMmRZVEJMelFGbzFBZnZLN1B5dmUyVEdLaUhJbyIsImNyZWF0ZWRfYXQiOjE3NTUzMTU2NTQsInR0bCI6ODY0MDAsInVybCI6Ii8xNzY5NzAzNDk5L3VwbG9hZC92aWRlbyIsInJlc3VsdCI6MCwiaXNzIjoiZ2FpYSIsImlhdCI6MTc1NTMxNTY1NH0.Y5d8tmNxLpCvjmKfUgud13WYZiLUNCDuihUzrKHF2HL1Y4-cDEABIJsy0_xwZxy-FqTxz7lEDlUiVM_yPQhuenbgAhpQi4k8tKk60Ag7ZD8cCV7046iviXemK9okxOizXko3o_wNn5WPgORrt4KR_ctHXoJ-QS1PeKVf39XVpzJEAnXv6psEQM6utW-aUnzbhkVIVhKIMp0Pe3ki01BIZdpu0SPuyw2AvW8RW1Fjf2Qk6vDaP_-BcbLaRF3XG6l4GmFLUEccwcF5LQYcwjFEbqGNjXrCmwpZ41xB-oJQKDNgmvUx0tYuxiq91gAoas1jpZREEcPMny4qqLpCxEd7XA',
                }
        return api, params
    


    @staticmethod
    def get_followings(vmid: str, pn: int, ps: int = 24):
        api = 'https://api.bilibili.com/x/relation/followings'
        params = {
        'order': 'desc',
        'order_type': '',
        'vmid': f'{vmid}',
        'pn': f'{pn}',
        'ps': f'{ps}',
        'gaia_source': 'main_web',
        'web_location': '333.1387',
    }
        return api, params
    
    @staticmethod
    def get_stat(vmid: str):
        api = 'https://api.bilibili.com/x/relation/stat'
        params = {
            'vmid': f'{vmid}',
            'web_location': '333.1387',
        }
        return api, params
    
    @staticmethod
    def get_coin_add(aid: str, csrf: str, mutiply: int):
        api = 'https://api.bilibili.com/x/web-interface/coin/add'
        params = {
            'aid': f'{aid}',
            'multiply': f'{mutiply}',
            'select_like': '1',
            'cross_domain': 'true',
            'from_spmid': '333.337.search-card.all.click',
            'spmid': '333.788.0.0',
            'statistics': '{"appId":100,"platform":5}',
            'eab_x': '2',
            'ramval': '2',
            'source': 'web_normal',
            'ga': '1',
            'csrf': csrf,
        }
        return api, params
    
    @staticmethod
    def get_collect(rid, add_media_id):
        api = 'https://api.bilibili.com/x/v3/fav/resource/deal'
        data = f'rid={rid}&type=2&add_media_ids={add_media_id}&del_media_ids=&platform=web&from_spmid=333.1387.homepage.video_card.click&spmid=333.788.0.0&statistics=%7B%22appId%22:100,%22platform%22:5%7D&csrf=9a59010f5cb5cbfb4007c1325b340c17'
        return api, data

    @staticmethod
    def get_collect_files(vmid: str):
        api = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all'
        params = {
            'type': '2',
            'rid': '116253708519246',
            'up_mid': f'{vmid}',
            'web_location': '333.788',
        }
        return api, params
    
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
    def get_acc_info():
        api = 'https://api.bilibili.com/x/space/wbi/acc/info'
        params = {
            'mid': '1166997747',
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


    nav= 'https://api.bilibili.com/x/web-interface/nav'
    aaa = 'https://api.bilibili.com/x/internal/gaia-gateway/ExGetAxe'