import time


class DouYinApi:
    @staticmethod
    def get_post(sec_uid: str):
        api = 'https://www-hj.douyin.com/aweme/v1/web/aweme/post/'
        params = {
                'device_platform': 'webapp',
                'aid': '6383',
                'channel': 'channel_pc_web',
                'sec_user_id': f'{sec_uid}',
                'max_cursor': '0',
                'locate_item_id': '7552472710513773864',
                'locate_query': 'false',
                'show_live_replay_strategy': '1',
                'need_time_list': '0',
                'time_list_query': '0',
                'whale_cut_token': '',
                'cut_version': '1',
                'count': '18',
                'publish_video_strategy_type': '2',
                'from_user_page': '1',
                'update_version_code': '170400',
                'pc_client_type': '1',
                'pc_libra_divert': 'Windows',
                'support_h265': '1',
                'support_dash': '1',
                'cpu_core_num': '32',
                'version_code': '290100',
                'version_name': '29.1.0',
                'cookie_enabled': 'true',
                'screen_width': '1920',
                'screen_height': '1080',
                'browser_language': 'zh-CN',
                'browser_platform': 'Win32',
                'browser_name': 'Edge',
                'browser_version': '146.0.0.0',
                'browser_online': 'true',
                'engine_name': 'Blink',
                'engine_version': '146.0.0.0',
                'os_name': 'Windows',
                'os_version': '10',
                'device_memory': '8',
                'platform': 'PC',
                'downlink': '10',
                'effective_type': '4g',
                'round_trip_time': '100',
                'webid': '7578114874557318683',
                'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
                'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
                'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
                'msToken': '5PFYVQc7_Lr9iWEaS7DRQ6Nwg97by_RhlGqGYwKU3RJcz8EWGUkkeqYuHfBZkjTJOcyN2jOu8pejnl162yqYhFKa2zxLjwktYcO0nFepzXQIE8r1lw0qiTMZeCDyVVPFV1jbY9eRBZdMaehdDLt2iqgisuQQDlr_sHyEBqMFW4Fk7M_jSgRcrMU=',
                'a_bogus': 'Dj0RDzy7Dp8jaV/SucEfH5VUw9y/NB8yhPioWqFT9NzZP7eGD8PZTPtnrozwlJ5zHYBkiqV7bV-lbfVcYUU0ZqHkKmpDSp7S7t/5VyXL0HkVbTJZXNfieGGxoiPPMC4Tm5ICi/6RXsMFIDQWVrCiAd17q/3NR5EdFq-UV/TnT9Km0Wujwn/5a-fkFh-3',
            }
        return api, params

    @staticmethod
    def get_reply(modal_id: str):
        api = 'https://www-hj.douyin.com/aweme/v1/web/comment/list/reply/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'item_id': f'{modal_id}',
            'comment_id': '7621821644105466633',
            'cut_version': '1',
            'cursor': '0',
            'count': '3',
            'item_type': '0',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '150',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': '0YtYERlOxTVCLQnwKjhHyfhRC58aJBwsYpKkLpLaYugkSjvDzGwIpZckpIrG45HXyl-_bcLP6O3KxGjrxM7UJHVkaHmpKhxuUR5wjdxz8x4KjEDwNJHz4xyitYBkI-knh-hRbc6vrA_m18OdNXjOdHM87-H_ZnGd-9AgzPEM61jMXg==',
            'a_bogus': 'd6sfgqS7d2mjPVKbmCEWHlql8HEANBSyclT2RLaT9xzWPHzG1RPpzcalbxwwRzZkybp0iqQHjV4AudxcusUkZFnkwmkDSmwjnt29Vy0LM1H1G-i2JHfieGSxziPclCsTmAICiMvRls0eIdcWIN9zAQIHL/vNR5jdPH-GV/zjP9K4UW8jko/9a3tpOXJqYf==',
        }
        return api, params

    @staticmethod
    def get_cmt(modal_id: str, cursor: str = '10'):
        api = 'https://www-hj.douyin.com/aweme/v1/web/comment/list/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'aweme_id': modal_id,
            'cursor': cursor,
            'count': '10',
            'item_type': '0',
            'insert_ids': '',
            'whale_cut_token': '',
            'cut_version': '1',
            'rcFT': '',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '50',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'msToken': '6damemKObHVFFazahDqqbQCuJnCWkIubAlzZ8CltcdAly62h-RVzFdZp68HaPmPZPp0bu9E2J-oobNwghJMqMVSKmPaRlg_0NmmBqLkKmAfYwufgWeyr3ccO7NjwfRK1YPmRzfi9G1ZmW07NSXLmcZzoiLCaYvM79jIqBSpHtDFQcQ==',
            'a_bogus': 'DJsnDwtyEx8RFd/tuOm6C1MUwHxlNB8y2aixRYlTCOOWP1zT7YNBzntTjxLlAIhyvmpkiCA7WnMAYxxbYsUTZFekwmZDSdhjH0VVVhvLhZrfT-ig3rf8C74FLXBP8b4u-A5ailRIMUryIdc-NHdu/Q1y7KoFQObkOqQRkMYbi9k6Z0LAEZn1PpGQi7JqxD==',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
        }
        return api, params

    @staticmethod
    def get_other(sec_uid: str):
        api = 'https://www.douyin.com/aweme/v1/web/user/profile/other/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'publish_video_strategy_type': '2',
            'source': 'channel_pc_web',
            'sec_user_id': sec_uid,
            'personal_center_strategy': '1',
            'profile_other_record_enable': '1',
            'land_to': '1',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '50',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': 'ZRYlL_D9GD0Wi7ZzgMV2I3B2sqwivXh53bvo-lQT1pcnVcAU7dG6aVGLmYlaW9eMJoHmJlrA0kIJiImB4iSNL0_JR3Cs0bce2lR97esFlIczsfd_ipfmV2uHg8BMKlV4RJ4T0zAHarg5jiPNeCkyIh3Zjj75dPfgLYn-ajkh3irUoKn1oTv5jos=',
            'a_bogus': 'Q6sVhztjE28jaV/SmOJNCSelM79/NB8ykeioWrnTtPY6aX0bAuNpzNtKGowPsxjEjRB0iC3H8Vl/YxVcYsUwZoHpFmpkuBhWn02VVz8oMqHZbPkZvrRweJtxuiTPlSsTmAAniZXRWs0CIE5WVN9wAB3HL/vNRcfdMq34VMYji9usUW8jwx/na5S2N7iqmf==',
        }
        return api, params
    
    @staticmethod
    def get_open_api():
        api = 'https://tnc0-alisc1.zijieapi.com/get_domains/v5/'
        params = {
            'tnc_js_sdk_version': '2.3.15.0',
            'device_platform': 'pc',
            'aid': '6383',
            'device_id': '7578114874557318683',
            'user_id': '102578708612',
            'web_service': '',
        }
        return api, params
    
    @staticmethod
    def get_social_count():
        api = 'https://www.douyin.com/aweme/v1/web/social/count/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'source': '6',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '50',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'msToken': 'mI_BIgafEFi510hALTymLHxTI2DKCV6_h4oo0cCjJnV3sdwxHh8aFKeUmCeZcIGN8CRdutohPUrrtJu-nOn3IrYMD2ECWPPZn9fCKL2kMEFb42D63vwJBY9edJdgHADeQfdgPDhGMhV4k7w9TquN3DS4F192c6RgFmrUzCzAkO-oyclQ3Tea-Dw=',
            'a_bogus': 'mfsRgwtJEo8ROVFS8CGPCbAUxIdArBuyRaidWaITHNTGP1zGYSNBTrtVrxFa4ZY8fmp0ieV7/VllbdVc84XwZo9kumkvuNtSIU5VVhfohHr2PGJgHHf8CSWFoXsOWcTul/53ilWIZUJw2Ec-NNdY/B3ySKoKQORkQqdRkZubx9kh106Ag1nrPQtQYXiq',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
        }
        return api, params

    @staticmethod
    def get_ms_token():
        api = 'https://mssdk.bytedance.com/web/report'
        params = {
            'ms_appid': '6383',
            'msToken': '6OI5ml1Pr_F47aU1hRFD-_uCKgSANNOqtH9YPOz2oZXOptsdS_RKrPtFyHG0XO1lGvxTuqdNJ0487zFJsEqvfmQIaKMZ_WqWQ0TpZzrzx6JY9TnJqzVX6A-LackhzTbO5M-yrs-FVEdKgBXBPLUcrj2RPajTbhums8fuUCP3WhGW5TdGxwvqVF4=',
        }
        data = '{"magic":538969122,"version":1,"dataType":8,"strData":"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","tspFromClient":1774852012204,"ulr":0}'
        return api, params, data
    
    @staticmethod
    def get_user(sec_uid):
        api = f'https://www.douyin.com/user/{sec_uid}'
        params = {
            'from_tab_name': 'main',
        }
        return api, params
    
    @staticmethod
    def get_media(sec_uid):
        api = f'https://www.douyin.com/user/{sec_uid}'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': f'https://www.douyin.com/user/{sec_uid}?enter_from=general_search&from_tab_name=main',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            # 'cookie': 'douyin.com; bd_ticket_guard_client_web_domain=2; enter_pc_once=1; UIFID_TEMP=29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa30111749c74fb73c84e778e8eadb65802f59608c9e983ed8c22ceca6592f05f717c6c28f94bbb00fb53ed1d3b86dc11c3a624dcfd50f3817b86933e365efd4a789330a612bab1d34a5ac143f2c250541; hevc_supported=true; fpk1=U2FsdGVkX1+P5GYYz4dUXtDPA7+5/DniDTJSO16isMZwImnb5DCq//CVHNiDek46RzyJ48xv++R7CDsrZbaqnQ==; fpk2=800cce95768a9a4605cb3f6b181e9057; UIFID=29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d; xgplayer_device_id=82175310514; xgplayer_user_id=305054426302; SEARCH_UN_LOGIN_PV_CURR_DAY=%7B%22date%22%3A1765539693418%2C%22count%22%3A4%7D; d_ticket=7f2847274b09ebeb55207b4430395f72a669c; passport_assist_user=Cj1MVVI_eNVb0w84qIgEim2A3MrJUMUbtwvd7Qol1I13H_YyVrntC4IbWdoVwvSIwsbmKrxUcbfLLBHkENCDGkoKPAAAAAAAAAAAAABP0_EQY243biLTBhMSirZhdkbTFnzZMqqvg21Ka6xakRKqoQiX4B-ZVefkBWPkC6mTuRC9h4QOGImv1lQgASIBAxIPWS4%3D; n_mh=lYcY7BLdmTEXV1EP3f8GdNh6MVYSRtVifLe4-4eubLc; uid_tt=212b87474f0e71918268f9d431161d37; uid_tt_ss=212b87474f0e71918268f9d431161d37; sid_tt=9476de3b51a545a815cc861109c3c6d3; sessionid=9476de3b51a545a815cc861109c3c6d3; sessionid_ss=9476de3b51a545a815cc861109c3c6d3; is_staff_user=false; _bd_ticket_crypt_cookie=835e8226aec2a8d7eb5aec1c9ef1519d; login_time=1765617046813; my_rd=2; SEARCH_RESULT_LIST_TYPE=%22single%22; SelfTabRedDotControl=%5B%7B%22id%22%3A%226910181298262788103%22%2C%22u%22%3A133%2C%22c%22%3A133%7D%5D; s_v_web_id=verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj; theme=%22dark%22; manual_theme=%22dark%22; __druidClientInfo=JTdCJTIyY2xpZW50V2lkdGglMjIlM0E1ODMlMkMlMjJjbGllbnRIZWlnaHQlMjIlM0ExMDYyJTJDJTIyd2lkdGglMjIlM0E1ODMlMkMlMjJoZWlnaHQlMjIlM0ExMDYyJTJDJTIyZGV2aWNlUGl4ZWxSYXRpbyUyMiUzQTEuMjUlMkMlMjJ1c2VyQWdlbnQlMjIlM0ElMjJNb3ppbGxhJTJGNS4wJTIwKFdpbmRvd3MlMjBOVCUyMDEwLjAlM0IlMjBXaW42NCUzQiUyMHg2NCklMjBBcHBsZVdlYktpdCUyRjUzNy4zNiUyMChLSFRNTCUyQyUyMGxpa2UlMjBHZWNrbyklMjBDaHJvbWUlMkYxNDUuMC4wLjAlMjBTYWZhcmklMkY1MzcuMzYlMjBFZGclMkYxNDUuMC4wLjAlMjIlN0Q=; __security_mc_1_s_sdk_crypt_sdk=e256819b-41b1-8eca; __security_mc_1_s_sdk_cert_key=524b273c-4e18-97ec; __security_mc_1_s_sdk_sign_data_key_web_protect=72f5cb2f-40eb-9685; is_dash_user=1; publish_badge_show_info=%220%2C0%2C0%2C1774606090731%22; sid_guard=9476de3b51a545a815cc861109c3c6d3%7C1774606118%7C5184000%7CTue%2C+26-May-2026+10%3A08%3A38+GMT; session_tlb_tag=sttt%7C4%7ClHbeO1GlRagVzIYRCcPG0wAAAAAAAAAAwGSMO4zq6o3BAcOJalthWd_xfoPXBIFBOPXO7Z9YMI0%3D; use_biz_token=true; sid_ucp_v1=1.0.0-KGJhN2UyMTg2MDI5ZjQ2ZDhiNmQ2M2FiMTA0ZGIxY2RjMGQwYWVlNTUKHwiEwauR_gIQpq6ZzgYY7zEgDDD4wKDbBTgHQPQHSAQaAmxxIiA5NDc2ZGUzYjUxYTU0NWE4MTVjYzg2MTEwOWMzYzZkMw; ssid_ucp_v1=1.0.0-KGJhN2UyMTg2MDI5ZjQ2ZDhiNmQ2M2FiMTA0ZGIxY2RjMGQwYWVlNTUKHwiEwauR_gIQpq6ZzgYY7zEgDDD4wKDbBTgHQPQHSAQaAmxxIiA5NDc2ZGUzYjUxYTU0NWE4MTVjYzg2MTEwOWMzYzZkMw; passport_csrf_token=a61920b8b8944d85f194954010032148; passport_csrf_token_default=a61920b8b8944d85f194954010032148; volume_info=%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.43%7D; dy_swidth=2048; dy_sheight=1280; playRecommendGuideTagCount=11; totalRecommendGuideTagCount=11; strategyABtestKey=%221774801446.994%22; ttwid=1%7Cbi8FDxpvqDxEQcHwQjDT06NprsmGdsoVdcWUaSQVw74%7C1774801448%7C9859a69909770cd21e5af9605ec199342105afc434cbdc1b54cf229a799b4fa7; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAsSnYSMZLcUc12iKKd2zu28mCgBEmKNQ3jpis7dBEgak%2F1774886400000%2F0%2F0%2F1774804203739%22; douyin.com; xg_device_score=7.0558880960500465; device_web_cpu_core=32; device_web_memory_size=8; architecture=amd64; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAsSnYSMZLcUc12iKKd2zu28mCgBEmKNQ3jpis7dBEgak%2F1774886400000%2F0%2F1774851988759%2F0%22; __ac_nonce=069ca179a00a9e71e8b68; __ac_signature=_02B4Z6wo00f01phDG7QAAIDCFg5tgXhl8k6YYx8AAM.n52; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1280%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A32%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQjVUd3FodVI3a2ZxLzNSVWo2RkxqQ042UGxYRUcwcm1FWnRONWVDUERSYjVUNmNFTG9RZmlTeFZ0UDNMZ2IxeXNWRjFPcWQ0UEFscG9ZbG5hWnl1NGs9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; biz_trace_id=8f8d5fac; odin_tt=44ccff25c8c70f5650fe9704d08acfffcee36d574f429ab8cf301f411074d78b0790dfd7e691b3ef6f2fd611b41f85b96082a8cb689c802d20841d0f35e56f2d; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e5927666d776a686028607d71606b766c6a6b3f2a2a756e756e636d6b666c63666e686e6e63606e6f686a616f636b6f6b63666368602a6c6b6f6066715666776c75712b6f76592758272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2736373c36343d37303d31323234272927676c715a75776a716a666a69273f2763646976602778; bit_env=nqQnZMWiHpT6LZ6P-PKOrU3EhW-aA11h9SHw9UkK9m-jhIHPqlgy6HL_Xz-lolecVamaC-S0hupTyyaEN0oeNWag34akMYzgh7XcRnVZqDxHTjphbmPV0O4z65kTna_0jwTZooEzMpYNoLRtPejCf5_MOWj1WqIAES3X97LSt60vCl0LkKb1mt3dSxvsRUmrZooLJ4LWu-YGLGEEFTLevpC4mZOzGWJQfLKgPHDlWKo71pGeDsXfxS6d0-83xy05Q6QQTvTq24qD6qjlHRi02Adgth7erb45IAH6vaToS4B-a6snjUX-V5_B2QeA4ciNLWnsyb019j_gi0xVTOMHFIB8eNK5MdFJhGs5qGCnc1BcOFWXtcJBvTpMNMnp5d77g7ZDf2k1HU8L39869sSJw_dk7pUK0vN4n--3cdozCOMAneNkdeWYheZ101tnKoRlZmPsbYju_bXJA-rofmtuwJIytjynf_XMVV9D-mIV_VWjdua54AjyYE3xA2a5yxQk2QWuNLN5R1UMEajO96WlEi9t0riojSeWKzr3Y6tqRas%3D; gulu_source_res=eyJwX2luIjoiZWQ4OTJkZTQxNGQ4NGI4MzgwNWEwYjA4MDY3MTA0MzU4MTFlNGFjOGQyYzEwZjAxMjZiMTJiYjAzYTEyZDlkNCJ9; passport_auth_mix_state=j4e0299mpn209n1go4153joikd2bjr4p; bd_ticket_guard_client_data_v2=eyJyZWVfcHVibGljX2tleSI6IkJCNVR3cWh1UjdrZnEvM1JVajZGTGpDTjZQbFhFRzBybUVadE41ZUNQRFJiNVQ2Y0VMb1FmaVN4VnRQM0xnYjF5c1ZGMU9xZDRQQWxwb1lsbmFaeXU0az0iLCJ0c19zaWduIjoidHMuMi42ZmQ3MTQ1MDVlNTViZjBmMzA5NThmMDRjODkxOTk1MzgxMmJhMjk3Njc5ZDdkODBkNmRhYWE0YjE2MjJhYWM4YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJra1c3aWJPTitkTUliT1RPUlB3TVZvZmQ0T3UwTmQ5NkVqWFV3SzNJRlVNPSIsInNlY190cyI6IiN5d3AxWUJWUG1iOGs2ZVRNZGt3dk8rWmxjczFINy92SGFxc2xTWHYzZzVoaStJN2FraUI5Sk0rVERmM00ifQ%3D%3D; IsDouyinActive=false',
        }

        params = {
            'from_tab_name': 'main',
            'modal_id': '7622914900192398627',
            'vid': '7622322995519819048',
        }
        return api, params, headers

    @staticmethod
    def get_search(query):
        api = 'https://www.douyin.com/aweme/v1/web/api/suggest_words/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'query': query,
            'business_id': '30088',
            'from_group_id': '7591861063445593515',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '100',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': 'EY8Wv_VuKTQkub3GI8EMJKtPxadgkyBkztqhVJy1dAZ1I7wvVwQs2ZQ_H4pLqQTVV60Ubs3VA5gr6qH-JqzKitJvDoZRz-s7gQlGkHdlds-W5njZBm0F4EVE3KO_feIAAtX_ACtHxZ_U1a6JvJ21OeCY1bfp-qYF3d6Th4TC0ezLnJkHotagA9U=',
            'a_bogus': 'dJUVhzSjDxQfOdKGmCYSH42lLA9Ars8yTeTKSNpPCxPGaHzGTRPBsOa8boF7hcOpvRBii9p7JV-AGjnc8UUTZFHpqmkDSD0j345IV8fohZrvGGkg1NRECyWzwXBcWcTue/53i1U6MUJyIDQ-NqQL/pV9SKLC5OmkKrdWk2ubO9kh1FgAE3cHPQGmYXJq',
        }
        return api, params
    
    @staticmethod
    def get_im_user_info():
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'update_version_code': '170400',
            'support_h265': '1',
            'support_dash': '1',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': '32',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '100',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': 'PPi1AOD1OiV9Ol0_JUMs4lZ5y0oxBocB_sebYHUSpxCtA66Wqg0_oebFvyoXuzVcn8EX2_OqHUb2ehbB8kYKyxyqZoOllsEvqyeBN-7P0CfHykidIeQbXVFemtgJHO6o-p4Dtp-QwHk506ZgzYELHy6a5ejWUErKLrKvFeFSekNToEYjpMbFk9E=',
            'a_bogus': 'YjUfktSyDN5fadFGuCYbHUPUe8dANPWysMiQWPxTyxFBa1FYaYPPsjc-aOFL5tAhv8Bki9V7jV-AbnDPm0X12K9kompvuLvWrU55V0vogZJIYBiZ1qfDCSWzLXsO85suaAVeiAR62UJyIEO-qrQ8/dV9yKLKQYmkKNd6k2zcx9p6ZMLADZc3PBb2EwGqBD==',
        }

        data = {
            'sec_user_ids': '["MS4wLjABAAAAM4Wb-xoU_SomU9vrUh-jFwESmgigZQfO6AcO389gb7M","MS4wLjABAAAAtnE3pd2_HefTYSxucJ68DC6Op-tcjRMkZPllMXnow8U","MS4wLjABAAAAz2gsw-TU7_LpPsaJuovXdiZHPQm_t3-3Ld2My0GDZVft_4-uzodWnjqiKXseHD9G","MS4wLjABAAAABWFboZ7bxjJ3VFNx4nkz-TCSOGC3xcOmung2POr4pfI","MS4wLjABAAAAvXCSaQksjNROR2rUnURFfkADpjdGeJ0ILGSm2BuLplg","MS4wLjABAAAAyq915_ojrI90Dlmf0hppV6iL8esQyVtOC-SCyEiexj0","MS4wLjABAAAAOkRZaaK18M4grAe9x78GYVo42YkCjsol5uvt_oUXYHeSA_IxTIEGV5XumJHo_3AU","MS4wLjABAAAAYtA8a5OjVvbD8Lf5M657w81XYOpZz1xLciP3p9Pe_ks","MS4wLjABAAAA5jtWF45wLjXiF-hH-aa4rn7TvNnwZy6iy2b2DgEPNx0","MS4wLjABAAAAJmvF8WCZtWAaOXg4rgCXBbMrPYZkdYe-XKukM2aYP_8hsq6crJ5dGM1jQHz-N0ej","MS4wLjABAAAAZPp2N7XSFcRPoYwryN9rw7Qm-OWq6rzXdnlaRVYLU3Q","MS4wLjABAAAAYWLOkZEEfIllqNjsssAkZv8JDnj2lMXBO4ivQGbK88U","MS4wLjABAAAArFNAYv57jOBJt6gTydRSQQ7watt1lHbE9AuW8-FDgK0","MS4wLjABAAAAuBrQst7pHibZUCz7pvrbITGQJwjb4Nj5lfsgJYyUXuA","MS4wLjABAAAAeME930x5sQ3UnVEbt7NMwneP2IPGVqzYeYiqN8CMqw4","MS4wLjABAAAA9TfSTvCa8MGTYA6sl3jCh_D7s8YOCnb5Fz29LLve5RdRIX2IgpxWnJjPv_lYkCEh","MS4wLjABAAAAbWGvpFR_7jusF4cXF4wx63IU45-R_cTLVeIsj0U5_FM","MS4wLjABAAAAkKr1HbKQdT3gfK_63Hy11Huf54qj3AowCkLgsu5hIvk","MS4wLjABAAAA_uI3Ihw7B-et5jC5Wg6z2By4NCm9Yq7DXS1_qttlGUQ","MS4wLjABAAAA95hVM-hMICRdjMK9dHvPHbvdJDqwgy8-hFzPoKq0tlU","MS4wLjABAAAAdSrToTpipen3zjGOWwwg5wFbgL0r5HQDOloFrO7N_uStRsgyt7516FTAw6wr4cWY","MS4wLjABAAAACHCbkrq_fapDpDNCAXbXxCHeIFEvHKZvBWfOKGqOu_E","MS4wLjABAAAATVjvVRC0UlgjhtzddDKkVvHqLCxJ0oQkGtws_gEP63enHTPySc65KkWyW3vxYAch","MS4wLjABAAAAtVLSJ3x_5K3SzXdIpSi2o_Z7VJrdcz_lV7rerRLvm3o","MS4wLjABAAAAdkSGzwF-StH4OxJ9FdDSqNXmFbJM1SjhR5CmNVh8_y3cnZmWNiMyUNZofFlx3S9L","MS4wLjABAAAAaOoaTUiFjZi8ElUyJXL5N6Z4CNVL1Qcg_IxZbTlov34","MS4wLjABAAAAE--a_x6_ItBCfELDKPu-suP-Aty5v4vEuQbDR69wDsoVrbQm3TZAmCHGAYRPjaFR","MS4wLjABAAAAK2kRJAvgHaPZwHk7177uaTp_G3o3p8497dBS3VNMn8J8fM1fX76ZsnNGcpVct8mq","MS4wLjABAAAAIDYpxkIgv7SUYV-2G1HBhuxGpdZBjc8pPl9kg8_4B8s","MS4wLjABAAAA41gfLQL-c2s_GUGfzFEdD_xOU9lbAHWKSUTs54EWFXZ-gYVTaB9rktJsXiqkeT0h","MS4wLjABAAAAfdyhCNy8uLrvNHl6PPEq_vbdlvg_GouN_TQxyVltZBQ","MS4wLjABAAAAr6kRvmm_iwYWysbQRkuCVn_l_rnfokrW9iEIZGoOesE","MS4wLjABAAAAnKUOCPR3G0ohe8BvREdSwWik1T-lWImyAk-LYx0ucok","MS4wLjABAAAAJnovPUmSgSB_gciCItB6BsNH__SrjiDaU0zYmyNu7CY","MS4wLjABAAAAF4gikAIzNbe5D3zQ-3bYGjut3XxdbAOpPdsf8RmbtGk","MS4wLjABAAAAcU_WwhxbxUva7l8af9fpgrhu1J4T21L0oAgsH62SDCPvyLDYwfva2fEIcsgadePa","MS4wLjABAAAAUBEzXDkZh6VmYrfDcZaC7JHz_Ty4woL6K21byvuTbleo2cpmusHVRztdJa6lM3MZ","MS4wLjABAAAArtV5x3EDaKLt2SyxhdQzdbe179tAwOMG0i5bKObWV7w","MS4wLjABAAAAP4j-tVRTgWa21iD_G9mBiMv2FVYjLC9oezra55XNkmA","MS4wLjABAAAAgmR0HBUktGtf_kKySD7hNm7FYvh8xYlbmv5ww5oGTvM"]',
        }

    @staticmethod
    def get_user_info():
        api = 'https://www-hj.douyin.com/aweme/v1/web/query/user/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'publish_video_strategy_type': '2',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '100',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': 'x5EMIUBSIy9W290BJZIGK6j7duDFaXwZYKaSewH8Nxp1QtRvGDfKcjy4M7c-I6Vae1elAW6SGNB3a-BZO-VfE_5ptjmTUwOKN4zsdCWkOosSE7woU5J75zH-FHm-1AT9yqjUgkAvpyr1MFyYc3G_h4clKarjd9zCpX_akm-5PhH5B1HKYOuRN3U=',
            'a_bogus': 'Yv4nDeUyON55Od/tmKYyHUBUrz2lrP8yuaTKSSxTCOKMPXUYGYPF0Pc4cxF7QtChXRBzieI7jV4lYfVcu0XiZqHpzmpvSZTW1s55VhvL/Zr2bTJZHHRLCyRzFXsaWR4ulQ5-i1R62UJ7IEQ-qNdm/p39HKoeQOYkKqQykMucN9ph10gAg3cePQSgThkq5E==',
        }
        return api, params
    
    @staticmethod
    def get_relation():
        api = 'https://www-hj.douyin.com/aweme/v1/web/im/spotlight/relation/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'count': '50',
            'source': 'coldup',
            'max_time': '1774937974946',
            'min_time': '0',
            'need_remove_share_panel': 'true',
            'need_sorted_info': 'true',
            'with_fstatus': '1',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '250',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': 'vhDKtKqjbUVRyku9iQqTVQ5sOZOQAzS3wquivXbrNVWrovGVP17xqRFK4F3i6WcmyHY7vM7_e70KH35VeLvyRdFPcppWyOA3uFyrgEBMC_-c1vSWGO8ApiYmEzXGy9lqcThRWyGz6VzNKSSA8fGjdUhuxXvpNvwz8VT4pN0qatwLRw==',
            'a_bogus': 'xJURgeyjmom5Kd/SYCEjHAFlfXylNP8yHeixRa-PHNTbP1eY1uPPzOazaowLzO9iO8BhwCA7cVUlYxVb8UXiZFnpqmpDuM0f8455Ih8ohqHgT4ig1NfgC7RFwXBO8Rsua/5riIWIZUJyIx5-ZHdL/B399KLe5Ybk/rdjkMucN9k6ZMgAgpc1PQGpxwJeUc5G',
        }
        return api, params
    
    @staticmethod
    def get_followings(offset: int = 0):
        api = 'https://www-hj.douyin.com/aweme/v1/web/user/following/list/'
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'user_id': '102578708612',
            'sec_user_id': 'MS4wLjABAAAAsSnYSMZLcUc12iKKd2zu28mCgBEmKNQ3jpis7dBEgak',
            'offset': f'{offset}',
            'min_time': '0',
            'max_time': '0',
            'count': '20',
            'source_type': '4',
            'gps_access': '0',
            'address_book_access': '0',
            'is_top': '1',
            'update_version_code': '170400',
            'pc_client_type': '1',
            'pc_libra_divert': 'Windows',
            'support_h265': '1',
            'support_dash': '1',
            'cpu_core_num': '32',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '2048',
            'screen_height': '1280',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Edge',
            'browser_version': '146.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '146.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '250',
            'webid': '7578114874557318683',
            'uifid': '29a1f63ec682dc0a0df227dd163e2b46e3a6390e403335fa4c2c6d1dc0ec5ffa8aa6438c57fda3f18128b16e092adfd0bee65d4dc8858ba767cd584c3a76aee55be56012dffde7c23c10f7c09e01d8e7cc89656607415db684e60776b43fbac457ad15a0e1ccd09fe52ba7c81e2d0cd64431c06eb29927d3094726bdfb6263acb7aff8159e4a787cbe677f88a6821f1f7209084d97ca445990a4eb956b93618d',
            'verifyFp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'fp': 'verify_mli2bv6l_14F6uUN1_qK2Z_49TD_BjJn_MbopWnRtpZaj',
            'msToken': 'F0kPDGU38Gd8N6XWV1GpcpD4aBISvwmWA5UyqC3nYxvE8W3E3WZR223Pn68FEKhYQeC9y6ASVK3RqSNR9nBKwEhPZdvHLb66hwGH1OF5Dvxl5e9MU0R5PpGy93WUJQqDEBsvGLfb8PpsgFVjYvKRclUsDU9shnGelkkqNyD3MK0dF3nd9CUPJgM=',
            'a_bogus': 'dfURDe7wOZ/nPdMb8KEfHlNU5gyArTWykBTdbeKPSNPNPHtbrmPPTxckJozLL5FM/mB0wClHrVUlbdxbu0UiZK9pompDS0ifu4VcI0mL01q3YPiZHHRYC7RzFXBP8bsu-/5-iAR62UJL2dQ-pNdg/BI97KLKQYYkOrQfk2ucx9k6ZFgALZclPdtkTwJzUAoy',
        }
        return api, params
    
    @staticmethod
    def getaaa():
        """
        搜索页面的视频下载链接接口
        """
        api = 'https://www.douyin.com/aweme/v1/web/general/search/single/'
        api = 'https://www.douyin.com/aweme/v1/web/general/search/stream/'

    @staticmethod
    def get_ms_token():
        tsp = int(time.time() * 1000)
        api = 'https://mssdk.bytedance.com/web/common'
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://www.douyin.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.douyin.com/',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-storage-access': 'active',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'cookie': 'ttwid=1%7Cbi8FDxpvqDxEQcHwQjDT06NprsmGdsoVdcWUaSQVw74%7C1771701228%7Ce09c06607627cf98b395d27c5c867e235b2cf9a0a5c451859db96eb0a2e47c6c',
        }

        params = {
            'ms_appid': '6383',
            'msToken': 'pJ3gAxj3j9bSPpMU4TlXZevFEyiQ1Q-TLcGPx5joTuLJX-cVgz94-luV7OHp264aggMPjyGmXGi_5IGbHmWGY2fUMAjxv5R0k8Bv3gxA1iKGWo1jJGk6c74oetRUKCayPnXjKieuFbrUcuWMYhwVHR4a4MGTo44Z1658dX7eh3G48BDkhuS1p38Z',
        }

        data = '{"magic":538969122,"version":1,"dataType":8,"strData":"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","tspFromClient":' + str(tsp) + ',"ulr":0}'

        return api, headers, params, data
