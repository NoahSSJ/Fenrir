import json
import math
import os
from pathlib import Path
from pprint import pprint
import random
import re
import subprocess
import sys
import time

import execjs
from loguru import logger
sys.path.append(str(Path(__file__).parent.parent / "api"))
sys.path.append(str(Path(__file__).parent))
from video import BiliBiliVideoApi
from .fetch import BiliBiliSpider
from .utils import BiliBiliUtils    
# from grpc_tools import protoc


class BiliBiliMedia(BiliBiliSpider):
    @staticmethod
    def get_one_media(**kwargs):
        """
        Note:下载博主某个视频
        Args:
            task (str): 任务字符串，包含视频url
            url (str): 视频url
            MinIOClient (MinIOClient): MinIO客户端实例, 可以传也可以不传
        example:
            下载保存到本地
            url = "https://www.bilibili.com/video/BV1uLWQzqEmj/?spm_id_from=333.337.search-card.all.click"
            a.get_one_media(url=url)

            下载保存到MinIO存储
            minio_client = MinIOClient()
            a.get_one_media(url=url, MinIOClient=minio_client)

        Returns:
            tuple: (video_url, audio_url, output_file)
        """
        task = kwargs.get("task")
        if task:
            task = json.loads(task)
            url = task["url"]
        else:
            url = kwargs.get("url")
            if not url:
                raise ValueError("必须提供 url 或 task 参数")
        response = BiliBiliSpider.session.get(url)
        print(response.text)
        title = re.findall(r'<title>(.*?)_哔哩哔哩_bilibili</title>', response.text)[0]
        print(title)
        author = re.findall(r'<meta data-vue-meta="true" itemprop="author" name="author" content="(.*?)">', response.text)[0]
        print(author)
        json_str = re.findall(r'window\.__playinfo__\s*=\s*({.*?});?\s*</script>', response.text, re.DOTALL)[0]
        json_dict = json.loads(json_str)
        # pprint(json_dict)
        video_url = json_dict['data']['dash']['video'][0]['backupUrl'][0]
        audio_url = json_dict['data']['dash']['audio'][0]['backupUrl'][0]
        # if kwargs["mode"] == "api":
        #     return video_url, audio_url
        # print(video_url)
        # print(audio_url)
        video_file = f"{title}_video.m4s"
        audio_file = f"{title}_audio.m4s"
        
        download_dir = Path(__file__).parent.parent.parent / "download" / author / "media"
        os.makedirs(download_dir, exist_ok=True)
        output_file = download_dir / f"{title}.mp4"
        
        with open(video_file, 'wb') as f:
            f.write(BiliBiliSpider.session.get(video_url).content)
        
        with open(audio_file, 'wb') as f:
            f.write(BiliBiliSpider.session.get(audio_url).content)
        
        cmd = [
            'ffmpeg',
            '-i', video_file,
            '-i', audio_file,
            '-c', 'copy',           # 视频和音频都直接拷贝，不重新编码
            '-map', '0:v:0',        # 取第一个视频流
            '-map', '1:a:0',        # 取第一个音频流
            output_file,
            '-y'                    # 覆盖已有文件
        ]
        subprocess.run(cmd)

        os.remove(video_file)
        os.remove(audio_file)
        # print(url)
        print(f"下载完成：{output_file}")
        if kwargs.get("MinIOClient"):
            kwargs.get("MinIOClient").upload_file("author", output_file, output_file)
        return video_url, audio_url, output_file
    
    

    def get_all_media(self):
        """
        下载博主所有视频, 同步顺序下载, 未使用REDIS
        """
        video_nums = BiliBiliSpider.utils.get_nav_num(self.mid)
        end = math.ceil(video_nums / 40)
        pn = 1
        cnt = 1
        while True:
            # if (pn >= end):
            #     break
            api, params = BiliBiliApi.get_search(pn)
            config = {
                "wbiImgKey": "7cd084941338484aae1ad9425b84077c",
                "wbiSubKey": "4932caff0ff746eab6f01bf08b70ac45"
            }

            with open("wid.js", mode='r', encoding='utf-8') as f:
                js_code = f.read()
            ctx = execjs.compile(js_code)
            wid = ctx.call("XN", params, config)
            # print(wid)
            params.update(wid)
            response = BiliBiliSpider.session.get(url=api, params=params)
            json_dict = json.loads(response.text)
            pprint(json_dict)
            for i in json_dict['data']['list']['vlist']:
                author = i['author']
                bvid = i['bvid']
                title = i['title']
                oid = i['aid']
                url = f"https://www.bilibili.com/video/{bvid}/?spm_id_from=333.1387.upload.video_card.click&vd_source=cd2f30c4c2b17931e5fe4b95752072ee"
                BiliBiliSpider.get_one_media(url=url)
                logger.info(f"序号: {cnt} | 作者: {author} | BV: {bvid} | 标题: {title} | oid: {oid} | url: {url} | 下载完成")
                cnt += 1

            pn += 1
            time.sleep(random.uniform(1.3, 4.1))
            break


    def procduce_all_media(self, r):
        """
        Note: 下载博主所有视频, 同步顺序下载, 使用REDIS, 遵循"PRODUCER-CONSUMER模式, 可选择保存在本地文件夹或者存储在MinIO中"

        Args:
            None

        ReturnS:
        """
        video_nums = BiliBiliSpider.get_nav_num(self.mid)
        end = math.ceil(video_nums / 40)
        pn = 1
        cnt = 1
        while True:
            if (pn >= end):
                break
            api, params = BiliBiliApi.get_search(pn)
            config = {
                "wbiImgKey": "7cd084941338484aae1ad9425b84077c",
                "wbiSubKey": "4932caff0ff746eab6f01bf08b70ac45"
            }

            with open("wid.js", mode='r', encoding='utf-8') as f:
                js_code = f.read()
            ctx = execjs.compile(js_code)
            wid = ctx.call("XN", params, config)
            # print(wid)
            params.update(wid)
            response = BiliBiliSpider.session.get(url=api, params=params)
            json_dict = json.loads(response.text)
            pprint(json_dict)
            for i in json_dict['data']['list']['vlist']:
                author = i['author']
                bvid = i['bvid']
                title = i['title']
                oid = i['aid']
                if r.r.sismember(f"{os.getenv('REDIS_DOWNLOADED_SET')}: {self.mid}", bvid):
                    continue
                url = f"https://www.bilibili.com/video/{bvid}/?spm_id_from=333.1387.upload.video_card.click&vd_source=cd2f30c4c2b17931e5fe4b95752072ee"
                task = json.dumps(
                    {   
                        "mid": f"{self.mid}",
                        "author": author,
                        "oid": oid,
                        "bvid": bvid,
                        "title": title,
                        "url": f"https://www.bilibili.com/video/{bvid}/?spm_id_from=333.1387.upload.video_card.click&vd_source=cd2f30c4c2b17931e5fe4b95752072ee"
                    }
                )
                r.r.lpush(f"{os.getenv('REDIS_TASK_PREFIX')}: {self.mid}", task)
                logger.info(f"序号: {cnt} | 作者: {author} | BV: {bvid} | 标题: {title} | oid: {oid} | url: {url} | 下载完成")
                cnt += 1

            pn += 1
            time.sleep(random.uniform(1.3, 4.1))
            break

    def consume_all_media(self, r):
        """
        Note: 下载博主所有视频, 同步顺序下载, 使用REDIS, 遵循"PRODUCER-CONSUMER模式, 存储在本地文件夹中"

        Args:
            r: RedisConfig对象

        ReturnS:
        """
        task_key = f"{os.getenv('REDIS_TASK_PREFIX')}:{self.mid}"
        print(task_key)
        task_cnt = 1
        while True:
            task = r.r.rpop(task_key)
            print(task)

            if not task:
                break
            # BiliBiliSpider.get_one_media(url=task['url'])
            time.sleep(random.uniform(1.5,4.5))
            task_cnt += 1
            if task_cnt == 2:
                break
    
    @staticmethod
    def get_danmaku(url):
        pid, _, oid = BiliBiliUtils.get_video_id(url, BiliBiliSpider.session)
        api, params = BiliBiliVideoApi.get_danmaku(oid, pid)
        params = BiliBiliUtils.get_wid_signature(params)
        response = BiliBiliSpider.session.get(url=api, params=params)
        print(response.status_code)
        
        # === 2. 计算文件路径（基于当前文件所在目录，避免运行目录不同导致找不到文件） ===

        current_dir = str(Path(__file__).parent)
        pb_path = Path(__file__).parent / 'bullet_screen.pb'
        proto_path = Path(__file__).parent / 'dm.proto'
        py_path = Path(__file__).parent / 'dm_pb2.py'


        # === 3. 保存二进制数据 ===
        with open(pb_path, 'wb') as f:
            f.write(response.content)

        # === 4. 自动编译 dm.proto（仅在需要时编译） ===
        need_compile = (
            not os.path.exists(py_path) or
            os.path.getmtime(proto_path) > os.path.getmtime(py_path)
        )
        if need_compile:
            print('编译 dm.proto ...')
            protoc.main([
                'grpc_tools.protoc',
                f'--python_out={current_dir}',
                f'--proto_path={current_dir}',
                proto_path,
            ])
        

        # import sys
        # if current_dir not in sys.path:
        #     sys.path.insert(0, current_dir)
        import dm_pb2
        
        danmaku_seg = dm_pb2.DmSegMobileReply()
        danmaku_seg.ParseFromString(response.content)
        
        # === 6. 输出弹幕 ===
        print(f'\n一共 {len(danmaku_seg.elems)} 条弹幕\n')
        for elem in danmaku_seg.elems:
            print(f'时间: {elem.progress}ms | 内容: {elem.content}')
        
        # 把弹幕列表返回出去，方便外部使用
        return danmaku_seg.elems
        

if __name__ == '__main__':
    # a = BiliBiliMedia()
    # a.get_one_media(url="https://www.bilibili.com/video/BV1uLWQzqEmj/?spm_id_from=333.337.search-card.all.click")
    print(sys.path)
    
    print(current_dir)