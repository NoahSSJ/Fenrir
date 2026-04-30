class WeiBoApi():

    @staticmethod
    def get_info(uid, is_n):
        api = "https://weibo.com/ajax/profile/info"
        if is_n:
            params = {
                'screen_name': f'{uid}',
                'scene': 'profile',
            }
        else:
            params = {
                'custom': f'{uid}',
                'scene': 'profile',
            }
        return api, params
    
    @staticmethod
    def get_following(uid):
        api = 'https://www.weibo.com/ajax/profile/followContent'
        params = {
            'sortType': 'all',
        }
        return api, params
    
    @staticmethod
    def get_cmt(id, uid, is_first):
        api = 'https://weibo.com/ajax/statuses/buildComments'
        if is_first:
            params = {
                'is_reload': '1',
                'id': f'{id}',
                'is_show_bulletin': '2',
                'is_mix': '0',
                'count': '20',
                'type': 'feed',
                'uid': f'{uid}',
                'fetch_level': '0',
                'locale': 'zh-CN',
            }
        else:
            params = {
                'flow': '0',
                'is_reload': '1',
                'id': '5276386847621761',
                'is_show_bulletin': '3',
                'is_mix': '0',
                'max_id': '141639424350015',
                'count': '20',
                'uid': '5574911608',
                'fetch_level': '0',
                'locale': 'zh-CN',
            }
        return api, params
            

    
 
