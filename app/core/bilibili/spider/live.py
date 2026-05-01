from pprint import pprint
import sys
from pathlib import Path
import json
import re
sys.path.append(str(Path(__file__).parent.parent / "api"))
from live import BiliBiliLiveApi
class BiliBiliLiveSpider():
    @staticmethod
    def get_live_info(session):
        api, params, headers = BiliBiliLiveApi.get_live_info()
        response = session.get(api, params=params, headers=headers) 
        # print(response.text)
        pattern = r"window\.__NEPTUNE_IS_MY_WAIFU__\s*=\s*(\{.*?\})\s*;?\s*</script>"
        match = re.search(pattern, response.text, re.DOTALL)

        if match:
            json_str = match.group(1)
            # print(json_str)
            data = json.loads(json_str)
            # pprint(data)
        else:
            print("没匹配到")

        streams = data["roomInitRes"]["data"]["playurl_info"]["playurl"]["stream"]
    
        result = []
        for s in streams:
            protocol = s["protocol_name"]
            for f in s["format"]:
                fmt = f["format_name"]
                for c in f["codec"]:
                    codec = c["codec_name"]
                    base_url = c["base_url"]
                    qn = c["current_qn"]
                    
                    # 每个 codec 可能有多个 CDN,都收集起来
                    for u in c["url_info"]:
                        full_url = u["host"] + base_url + u["extra"]
                        result.append({
                            "protocol": protocol,
                            "format": fmt,
                            "codec": codec,
                            "qn": qn,
                            "url": full_url,
                        })
        print(result)
        # return result