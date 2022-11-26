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
    PngCm = auto()
    """
    图床
    url: https://png.cm/
    """
    Riyugo = auto()
    """
    链接存在有效期
    url: https://riyugo.com/
    """
    Ai58 = auto()
    """
    58同城客服, 在线上传图片
    url: https://ai.58.com
    """
