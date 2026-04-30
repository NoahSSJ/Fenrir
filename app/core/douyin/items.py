
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from base import BaseDataClass


class FollowingsItem(BaseDataClass):
    avatar_thumb: str
    nickname: str
    sec_uid: str
    signature: str
    uid: str
    unique_id: str 
    short_id: str 
    aweme_count: str


class CommentItem(BaseDataClass):
    cid: str
    ip: str
    name: str
    text: str
    time: str

