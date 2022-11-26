"""
@author hujing
"""
from enum import Enum, auto


class DepotType(Enum):
    CatBox = auto()
    """
    图床
    url: https://catbox.moe/
    """
    Ai58 = auto()
    """
    58同城客服, 在线上传图片
    url: https://ai.58.com
    """
